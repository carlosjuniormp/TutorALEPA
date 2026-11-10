# TutorALEPA — Base de conhecimento do concurso ALEPA 2026

**Data-base:** 10/11/2026. **Revisão:** em desenvolvimento. As matrizes são resumos rastreáveis dos Anexos II e retificações 002/003, não substituem a redação integral do edital.

## Fontes primárias oficiais
- [001/2026 — nível médio](https://fundacaocetap.selecao.net.br/informacoes/155/) — última retificação listada 004/2026, 09/11.
- [002/2026 — nível superior](https://fundacaocetap.selecao.net.br/informacoes/156/) — última retificação listada 005/2026, 09/11.
- [003/2026 — procurador](https://fundacaocetap.selecao.net.br/informacoes/157/) — última retificação listada 005/2026, 09/11 (não incluído na matriz prioritária).

## Comece por aqui
1. **[MATRIZ DE DISCIPLINAS E TÓPICOS POR CARGO](base/matriz-cargos-001-002.md)** — MED-04 PL.AL.060, SUP-02 e SUP-03 PL.AL.102, SUP-15 PL.AL.070.
2. **[CONTROLE DE RETIFICAÇÕES](base/retificacoes-e-integridade.md)** — mudanças de numeração e alcance.
3. [Plano de atualização das apostilas](base/plano-revisao-apostilas.md)
4. [Inventário de documentos oficiais](base/fontes-oficiais.md)
5. [Errata confirmada](base/errata-confirmada.md)
6. [Auditoria dos nove materiais recebidos](base/auditoria-materiais.md)
7. [Instruções para o tutor](prompts/tutor.md)

## Regras
- Precedência: edital vigente com retificações > outras referências > apostilas.
- **PL.AL.102 identifica dois cargos distintos**: Assessor Técnico (02) e Técnico Legislativo (03).
- **PL.AL.070 é o cargo 15 — Assistência Legislativa**, corrigido pela Retificação 003/2026, e usa conteúdos próprios da Retificação 002/2026.
- Não reproduzir apostilas licenciadas nem expor suas marcas d'água num repositório público.
- Nem todas as 1.285 páginas privadas, normas citadas ou detalhes de todos os editais estão auditados. Status e lacunas devem ser declarados.

## Base pesquisável (fase técnica)
- [Dados de cargos](data/cargos.json) e [50 tópicos iniciais estruturados](data/topicos.json)
- [Busca local em Python](tutoralepa.py), [guia de consulta](base/como-consultar.md) e [testes](tests/test_tutoralepa.py)
- [Workflow de validação GitHub Actions](.github/workflows/validar-base.yml)
- [Questões validadas](data/questoes.json): coleção ainda vazia por exigência de revisão jurídica e de procedência.

Exemplos:
```bash
python tutoralepa.py validar
python tutoralepa.py buscar "orçamento" --trilha SUP-15
python -m unittest discover -s tests -v
```
**Limitações:** busca por títulos e tags, não por texto integral de PDF; não é aplicativo web. Acompanhamento lê arquivo de tentativas local, não mantém conta/sincronização de aluno. A aprovação da suíte de testes no GitHub Actions depende de execução e deve ser verificada na aba Actions.
