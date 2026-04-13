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
  - [Fotogrametria & Escaneamento](#-fotogrametria--escaneamento)
  - [IoT & Digital Twins](#-iot--digital-twins)
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
| [APS Revit Automation MCP](https://github.com/autodesk-platform-services/aps-sample-mcp-server-revit-automation) | Servidor MCP cloud-native para automação headless do Revit via Automation API. Funciona com ACC/BIM360 Cloud Models — sem Revit local. | C# / .NET |
| [AutoCAD MCP (PeterPerez01)](https://github.com/PeterPerez01/autocad-mcp) | Servidor MCP para AutoCAD via Windows COM. Criação inteligente (paredes, portas, janelas, salas, mobília), geometria, gestão de layers e inspeção de entidades. | Python |
| [Blender MCP](https://github.com/ahujasid/blender-mcp) | Servidor MCP para Blender com manipulação de objetos, materiais, geometry nodes, assets Poly Haven, Hunyuan3D e geração de modelos Hyper3D Rodin. 18.300+ stars. | Python |
| [FreeCAD MCP (ContextForm)](https://github.com/contextform/freecad-mcp) | Controle do FreeCAD via IA — criação de sketches, operações 3D (extrusão, revolução, loft), design paramétrico e gestão de arquivos multi-formato. 65+ stars. | Python |
| [FreeCAD Robust MCP](https://github.com/spkane/freecad-robust-mcp-and-more) | Servidor MCP robusto para FreeCAD com XML-RPC/JSON-RPC, modo headless, suporte Docker e ferramentas de gestão de documentos. 55+ stars. | Python |
| [OpenSCAD MCP Server](https://github.com/jhacksman/OpenSCAD-MCP-Server) | Linguagem natural para modelos 3D paramétricos. Geração multi-view, IA de imagem (Gemini/Venice.ai), exportação multi-formato e integração com impressora 3D. 139+ stars. | Python |
| [That Open Engine (components)](https://github.com/ThatOpen/engine_components) | Toolkit BIM open-source — viewer, fragments, gestão de propriedades, indexação espacial e mais. Construa apps BIM web completos com Three.js. 624+ stars. | TypeScript |
| [That Open Engine (clay)](https://github.com/ThatOpen/engine_clay) | Engine BIM leve e open-source para criação e edição de geometria 3D BIM de forma programática. | TypeScript |
| [That Open Engine (fragments)](https://github.com/ThatOpen/engine_fragment) | Engine de geometria 3D de alta performance otimizada para carregar e renderizar grandes modelos BIM no navegador. 174+ stars. | TypeScript |

### 📐 IFC & openBIM

> Interação com arquivos IFC (Industry Foundation Classes) para workflows openBIM.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [ifcMCP](https://github.com/smartaec/ifcmcp) | Servidor MCP para interação com arquivos IFC. Recuperação de entidades, consulta de propriedades, análise espacial e detecção de aberturas em paredes. | Python |
| [IfcOpenShell](https://ifcopenshell.org/) | Biblioteca open-source para leitura/escrita de arquivos IFC. Base para muitos servidores MCP do setor. | Python / C++ |
| [MCP4IFC](https://github.com/Show2Instruct/ifc-bonsai-mcp) | Framework open-source que permite LLMs criar e modificar dados IFC de edifícios via MCP. Integra com Blender/Bonsai e IfcOpenShell. Geração de código com RAG. | Python |
| [That Open Engine (web-ifc)](https://github.com/ThatOpen/engine_web-ifc) | Leitura e escrita de arquivos IFC com JavaScript em velocidade nativa. Parser baseado em WebAssembly para navegador e Node.js. 933+ stars. | TypeScript |
| [web-ifc-three](https://github.com/ThatOpen/web-ifc-three) | Loader IFC oficial para Three.js. Permite renderizar modelos IFC diretamente em visualizadores 3D web. 582+ stars. | JavaScript |

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
| [StructureClaw](https://github.com/structureclaw/structureclaw) | Workspace de engenharia estrutural assistido por IA. Workflow conversacional de linguagem natural até artefatos de análise com ciclo de rascunho, validação, análise e verificação de código. 35+ stars. | TypeScript / Python |
| [Talk with Your ETABS Model (VIKTOR)](https://github.com/viktor-platform/talk-with-your-model) | Agente IA para modelos estruturais ETABS. Consulta de resultados, criação de heat maps, plotagem de deformadas e dimensionamento de fundações via linguagem natural. | Python |

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
| [Civil3D MCP](https://github.com/Sacred-G/Civil3D-mcp) | Servidor MCP para Autodesk Civil 3D. Criação, modificação e consulta de elementos de projeto civil — pontos, alinhamentos, perfis, superfícies e segmentos de linha. | C# / TypeScript |

### 🌍 Geoespacial & GIS

> Integração com ferramentas GIS e serviços de geolocalização.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [QGIS MCP](https://github.com/jjsantos01/qgis_mcp) | Integração QGIS com IA. Manipulação de projetos/camadas, execução de algoritmos de processamento e código PyQGIS. 866+ stars. | Python |
| [ArcGIS Pro Bridge](https://market-mcp.com/mcp/arcgis-pro-bridge) | Framework MCP conectando ArcGIS Pro a agentes IA. Consulta de mapas e automação de geoprocessamento via linguagem natural. | C# / .NET |
| [Mapbox MCP Server](https://github.com/mapbox/mcp-server) | Geocodificação, busca de POIs, roteamento multi-modal, matrizes de tempo de viagem, otimização de rotas e isócronas. | TypeScript |
| [gis-mcp](https://github.com/mahdin75/gis-mcp) | 100+ ferramentas geoespaciais usando Shapely, GeoPandas, PyProj e Rasterio. Buffer, interseção, Voronoi, transformações e I/O vetorial. 126+ stars. | Python |
| [Overture Maps MCP](https://github.com/srivinod1/overture-mcp-server) | Analytics espaciais sobre dados Overture Maps — Places, Buildings, Transportation, Divisions e Land Use. DuckDB + GeoParquet, sem credenciais. | Python |
| [Axion Planetary MCP](https://github.com/Dhenenjay/axion-planetary-mcp) | Integração Google Earth Engine via MCP. 30+ datasets de satélite (Landsat, Sentinel, MODIS), NDVI/NDWI, risco de incêndio, modelagem de inundações e detecção de desmatamento. 217+ stars. | Python |
| [geeViz MCP](https://geeviz.org/mcp_server.html) | Toolkit Python para Google Earth Engine com 34 ferramentas MCP. Execute código e inspecione assets GEE ao vivo via assistentes IA. | Python |

### 🤝 Colaboração & Plataformas BIM

> Plataformas de colaboração e compartilhamento de dados BIM.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [Speckle MCP](https://github.com/bimgeek/speckle-mcp) | Servidor MCP para Speckle — o hub colaborativo de dados AEC. Listagem de projetos, versões de modelos, consulta de objetos e propriedades. | Python |
| [Trimble Connect](https://developer.tekla.com/trimble-connect) | Plataforma de colaboração na nuvem com APIs para integração, sincronização de dados e suporte a BCF 3.0. | - |
| [Procore MCP Server](https://github.com/zeniasupp0rt-cmyk/procore-mcp-server) | Servidor MCP para gestão de obras Procore. Projetos, RFIs, submittals, documentos e orçamento acessíveis via assistentes IA. Autenticação OAuth2. | TypeScript |

### 💰 Gestão de Obras & Custos

> Ferramentas de IA para estimativas, planejamento e gestão de projetos de construção.

| Projeto | Descrição | Tipo |
|---------|-----------|------|
| [Planaut](https://planaut.ai/) | Co-piloto IA para gestão de obras. Processa documentos (2000+ páginas), extrai escopo com CSI MasterFormat, gera cronogramas CPM e estimativas de custo. | SaaS |
| [BuildEngine](https://buildengine.ai/) | Gera estimativas de construção em 6 minutos (40x mais rápido). Simula processo construtivo completo, identifica escopos faltantes. | SaaS |
| [BuildX Protocol](https://buildx.pro/) | 2.182 calculadoras de custos, IA para perguntas sobre custos de construção e marketplace de subempreiteiros. | SaaS |
| [BEXEL Manager](https://bexelmanager.com/cost-estimator) | Gestão de custos 5D BIM. Simulações 4D+5D, quantitativos, análise de custos, fluxo de caixa e analytics com IA. | Software |
| [OpenConstructionERP](https://github.com/datadrivenconstruction/OpenConstructionERP) | Plataforma open-source de estimativa para construção. Takeoff com IA (16 provedores de LLM), 55K+ itens de custo, 21 idiomas, planejamento 4D/5D, viewer BIM. AGPL-3.0. | Open Source |
| [Bidwright](https://github.com/braedonsaunders/bidwright) | Plataforma de estimativa de construção AI-native. Intake de licitações, takeoff de desenhos com anotações, precificação, cronograma, geração de PDF de propostas e servidor MCP. MIT. | Open Source |

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

### 📷 Fotogrametria & Escaneamento

> Ferramentas para pipelines de fotogrametria, levantamentos com drones e reconstrução 3D.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [Metashape MCP](https://github.com/jenkinsm13/metashape-mcp) | Servidor MCP com IA para Agisoft Metashape Professional 2.3+. 106 ferramentas em 15 módulos — pipeline completo de fotogrametria, de alinhamento a exportação de ortomosaico. Modo headless para CI. | Python |

### 🏠 IoT & Digital Twins

> Plataformas de edifícios inteligentes conectando sensores IoT, digital twins e analytics com IA.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [CONTEXUS](https://github.com/contexusio/contexus) | Framework open-source modular para edifícios inteligentes. 13+ módulos, conectividade IoT (LoRaWAN, MQTT, BACnet, Modbus), digital twin 3D BIM com sobreposição de sensores em tempo real e manutenção preditiva com IA. MIT. | TypeScript / Shell |
| [Digital Twin MCP](https://github.com/aisystant/digital-twin-mcp) | Servidor MCP de digital twin baseado em metamodelo com 65+ indicadores hierárquicos, controle de acesso e deploy via Cloudflare Workers. | TypeScript |

### 🛠️ Ferramentas de Desenvolvimento

> Ferramentas gerais de desenvolvimento que auxiliam no workflow AEC.

| Projeto | Descrição | Linguagem |
|---------|-----------|-----------|
| [GitHub MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/github) | Integração com GitHub API — gestão de repos, PRs, issues. | TypeScript |
| [Git MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/git) | Operações Git diretas para repositórios locais. | TypeScript |
| [Docker MCP](https://github.com/modelcontextprotocol/servers) | Operações Docker para containers e stacks compose. | TypeScript |
| [That Open Engine (UI Components)](https://github.com/ThatOpen/engine_ui-components) | Coleção de web components para interfaces de aplicações BIM — painéis, árvores, tabelas de propriedades e mais. | TypeScript |
| [That Open Engine (Templates)](https://github.com/ThatOpen/engine_templates) | Templates iniciais para criar rapidamente aplicações BIM web com That Open Engine. | TypeScript |

---

## Skills & Rules para AEC

> Skills e Rules são instruções persistentes que personalizam o comportamento de assistentes IA em IDEs como Cursor, VS Code e outros. Abaixo estão recursos curados para profissionais AEC — de skills de disciplina de workflow a regras de codificação por linguagem.

### O que são?

- **Rules** (`.cursor/rules/`): Instruções sempre ativas que definem padrões de código, stack tecnológica e convenções do projeto.
- **Skills** (`SKILL.md`): Instruções procedurais sob demanda — "como fazer" que os agentes aplicam quando a tarefa é relevante.
- **AGENTS.md**: Arquivo alternativo na raiz do projeto para orientar agentes de IA.

### Recursos Específicos para AEC

| Recurso | Descrição | Link |
|---------|-----------|------|
| [cad2data-Revit-IFC-DWG-DGN](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN) | Workflows automatizados de conversão CAD/BIM com integração de agentes IA. Processamento em lote, validação, relatórios QTO, estimativa de custos e análise de pegada de carbono. Sem licença Autodesk. 284+ stars. | [GitHub](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN) |
| [Debugging Revit Plugins com Cursor](https://aps.autodesk.com/blog/debugging-revit-plugins-cursor-modern-developer-workflow) | Guia oficial da Autodesk sobre debugging de add-ins C# Revit usando Cursor IDE com setup pré-configurado. | [Blog](https://aps.autodesk.com/blog/debugging-revit-plugins-cursor-modern-developer-workflow) |

### Skills de Workflow & Disciplina

> De [cursorskills](https://github.com/bluriesophos/cursorskills) — skills orientadas a processo que trazem estrutura ao desenvolvimento AEC. Instale copiando a pasta da skill para `~/.cursor/skills/` (pessoal) ou `.cursor/skills/` (projeto).

| Skill | O que faz | Por que importa para AEC |
|-------|----------|-------------------------|
| [battle-plan](https://github.com/bluriesophos/cursorskills/tree/main/battle-plan) | Ritual completo de planejamento antes de tarefas significativas — escopo, avaliação de risco, estimativa, confirmação. | Automação BIM e desenvolvimento de plugins exigem planejamento prévio. |
| [pre-mortem](https://github.com/bluriesophos/cursorskills/tree/main/pre-mortem) | Imagina cenários de falha e reordena o plano de implementação para abordar itens de alto risco primeiro. | Previne erros custosos em transações Revit, processamento IFC e scripts de análise estrutural. |
| [split-decision](https://github.com/bluriesophos/cursorskills/tree/main/split-decision) | Apresenta 2-4 opções como tabela comparativa com trade-offs antes de decidir. | Escolha entre APIs BIM, formatos de dados (IFC vs RVT) ou abordagens de simulação. |
| [code-review](https://github.com/bluriesophos/cursorskills/tree/main/code-review) | Revisão estruturada contra 14 critérios de qualidade (design, segurança, performance, testes). | Essencial para revisar add-ins Revit e componentes Grasshopper antes do deploy. |
| [debug-to-fix](https://github.com/bluriesophos/cursorskills/tree/main/debug-to-fix) | Ciclo completo de debug: esclarecer, investigar, corrigir, verificar. | Debugging de issues na API Revit, data trees do Grasshopper e erros de parsing IFC. |
| [prove-it](https://github.com/bluriesophos/cursorskills/tree/main/prove-it) | Verifica resultados antes de declarar tarefas completas. | Garante que scripts BIM produzem geometria/dados corretos antes da aprovação. |
| [safe-refactor](https://github.com/bluriesophos/cursorskills/tree/main/safe-refactor) | Ciclo de refatoração com avaliação de risco, preparação, implementação e verificação. | Refatoração segura de plugins Revit grandes ou bibliotecas BIM compartilhadas. |
| [trace-it](https://github.com/bluriesophos/cursorskills/tree/main/trace-it) | Rastreia todos os chamadores antes de modificar código compartilhado. | Previne "corrigi uma coisa, quebrei três" em bibliotecas BIM compartilhadas. |
| [breadcrumbs](https://github.com/bluriesophos/cursorskills/tree/main/breadcrumbs) | Deixa notas para sessões futuras em `.cursor/breadcrumbs.md`. | Projetos longos de automação BIM se beneficiam da memória entre sessões. |
| [pair-mode](https://github.com/bluriesophos/cursorskills/tree/main/pair-mode) | Transforma o agente em parceiro de pair programming que explica o raciocínio. | Aprender Revit API, IfcOpenShell ou scripting Grasshopper com assistência guiada. |
| [you-sure](https://github.com/bluriesophos/cursorskills/tree/main/you-sure) | Pausa antes de ações destrutivas/irreversíveis com checklist de impacto. | Previne corrupção acidental de modelos em transações Revit ou operações em banco de dados. |

### Skills Específicas por Domínio

> De [cursor-anthropic-skills](https://github.com/SteelMorgan/cursor-anthropic-skills) — 70+ skills especializadas cobrindo desenvolvimento, dados, MCP e mais. Abaixo estão as mais relevantes para workflows AEC.

**Processamento de Documentos & Dados**

| Skill | Descrição | Caso de Uso AEC |
|-------|-----------|----------------|
| [Document Processing (PDF)](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Criar, mesclar, extrair de PDFs. Formulários preenchíveis. | Especificações técnicas, docs de obra, RFIs |
| [Document Processing (Excel)](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Criação de planilhas, análise de dados, gráficos, fórmulas. | BOQs, estimativas de custo, quantitativos |
| [Document Processing (DOCX)](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Criação de documentos Word e geração de relatórios. | Relatórios de projeto, atas de reunião, RFPs |
| [Document Processing (PPTX)](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Criação de apresentações e slides. | Apresentações para clientes, revisões de design |
| [Visual OCR](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Extração de texto de imagens via OCR. | Extrair texto de desenhos e plantas escaneadas |
| [Document Structure Analysis](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Análise de layouts e estrutura de documentos. | Parsing de especificações técnicas e contratos |

**Desenvolvimento MCP**

| Skill | Descrição | Caso de Uso AEC |
|-------|-----------|----------------|
| [MCP Server Architecture](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Design e implementação de servidores MCP. | Construir MCP servers customizados para AEC |
| [MCP Integration](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Orquestração multi-servidor e workflows. | Conectar Revit + IFC + GIS MCP servers |
| [MCP Protocol](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Especificação e conformidade do protocolo MCP. | Garantir conformidade MCP para ferramentas BIM |
| [MCP Testing](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Testes de implementações de servidores MCP. | QA para MCP servers AEC |

**Dados & IA**

| Skill | Descrição | Caso de Uso AEC |
|-------|-----------|----------------|
| [Data Engineering](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Pipelines ETL/ELT, data warehouses, infraestrutura. | Pipelines de dados BIM, ETL IFC-para-banco |
| [Data Science](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Modelagem estatística, análise preditiva, análise exploratória. | Análise de dados de construção, predição de tendências |
| [Computer Vision](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Processamento de imagem, reconhecimento e análise. | Monitoramento de obra, tracking de progresso por fotos |
| [3D Art](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Assets 3D, modelagem e otimização. | Visualização 3D para modelos arquitetônicos |

**Desenvolvimento & DevOps**

| Skill | Descrição | Caso de Uso AEC |
|-------|-----------|----------------|
| [Debugging](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Debugging estruturado e análise de causa raiz. | Debugging de add-ins Revit e scripts Grasshopper |
| [Code Review](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Revisão estruturada de qualidade de código. | Revisão de código de plugins BIM |
| [Docker Operations](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Gestão de containers, compose, health checks. | Processamento BIM containerizado, deploy de MCP servers |
| [PowerShell](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Scripting e automação Windows. | Automação Windows para ferramentas AEC (maioria roda em Windows) |
| [Mermaid Diagrams](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Fluxogramas, diagramas de sequência, ERDs, Gantt. | Fluxos de processo, timelines de projeto, diagramas de arquitetura |
| [Technical Writing](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Guias do usuário, tutoriais, documentação técnica. | Documentação de plugins, guias de API |
| [API Documentation](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | OpenAPI specs, geração de SDK, docs para desenvolvedores. | Documentar APIs BIM e MCP servers |
| [Git Flow](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Gestão de branches, releases, workflow Git. | Controle de versão para projetos de plugins BIM |

### Regras de Codificação (por Linguagem)

> De [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) (38.700+ stars) — arquivos `.cursorrules` organizados por linguagem. Abaixo estão os mais relevantes para stacks de desenvolvimento AEC.

**Python** (Dynamo, IfcOpenShell, MCP servers, processamento de dados)

| Regra | Link |
|-------|------|
| Python Best Practices | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/python-cursorrules-prompt-file-best-practices) |
| Python Developer | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/python-developer-cursorrules-prompt-file) |
| Python Projects Guide | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/python-projects-guide-cursorrules-prompt-file) |
| Python FastAPI Best Practices | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/python-fastapi-best-practices-cursorrules-prompt-f) |
| Python Containerization | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/python-containerization-cursorrules-prompt-file) |
| Python LLM/ML Workflow | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/python-llm-ml-workflow-cursorrules-prompt-file) |

**C# / .NET** (Revit API, Civil 3D, Tekla, ArcGIS Pro)

| Regra | Link |
|-------|------|
| Unity C# (padrões similares ao C# do Revit) | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/unity-cursor-ai-c-cursorrules-prompt-file) |

**TypeScript** (MCP servers, dashboards web, integrações Speckle)

| Regra | Link |
|-------|------|
| TypeScript Code Convention | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/typescript-code-convention-cursorrules-prompt-file) |
| TypeScript + Node.js + Next.js + AI | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/typescript-nodejs-nextjs-ai-cursorrules-prompt-fil) |
| TypeScript LLM Tech Stack | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/typescript-llm-tech-stack-cursorrules-prompt-file) |

**Geral**

| Regra | Link |
|-------|------|
| Code Guidelines | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/code-guidelines-cursorrules-prompt-file) |
| Code Style Consistency | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/code-style-consistency-cursorrules-prompt-file) |

### Frameworks de Geração de Skills & Rules

| Recurso | Descrição | Link |
|---------|-----------|------|
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
| [OpenConstructionERP](https://openconstructionerp.com/) | Estimativa de construção gratuita e open-source. 55K+ itens de custo, 21 idiomas, takeoff com IA de PDFs/fotos/CAD. |
| [Bidwright](https://github.com/braedonsaunders/bidwright) | Workflow completo de licitação AI-native — intake, takeoff, precificação, cronograma e propostas em PDF. Open-source (MIT). |

### 📋 Gestão de Projetos & Planejamento

| Ferramenta | Descrição |
|------------|-----------|
| [Tekla 2026](https://www.tekla.com/) | Assistente IA para modelagem e desenhos de fabricação com linguagem natural. |
| [Trimble Connect](https://connect.trimble.com/) | Plataforma cloud de colaboração com BCF 3.0 e sincronização em tempo real. |
| [Speckle](https://speckle.systems/) | "Git para BIM" — colaboração open-source e interoperabilidade entre ferramentas AEC. |
| [Procore](https://www.procore.com/) | Plataforma líder de gestão de obras com recursos IA, RFIs, submittals, orçamentos e integração MCP. |
| [VIKTOR](https://www.viktor.ai/) | Plataforma de engenharia com agentes IA e integração MCP. Integração ETABS/SAP2000, apps web paramétricas e workflows com LLM. |

### 📡 Monitoramento de Obras & LiDAR

| Ferramenta | Descrição |
|------------|-----------|
| [viLid (viact.ai)](https://www.viact.ai/vilid) | Monitoramento LiDAR 4D com IA para tracking de progresso e detecção de desvios. |
| [Carlson Point Cloud 2026](https://carlsonps.com/products/carlsonpointcloud) | Processamento de nuvens de pontos de LiDAR, fotogrametria e drones. |

### 🎨 Design Generativo & Assistentes

| Ferramenta | Descrição |
|------------|-----------|
| [OpenPencil](https://github.com/open-pencil/open-pencil) | Editor de design open-source com 90+ ferramentas IA, servidor MCP e export Tailwind CSS. |
| [StructureClaw](https://github.com/structureclaw/structureclaw) | Workspace de engenharia estrutural assistido por IA — linguagem natural para artefatos de análise com validação e verificação de código. |
| [Structural LLaMA](https://github.com/joreilly86/structual_llama) | Assistente IA open-source para engenharia estrutural baseado no Llama2-13b. Orientação de projeto, ajuda com Python e conformidade com normas. |

---

## Recursos Educacionais

| Recurso | Descrição |
|---------|-----------|
| [Awesome-AECO](https://github.com/osama-ata/Awesome-AECO) | Lista curada de ferramentas open-source para o ambiente construído (BIM, CAD, simulação, digital twins). |
| [That Open Engine Docs](https://docs.thatopen.com/) | Documentação oficial do That Open Engine — bibliotecas BIM open-source para web (parsing IFC, viewer 3D, fragments, components). |
| [MCP Protocol Docs](https://modelcontextprotocol.io/) | Documentação oficial do Model Context Protocol. |
| [Modular Reference Architecture for MCP-Servers (Paper)](https://ui.adsabs.harvard.edu/abs/2026arXiv260100809H/abstract) | Paper acadêmico propondo arquitetura modular de referência para servidores MCP em interações BIM agentic. |
| [MCP Servers in Construction (Autodesk Blog)](https://www.autodesk.com/blogs/construction/mcp-servers-in-construction/) | Post do blog da Autodesk explicando MCP servers no contexto da construção. |
| [AI Agents & MCP para Engenheiros (VIKTOR)](https://www.viktor.ai/blog/196/how-engineers-can-use-ai-agents-and-mcp-servers-to-work-smarter) | Guia prático sobre como engenheiros podem usar agentes de IA e servidores MCP no dia a dia. |
| [Cursor Rules Guide](https://skillsplayground.com/guides/cursor-rules/) | Guia completo sobre Rules e Skills no Cursor IDE. |
| [MCP4IFC Paper (arXiv)](https://arxiv.org/abs/2511.05533) | Paper sobre design de edifícios baseado em IFC usando LLMs via MCP. Framework para manipulação direta de IFC com consultas de cena, funções predefinidas e geração de código com RAG. |
| [CONTEXUS Smart Building Docs](https://contexus.io/) | Documentação do framework open-source de edifícios inteligentes — IoT, digital twins e analytics com IA para gestão de facilities. |

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
