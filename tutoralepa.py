#!/usr/bin/env python3
"""Consulta local à base TutorALEPA. Python 3.9+; somente biblioteca padrão."""
import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VALID_TRILHAS = {"MED-04", "SUP-02", "SUP-03", "SUP-15"}


def load(name):
    with (ROOT / "data" / name).open(encoding="utf-8") as handle:
        return json.load(handle)


def normalize(value):
    value = unicodedata.normalize("NFKD", str(value)).casefold()
    return re.sub(r"[^a-z0-9]+", " ", "".join(ch for ch in value if not unicodedata.combining(ch))).strip()


def validate():
    cargos = load("cargos.json")["cargos"]
    topics = load("topicos.json")["topicos"]
    assert {c["trilha"] for c in cargos} == VALID_TRILHAS
    ids = set()
    for item in topics:
        assert item["trilha"] in VALID_TRILHAS
        assert item["id"] not in ids, "ID duplicado"
        ids.add(item["id"])
        assert item["fonte"]["url"].startswith("https://")
        assert item["status"] in {"resumo_tematico_a_detalhar", "confirmado", "pendente"}
    questions = load("questoes.json")["questoes"]
    for item in questions:
        assert item["trilha"] in VALID_TRILHAS
        assert item["status_validacao"] == "validada"
        assert item["id"] and item["enunciado"] and item["justificativa"]
    return len(cargos), len(topics), len(questions)


def search(query="", trilha=None, disciplina=None, limit=20):
    if trilha and trilha not in VALID_TRILHAS:
        raise ValueError("Trilha inválida: " + trilha)
    words = normalize(query).split()
    items = load("topicos.json")["topicos"]
    matches = []
    for t in items:
        if trilha and t["trilha"] != trilha:
            continue
        if disciplina and normalize(disciplina) not in normalize(t["disciplina"]):
            continue
        haystack = normalize(" ".join([t["titulo"], t["disciplina"], t["id"], " ".join(t["tags"])]))
        if words and not all(w in haystack for w in words):
            continue
        matches.append(t)
    return matches[:limit]


def progress(path, trilha):
    """Resumo de tentativas particulares de um arquivo JSONL local, não sincronizado."""
    if trilha not in VALID_TRILHAS:
        raise ValueError("Trilha inválida")
    p = Path(path)
    if not p.exists():
        return {"trilha": trilha, "tentativas": 0, "acertos": 0, "taxa": None}
    values = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("trilha") == trilha:
            values.append(row)
    n = len(values)
    hits = sum(row.get("correta") is True for row in values)
    return {"trilha": trilha, "tentativas": n, "acertos": hits, "taxa": round(100 * hits / n, 1) if n else None}


def main():
    parser = argparse.ArgumentParser(description="Busca por cargo na base ALEPA")
    commands = parser.add_subparsers(dest="command", required=True)
    find = commands.add_parser("buscar")
    find.add_argument("termo", nargs="?", default="")
    find.add_argument("--trilha", choices=sorted(VALID_TRILHAS))
    find.add_argument("--disciplina")
    find.add_argument("--limite", type=int, default=20)
    commands.add_parser("validar")
    show = commands.add_parser("cargos")
    stats = commands.add_parser("progresso")
    stats.add_argument("--arquivo", default="progresso-local.jsonl")
    stats.add_argument("--trilha", choices=sorted(VALID_TRILHAS), required=True)
    args = parser.parse_args()
    if args.command == "validar":
        c, t, q = validate()
        print(f"OK: {c} trilhas, {t} tópicos, {q} questões validadas")
    elif args.command == "buscar":
        print(json.dumps(search(args.termo, args.trilha, args.disciplina, max(0, args.limite)), ensure_ascii=False, indent=2))
    elif args.command == "cargos":
        print(json.dumps(load("cargos.json")["cargos"], ensure_ascii=False, indent=2))
    elif args.command == "progresso":
        print(json.dumps(progress(args.arquivo, args.trilha), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
