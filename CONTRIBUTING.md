# Guia de Contribuição / Contributing Guide

Obrigado por querer contribuir com o **Awesome AI Tools for AEC**! Este projeto é colaborativo e sua ajuda é fundamental para mantê-lo relevante e atualizado.

Thank you for wanting to contribute to **Awesome AI Tools for AEC**! This project is collaborative and your help is essential to keep it relevant and up to date.

## Como Contribuir

### Adicionando um novo recurso

1. **Fork** este repositório
2. Crie uma **branch** para sua contribuição: `git checkout -b add/nome-do-recurso`
3. Edite o `README.md` seguindo os padrões abaixo
4. Faça **commit** das suas alterações: `git commit -m "Add: nome do recurso"`
5. Envie um **pull request**

### Critérios para inclusão

Para que um recurso seja incluído, ele deve:

- Ser **relevante para o setor AEC** (Arquitetura, Engenharia e Construção)
- Estar em uma das categorias existentes (ou justificar uma nova categoria)
- Ter **documentação mínima** ou um README compreensível
- Estar **funcional** ou em estágio de desenvolvimento claro
- **Não ser spam** ou autopromoção sem valor real

### Formato de entrada

#### MCP Servers

Adicione na tabela da categoria correspondente, seguindo o formato:

```markdown
| [Nome do Projeto](URL) | Descrição breve e objetiva do que faz. | Linguagem |
```

#### Aplicações de IA

```markdown
| [Nome da Ferramenta](URL) | Descrição breve e objetiva do que faz. |
```

#### Skills & Rules

Se você tem Skills ou Rules para compartilhar:

1. Descreva brevemente o objetivo da Rule/Skill
2. Inclua a aplicação principal (ex: "Desenvolvimento de plugins Revit")
3. Se possível, adicione um link para o arquivo ou gist

### Padrões de escrita

- Descrições devem ser **concisas** (1-2 frases)
- Use **português** para descrições
- Inclua a **linguagem de programação** quando aplicável
- Mantenha a **ordem alfabética** dentro de cada categoria
- Não use adjetivos promocionais exagerados

### Validação local do catálogo / Local catalog checks

PT: Atualize as entradas em `README.md` e `README.pt-BR.md`, com o mesmo URL em ambos. Mantenha o H1 na primeira linha, a descrição preenchida, URLs `http(s)`, a largura e o separador das tabelas. Insira novos itens em ordem alfabética na categoria; o CI não reorganiza itens antigos. Antes de abrir um PR, execute:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_readmes.py --base-ref main
```

EN: Update both `README.md` and `README.pt-BR.md` with the same URL. Keep the H1 on the first line, a nonempty description, `http(s)` URLs, valid table widths/separators, and new items alphabetically placed in their category. Run the commands above before opening a PR. `--base-ref` is required and compares with a Git commit; the default head is your working tree (including uncommitted README edits). For two Git refs, use `--base-ref <base> --head-ref <head>`; the validator reads them using `git show` and never runs their code. Omitting `--base-ref` is an error, not a successful validation.

PT/EN: A verificação é incremental: compara erros novos com o baseline, sem bloquear dívidas antigas, e detecta desequilíbrio novo ou agravado de URLs entre idiomas por adição ou remoção. Em `pull_request` e `push`, o workflow usa código do SHA do evento com token somente leitura, sem segredos e sem persistir credenciais. Para `workflow_dispatch`, usa código de `main`; informe opcionalmente um número positivo de PR para checar seus READMEs somente como dados (`git show`), sem executar código desse PR. Sem PR, compara `main` com seu commit anterior; em `push` compara os SHAs do evento. A checagem é apenas sintática/estrutural: não acessa sites nem atesta disponibilidade, relevância para AEC, encaixe na categoria ou ausência de spam. Essas decisões exigem revisão humana. CI verde não é aprovação de produto.

## Sugerindo melhorias

Além de adicionar recursos, você pode:

- **Reportar links quebrados** — abra uma issue
- **Sugerir novas categorias** — abra uma issue com justificativa
- **Corrigir informações** — envie um PR
- **Melhorar descrições** — envie um PR

## Template para Issues

### Novo recurso

```
**Nome:** [Nome do projeto]
**URL:** [Link]
**Categoria:** [BIM, GIS, Estrutural, etc.]
**Descrição:** [O que faz e por que é relevante para AEC]
**Linguagem:** [Python, TypeScript, C#, etc.]
```

### Link quebrado

```
**Recurso:** [Nome]
**URL atual:** [Link quebrado]
**URL correta:** [Novo link, se souber]
```

## Código de Conduta

Ao contribuir, você concorda em seguir nosso [Código de Conduta](CODE_OF_CONDUCT.md).

---

Obrigado por ajudar a construir uma comunidade mais forte de IA para AEC!
