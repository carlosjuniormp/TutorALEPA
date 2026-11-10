# Como consultar a base

## Pré-requisito
Python 3.9+ (nenhum pacote externo). Clone o repositório:
```bash
git clone https://github.com/carlosjuniormp/TutorALEPA.git
cd TutorALEPA
```

## Comandos
```bash
python tutoralepa.py validar
python tutoralepa.py cargos
python tutoralepa.py buscar "orçamento" --trilha SUP-15
python tutoralepa.py buscar "arquivologia" --trilha MED-04
python tutoralepa.py buscar "direito processual civil" --trilha SUP-02
python tutoralepa.py progresso --trilha MED-04 --arquivo progresso-local.jsonl
python -m unittest discover -s tests -v
```

A busca é lexical, tolera acentos e filtra por trilha. Ela pesquisa **títulos temáticos e identificadores**; não faz busca semântica em PDFs e não acessa automaticamente as páginas da CETAP.

## Dados, fontes e níveis de confirmação
- `data/cargos.json`: quatro trilhas, com identificação completa.
- `data/topicos.json`: 50 **registros temáticos sintéticos**, não 50 capítulos auditados. Cada registro contém o identificador, fonte, bloco geral/específico e estado de verificação.
- `data/fontes.json`: três páginas oficiais de concurso.
- `data/questoes.json`: coleção vazia de propósito; não há questões licenciadas nem gabaritos ainda validados.

Não use o campo `status=resumo_tematico_a_detalhar` para afirmar que um subtópico ou apostila foi auditado integralmente.

## Acompanhamento de estudos
O comando `progresso` lê um arquivo local, privado, JSON Lines. Exemplo de linha que o aluno pode gerar em seu próprio computador:

```json
{"trilha":"MED-04","questao_id":"EXEMPLO-01","correta":true,"data":"2026-11-10"}
```

Esse exemplo é apenas ilustrativo, não uma questão validada. Nunca enviar logs com desempenho pessoal para repositório público.

## Próxima evolução
1. Auditoria literal de cada subitem do Anexo II com página, seção, texto e retificação.
2. Revisão dos exercícios privados sem publicar seus textos no repositório público.
3. Inclusão somente de questões originais autorizadas e com justificativas verificadas.
4. Interface web e sincronização privada de desempenho, se autorizadas, sem expor dados.
