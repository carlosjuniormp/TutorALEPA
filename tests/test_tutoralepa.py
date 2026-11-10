import unittest
from pathlib import Path
import tempfile
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tutoralepa import load, normalize, progress, search, validate


class TestTutorALEPA(unittest.TestCase):
    def test_integridade(self):
        cargos, topicos, questoes = validate()
        self.assertEqual(cargos, 4)
        self.assertGreaterEqual(topicos, 40)
        self.assertEqual(questoes, 0)

    def test_acentos_e_busca(self):
        self.assertEqual(normalize("Legislação e Ética"), "legislacao e etica")
        result = search("orçamento", trilha="SUP-15")
        self.assertTrue(any("contabilidade" in x["disciplina"] for x in result))
        self.assertTrue(all(x["trilha"] == "SUP-15" for x in result))

    def test_duplicidade_codigo_cargo(self):
        cargos = load("cargos.json")["cargos"]
        code = [c for c in cargos if c["codigo"] == "PL.AL.102"]
        self.assertEqual(len(code), 2)
        self.assertEqual({c["trilha"] for c in code}, {"SUP-02", "SUP-03"})

    def test_nao_mistura_especificos(self):
        result = search(trilha="SUP-15")
        self.assertFalse(any(x["disciplina"] == "direito-processual-civil" for x in result))
        for trilha in ("SUP-02", "SUP-03"):
            self.assertTrue(search("direito processual civil", trilha=trilha))

    def test_registro_vazio(self):
        with tempfile.TemporaryDirectory() as folder:
            row = progress(str(Path(folder) / "faltando.jsonl"), "MED-04")
            self.assertIsNone(row["taxa"])
            self.assertEqual(row["tentativas"], 0)


if __name__ == "__main__":
    unittest.main()
