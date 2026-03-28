# Awesome AI Tools for AEC [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Uma lista curada de servidores **Model Context Protocol (MCP)**, **Skills**, **Rules** e **aplicações de IA** voltados para o setor de **Arquitetura, Engenharia e Construção (AEC)**. O objetivo é reunir recursos que ajudem profissionais do setor a integrar inteligência artificial nos seus fluxos de trabalho — desde modelagem BIM até gestão de obras.

O [MCP](https://modelcontextprotocol.io/) é um protocolo aberto que permite que modelos de IA interajam de forma segura com recursos locais e remotos por meio de servidores padronizados.

> **Contribua!** Este repositório é colaborativo. Se você conhece algum MCP Server, Skill ou ferramenta de IA relevante para AEC que não está listada, abra uma [issue](../../issues) ou envie um [pull request](../../pulls). Consulte o [CONTRIBUTING.md](CONTRIBUTING.md) para saber como contribuir.

🇺🇸 [English Version](README.md)

---

## Aviso de Segurança

> **Atenção:** Servidores MCP executam código na sua máquina com as mesmas permissões do processo hospedeiro. Sempre revise o código antes de instalar, execute em ambientes isolados quando possível e limite as permissões ao mínimo necessário.

---

## Sumário

- [Clientes MCP Compatíveis](#clientes-mcp-compatíveis)
- [MCP Servers](#mcp-servers)
  - [BIM & Modelagem 3D](#-bim--modelagem-3d)
  - [IFC & openBIM](#-ifc--openbim)
  - [Design Paramétrico](#-design-paramétrico)
  - [Engenharia Estrutural & FEA](#-engenharia-estrutural--fea)
  - [Simulação Energética & Sustentabilidade](#-simulação-energética--sustentabilidade)
  - [Engenharia Civil & Infraestrutura](#-engenharia-civil--infraestrutura)
  - [Geoespacial & GIS](#-geoespacial--gis)
  - [Colaboração & Plataformas BIM](#-colaboração--plataformas-bim)
  - [Gestão de Obras & Custos](#-gestão-de-obras--custos)
  - [Documentação & Arquivos](#-documentação--arquivos)
  - [Bancos de Dados](#-bancos-de-dados)
  - [Busca & Web](#-busca--web)
  - [Visualização de Dados](#-visualização-de-dados)
  - [Ferramentas de Desenvolvimento](#-ferramentas-de-desenvolvimento)
- [Skills & Rules para AEC](#skills--rules-para-aec)
- [Aplicações de IA para AEC](#aplicações-de-ia-para-aec)
  - [Estimativa de Custos](#-estimativa-de-custos)
  - [Gestão de Projetos & Planejamento](#-gestão-de-projetos--planejamento)
  - [Monitoramento de Obras & LiDAR](#-monitoramento-de-obras--lidar)
  - [Design Generativo & Assistentes](#-design-generativo--assistentes)
- [Recursos Educacionais](#recursos-educacionais)
- [Como Contribuir](#como-contribuir)

---

## Clientes MCP Compatíveis

Os MCP Servers listados aqui podem ser utilizados com diversos clientes compatíveis:

| Cliente | Documentação |
|---------|-------------|
| [Claude Desktop](https://claude.ai) | [Claude x MCP](https://modelcontextprotocol.io/quickstart) |
| [Cursor](https://www.cursor.com/) | [Cursor x MCP](https://docs.cursor.com/advanced/model-context-protocol) |
| [VS Code](https://code.visualstudio.com/) | [VS Code x MCP](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) |
| [Zed Editor](https://zed.dev/) | [Zed x MCP](https://zed.dev/blog/mcp) |
| [Continue](https://www.continue.dev/) | [Continue x MCP](https://blog.continue.dev/model-context-protocol) |
| [Goose](https://block.github.io/goose/) | [Goose x MCP](https://block.github.io/goose/docs/getting-started/using-extensions) |

---

## MCP Servers

### 🏗️ BIM & Modelagem 3D

> Servidores que permitem interação direta com ferramentas BIM como Revit e Tekla via linguagem natural.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [RevitMCPBridge2026](https://github.com/WeberG619/RevitMCPBridge2026) | 705+ endpoints MCP para controle completo do Revit 2026 via named pipes. Criação de paredes, portas, vistas, documentação e verificação de conformidade. | Python / C# |
| [Revit 2026 MCP Server](https://github.com/antonhofstader/Revit-2026-MCP-Server) | Servidor MCP para Revit 2026 com add-in C# e comunicação via JSON-RPC. Consulta de elementos, modificação de parâmetros e criação de vistas. | Python / C# |
| [Revit MCP (mcp-servers-for-revit)](https://github.com/mcp-servers-for-revit) | Organização com múltiplas implementações MCP para Revit (TypeScript e Python). 363+ stars. | TS / Python |
| [APS AECDM MCP](https://github.com/autodesk-platform-services/aps-aecdm-mcp-dotnet) | Servidor MCP .NET conectando Claude Desktop com a AEC Data Model API. Consulta de dados de design, filtro de elementos por categoria e renderização no Viewer. | C# / .NET |
| [APS Revit MCP Tools Bundle](https://github.com/autodesk-platform-services/aps-sample-revit-mcp-tools-bundle) | AppBundle para Automation API do Revit 2026. Execução de ferramentas customizadas em Revit Cloud Models via MCP. | Python |
| [APS MCP Server (Python)](https://github.com/autodesk-platform-services/aps-mcp-server-python) | Servidor MCP para Autodesk Platform Services com diferentes abordagens de autenticação. | Python |
| [Autodesk MCP Servers](https://www.autodesk.com/solutions/autodesk-ai/autodesk-mcp-servers) ⭐ | Servidores MCP oficiais da Autodesk para Revit, AutoCAD, Inventor e Navisworks. | - |
| [TeklaMCPServer](https://github.com/YuriyKirillov/TeklaMCPServer) | Servidor MCP para Tekla Structures. Inserção/remoção de componentes, seleção de elementos, gestão de propriedades e operações geométricas. | Python |

### 📐 IFC & openBIM

> Interação com arquivos IFC (Industry Foundation Classes) para workflows openBIM.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [ifcMCP](https://github.com/smartaec/ifcmcp) | Servidor MCP para interação com arquivos IFC. Recuperação de entidades, consulta de propriedades, análise espacial e detecção de aberturas em paredes. | Python |
| [IfcOpenShell](https://ifcopenshell.org/) | Biblioteca open-source para leitura/escrita de arquivos IFC. Base para muitos servidores MCP do setor. | Python / C++ |

### 🎨 Design Paramétrico

> Servidores MCP para integração com Rhino e Grasshopper, habilitando design paramétrico assistido por IA.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [Cordyceps](https://github.com/brookstalley/cordyceps) | Servidor MCP para Rhino 8.21+ com controle completo do Grasshopper (componentes, conexões, grupos) e integração Rhino (bake, layers, renderização). | C# |
| [GH_mcp_server](https://github.com/veoery/gh_mcp_server) | Interação direta de LLMs com Rhino/Grasshopper. Análise de .3dm, modelagem 3D e geração automática de código GHPython. | Python |
| [Grasshopper MCP (dongwoosuk)](https://playbooks.com/mcp/dongwoosuk/grasshopper-mcp) | Integração Rhino/Grasshopper com mentoring por IA, otimização de layout com ML e execução de Python no Rhino. | Python |
| [AI-architecture](https://github.com/Xiaohu1009/AI-architecture) | Integração unificada Rhino + Grasshopper com roteamento inteligente, criação de objetos, operações paramétricas e reconhecimento de padrões. | Python |

### 🔩 Engenharia Estrutural & FEA

> Análise por Elementos Finitos e ferramentas de engenharia estrutural acessíveis via MCP.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [FEA-MCP](https://github.com/greatapo/fea-mcp) | Servidor MCP para Análise por Elementos Finitos. API unificada para softwares FEA (suporte a ETABS e LUSAS). Modelagem geométrica, análise e pós-processamento. | Python |

### ♻️ Simulação Energética & Sustentabilidade

> Ferramentas para simulação de desempenho energético de edificações.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [EnergyPlus-MCP](https://www.osti.gov/pages/biblio/3015372) | Primeiro servidor MCP open-source para EnergyPlus. 35 ferramentas especializadas para gestão de modelos, edição, configuração HVAC e execução de simulações. | Python |
| [idfkit-mcp](https://github.com/idfkit/idfkit-mcp/) | Servidor MCP para simulação energética EnergyPlus. Instalação via pip/uv, suporte a múltiplos clientes (Claude, Cursor, VS Code). | Python |
| [OpenStudio MCP](https://github.com/NatLabRockies/openstudio-mcp) | 22 skills, 126 ferramentas MCP para simulação energética OpenStudio. Criação, modificação e simulação de modelos energéticos via linguagem natural. Docker support. 450+ testes. | Python |

### 🚧 Engenharia Civil & Infraestrutura

> Cálculos e ferramentas para engenharia civil, hidrologia e infraestrutura.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [Civil Engineering Tools Server](https://ubos.tech/mcp/mcp-civil-tools/overview/) | Cálculos especializados: conversão de coordenadas, curvas IDF, infiltração, estabilidade de taludes, muros de arrimo, escoamento e drenagem. | Python |

### 🌍 Geoespacial & GIS

> Integração com ferramentas GIS e serviços de geolocalização.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [QGIS MCP](https://github.com/jjsantos01/qgis_mcp) | Integração QGIS com IA. Manipulação de projetos/camadas, execução de algoritmos de processamento e código PyQGIS. 866+ stars. | Python |
| [ArcGIS Pro Bridge](https://market-mcp.com/mcp/arcgis-pro-bridge) | Framework MCP conectando ArcGIS Pro a agentes IA. Consulta de mapas e automação de geoprocessamento via linguagem natural. | C# / .NET |
| [Mapbox MCP Server](https://github.com/mapbox/mcp-server) | Geocodificação, busca de POIs, roteamento multi-modal, matrizes de tempo de viagem, otimização de rotas e isócronas. | TypeScript |

### 🤝 Colaboração & Plataformas BIM

> Plataformas de colaboração e compartilhamento de dados BIM.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [Speckle MCP](https://github.com/bimgeek/speckle-mcp) | Servidor MCP para Speckle — o hub colaborativo de dados AEC. Listagem de projetos, versões de modelos, consulta de objetos e propriedades. | Python |
| [Trimble Connect](https://developer.tekla.com/trimble-connect) | Plataforma de colaboração na nuvem com APIs para integração, sincronização de dados e suporte a BCF 3.0. | - |

### 💰 Gestão de Obras & Custos

> Ferramentas de IA para estimativas, planejamento e gestão de projetos de construção.

| Projeto | Descrição | Tipo |
|---------|-----------|------|
| [Planaut](https://planaut.ai/) | Co-piloto IA para gestão de obras. Processa documentos (2000+ páginas), extrai escopo com CSI MasterFormat, gera cronogramas CPM e estimativas de custo. | SaaS |
| [BuildEngine](https://buildengine.ai/) | Gera estimativas de construção em 6 minutos (40x mais rápido). Simula processo construtivo completo, identifica escopos faltantes. | SaaS |
| [BuildX Protocol](https://buildx.pro/) | 2.182 calculadoras de custos, IA para perguntas sobre custos de construção e marketplace de subempreiteiros. | SaaS |
| [BEXEL Manager](https://bexelmanager.com/cost-estimator) | Gestão de custos 5D BIM. Simulações 4D+5D, quantitativos, análise de custos, fluxo de caixa e analytics com IA. | Software |

### 📄 Documentação & Arquivos

> Ferramentas para processar documentos técnicos, contratos e especificações.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [Fetch MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) | Busca e processamento eficiente de conteúdo web para consumo por IA. | Python |
| [FileSystem MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | Acesso direto ao sistema de arquivos local com permissões configuráveis. | TypeScript |

### 🗄️ Bancos de Dados

> Acesso a bancos de dados para armazenamento e consulta de dados de projeto.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [PostgreSQL MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) | Integração com PostgreSQL — inspeção de schema e execução de queries. | TypeScript |
| [SQLite MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) | Operações SQLite com recursos de análise integrados. | Python |
| [DuckDB MCP](https://github.com/modelcontextprotocol/servers) | Integração DuckDB para análise de dados local de alta performance. | Python |

### 🔍 Busca & Web

> Busca na web e automação de navegador para pesquisas técnicas.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [Brave Search MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) | Busca web via API do Brave Search. | TypeScript |
| [Puppeteer MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) | Automação de navegador para scraping e interação web. | TypeScript |
| [Playwright MCP](https://github.com/executeautomation/mcp-playwright) | Automação de navegador via Playwright para testes e scraping. | TypeScript |
| [ArXiv MCP](https://github.com/modelcontextprotocol/servers) | Busca de artigos científicos no ArXiv — útil para pesquisa técnica. | Python |

### 📊 Visualização de Dados

> Geração de gráficos e visualizações para análise de dados de projeto.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [ECharts MCP](https://github.com/modelcontextprotocol/servers) | Geração dinâmica de gráficos com Apache ECharts via IA. | TypeScript |
| [Mermaid MCP](https://github.com/modelcontextprotocol/servers) | Geração de diagramas e fluxogramas com Mermaid via IA. | TypeScript |
| [VegaLite MCP](https://github.com/modelcontextprotocol/servers) | Visualizações com VegaLite a partir de dados processados. | TypeScript |

### 🛠️ Ferramentas de Desenvolvimento

> Ferramentas gerais de desenvolvimento que auxiliam no workflow AEC.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [GitHub MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/github) | Integração com GitHub API — gestão de repos, PRs, issues. | TypeScript |
| [Git MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/git) | Operações Git diretas para repositórios locais. | TypeScript |
| [Docker MCP](https://github.com/modelcontextprotocol/servers) | Operações Docker para containers e stacks compose. | TypeScript |

---

## Skills & Rules para AEC

> Skills e Rules são instruções persistentes que personalizam o comportamento de assistentes IA em IDEs como Cursor, VS Code e outros. Abaixo estão recursos relevantes para o setor AEC.

### O que são?

- **Rules** (`.cursor/rules/`): Instruções sempre ativas que definem padrões de código, stack tecnológica e convenções do projeto.
- **Skills** (`SKILL.md`): Instruções procedurais sob demanda — "como fazer" que os agentes aplicam quando a tarefa é relevante.
- **AGENTS.md**: Arquivo alternativo na raiz do projeto para orientar agentes de IA.

### Coleções & Frameworks

| Recurso | Descrição | Link |
|---------|-----------|------|
| [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | A maior lista curada de arquivos `.cursorrules`. 38.700+ stars. Organizada por framework e linguagem. | [GitHub](https://github.com/PatrickJS/awesome-cursorrules) |
| [cursor-rules-and-prompts](https://github.com/thehimel/cursor-rules-and-prompts) | Coleção abrangente de rules e prompts para padrões de código. | [GitHub](https://github.com/thehimel/cursor-rules-and-prompts) |
| [cursorskills](https://github.com/bluriesophos/cursorskills) | Arquivos SKILL.md reutilizáveis — planejamento, code review, debugging e gestão de dados. | [GitHub](https://github.com/bluriesophos/cursorskills) |
| [cursor-anthropic-skills](https://github.com/SteelMorgan/cursor-anthropic-skills) | Skills otimizadas para Anthropic em workflows de agentes estruturados. | [GitHub](https://github.com/SteelMorgan/cursor-anthropic-skills) |

### Recursos Específicos para AEC

| Recurso | Descrição | Link |
|---------|-----------|------|
| [cad2data-Revit-IFC-DWG-DGN](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN) | Workflows automatizados de conversão CAD/BIM. Processamento em lote, validação, relatórios QTO, estimativa de custos e análise de pegada de carbono. Sem necessidade de licença Autodesk. 284+ stars. | [GitHub](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN) |
| [Debugging Revit Plugins com Cursor](https://aps.autodesk.com/blog/debugging-revit-plugins-cursor-modern-developer-workflow) | Guia oficial da Autodesk sobre debugging de add-ins C# Revit usando Cursor IDE com setup de debugging pré-configurado. | [Blog](https://aps.autodesk.com/blog/debugging-revit-plugins-cursor-modern-developer-workflow) |
| [cursor-custom-agents-rules-generator](https://github.com/bmadcode/cursor-custom-agents-rules-generator) | Framework para geração automática de rules e agentes customizados. Útil como base para criar rules específicas de AEC. | [GitHub](https://github.com/bmadcode/cursor-custom-agents-rules-generator) |

### Skills & Rules da Comunidade (Aberto para Contribuição)

Estamos construindo uma coleção de Skills e Rules específicas para AEC. Tópicos que buscamos:

- **Revit API** — Convenções de codificação para plugins C#/Python Revit (transações, FilteredElementCollector, parâmetros)
- **Dynamo / Python** — Padrões para scripts Dynamo em projetos BIM
- **IFC Processing** — Convenções para parsers e validadores baseados em IfcOpenShell
- **Civil 3D API** — Padrões para desenvolvimento com Civil 3D .NET API
- **Grasshopper / RhinoCommon** — Regras para desenvolvimento de componentes Grasshopper e scripts RhinoCommon
- **Documentação Técnica** — Regras para geração automatizada de documentos técnicos e relatórios

> **Quer contribuir?** Veja o [CONTRIBUTING.md](CONTRIBUTING.md) para o template e diretrizes.

---

## Aplicações de IA para AEC

> Ferramentas e plataformas de IA (não necessariamente MCP) que trazem ganhos significativos para profissionais AEC.

### 💵 Estimativa de Custos

| Ferramenta | Descrição |
|------------|-----------|
| [Planaut](https://planaut.ai/) | IA para extração de escopo, cronogramas CPM e estimativas a partir de documentos. |
| [BuildEngine](https://buildengine.ai/) | Estimativas em 6 minutos simulando o processo construtivo. |
| [BuildX Protocol](https://buildx.pro/) | 2.182 calculadoras de custos com IA para construção nos EUA. |
| [BEXEL Manager](https://bexelmanager.com/) | Gestão 5D BIM com simulações 4D+5D e IA. |

### 📋 Gestão de Projetos & Planejamento

| Ferramenta | Descrição |
|------------|-----------|
| [Tekla 2026](https://www.tekla.com/) | Assistente IA para modelagem e desenhos de fabricação com linguagem natural. |
| [Trimble Connect](https://connect.trimble.com/) | Plataforma cloud de colaboração com BCF 3.0 e sincronização em tempo real. |
| [Speckle](https://speckle.systems/) | "Git para BIM" — colaboração open-source e interoperabilidade entre ferramentas AEC. |

### 📡 Monitoramento de Obras & LiDAR

| Ferramenta | Descrição |
|------------|-----------|
| [viLid (viact.ai)](https://www.viact.ai/vilid) | Monitoramento LiDAR 4D com IA para tracking de progresso e detecção de desvios. |
| [Carlson Point Cloud 2026](https://carlsonps.com/products/carlsonpointcloud) | Processamento de nuvens de pontos de LiDAR, fotogrametria e drones. |

### 🎨 Design Generativo & Assistentes

| Ferramenta | Descrição |
|------------|-----------|
| [OpenPencil](https://github.com/open-pencil/open-pencil) | Editor de design open-source com 90+ ferramentas IA, servidor MCP e export Tailwind CSS. |

---

## Recursos Educacionais

| Recurso | Descrição |
|---------|-----------|
| [Awesome-AECO](https://github.com/osama-ata/Awesome-AECO) | Lista curada de ferramentas open-source para o ambiente construído (BIM, CAD, simulação, digital twins). |
| [MCP Protocol Docs](https://modelcontextprotocol.io/) | Documentação oficial do Model Context Protocol. |
| [Modular Reference Architecture for MCP-Servers (Paper)](https://ui.adsabs.harvard.edu/abs/2026arXiv260100809H/abstract) | Paper acadêmico propondo arquitetura modular de referência para servidores MCP em interações BIM agentic. |
| [MCP Servers in Construction (Autodesk Blog)](https://www.autodesk.com/blogs/construction/mcp-servers-in-construction/) | Post do blog da Autodesk explicando MCP servers no contexto da construção. |
| [AI Agents & MCP para Engenheiros (VIKTOR)](https://www.viktor.ai/blog/196/how-engineers-can-use-ai-agents-and-mcp-servers-to-work-smarter) | Guia prático sobre como engenheiros podem usar agentes de IA e servidores MCP no dia a dia. |
| [Cursor Rules Guide](https://skillsplayground.com/guides/cursor-rules/) | Guia completo sobre Rules e Skills no Cursor IDE. |

---

## Como Contribuir

Contribuições são muito bem-vindas! Consulte o [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre como adicionar novos recursos à lista.

Formas de contribuir:
- Adicionar novos MCP Servers voltados para AEC
- Compartilhar Skills & Rules para desenvolvimento AEC
- Sugerir aplicações de IA relevantes para o setor
- Corrigir informações desatualizadas
- Melhorar descrições e categorização

---

## Legenda

| Símbolo | Significado |
|---------|-------------|
| ⭐ | Implementação oficial |
| 🆕 | Adicionado recentemente |
| 🔧 | Em desenvolvimento ativo |
| 📖 | Bem documentado |

---

## Licença

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

Na medida do possível sob a lei, os autores renunciaram a todos os direitos autorais e direitos conexos ou vizinhos a este trabalho.
