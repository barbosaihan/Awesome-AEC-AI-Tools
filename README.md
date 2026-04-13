# Awesome AI Tools for AEC [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of **Model Context Protocol (MCP) servers**, **Skills**, **Rules**, and **AI applications** for the **Architecture, Engineering, and Construction (AEC)** industry. The goal is to gather resources that help professionals integrate artificial intelligence into their workflows — from BIM modeling to construction site management.

[MCP](https://modelcontextprotocol.io/) is an open protocol that enables AI models to securely interact with local and remote resources through standardized server implementations.

> **Contribute!** This repository is collaborative. If you know of any MCP Server, Skill, or AI tool relevant to AEC that is not listed, open an [issue](../../issues) or submit a [pull request](../../pulls). See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

🇧🇷 [Versão em Português](README.pt-BR.md)

---

## Security Warning

> **Warning:** MCP servers execute code on your machine with the same permissions as the host process. Always review code before installing, run in isolated environments when possible, and limit permissions to the minimum required.

---

## Table of Contents

- [Compatible MCP Clients](#compatible-mcp-clients)
- [MCP Servers](#mcp-servers)
  - [BIM & 3D Modeling](#-bim--3d-modeling)
  - [IFC & openBIM](#-ifc--openbim)
  - [Parametric Design](#-parametric-design)
  - [Structural Engineering & FEA](#-structural-engineering--fea)
  - [Energy Simulation & Sustainability](#-energy-simulation--sustainability)
  - [Civil Engineering & Infrastructure](#-civil-engineering--infrastructure)
  - [Geospatial & GIS](#-geospatial--gis)
  - [BIM Collaboration Platforms](#-bim-collaboration-platforms)
  - [Construction Management & Cost](#-construction-management--cost)
  - [Documents & Files](#-documents--files)
  - [Databases](#-databases)
  - [Search & Web](#-search--web)
  - [Data Visualization](#-data-visualization)
  - [Photogrammetry & Site Scanning](#-photogrammetry--site-scanning)
  - [IoT & Digital Twins](#-iot--digital-twins)
  - [Development Tools](#-development-tools)
- [Skills & Rules for AEC](#skills--rules-for-aec)
- [AI Applications for AEC](#ai-applications-for-aec)
  - [Cost Estimation](#-cost-estimation)
  - [Project Management & Planning](#-project-management--planning)
  - [Site Monitoring & LiDAR](#-site-monitoring--lidar)
  - [Generative Design & Assistants](#-generative-design--assistants)
- [Educational Resources](#educational-resources)
- [How to Contribute](#how-to-contribute)

---

## Compatible MCP Clients

The MCP Servers listed here can be used with various compatible clients:

| Client | Documentation |
|--------|---------------|
| [Claude Desktop](https://claude.ai) | [Claude x MCP](https://modelcontextprotocol.io/quickstart) |
| [Cursor](https://www.cursor.com/) | [Cursor x MCP](https://docs.cursor.com/advanced/model-context-protocol) |
| [VS Code](https://code.visualstudio.com/) | [VS Code x MCP](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) |
| [Zed Editor](https://zed.dev/) | [Zed x MCP](https://zed.dev/blog/mcp) |
| [Continue](https://www.continue.dev/) | [Continue x MCP](https://blog.continue.dev/model-context-protocol) |
| [Goose](https://block.github.io/goose/) | [Goose x MCP](https://block.github.io/goose/docs/getting-started/using-extensions) |

---

## MCP Servers

### 🏗️ BIM & 3D Modeling

> Servers that enable direct interaction with BIM tools like Revit and Tekla via natural language.

| Project | Description | Language |
|---------|-------------|----------|
| [RevitMCPBridge2026](https://github.com/WeberG619/RevitMCPBridge2026) | 705+ MCP endpoints for full Revit 2026 control via named pipes. Wall creation, door placement, views, documentation, and code compliance checks. | Python / C# |
| [Revit 2026 MCP Server](https://github.com/antonhofstader/Revit-2026-MCP-Server) | MCP server for Revit 2026 with C# add-in and JSON-RPC communication. Element queries, parameter modification, and view creation. | Python / C# |
| [Revit MCP (mcp-servers-for-revit)](https://github.com/mcp-servers-for-revit) | Organization hosting multiple MCP implementations for Revit (TypeScript and Python). 363+ stars. | TS / Python |
| [APS AECDM MCP](https://github.com/autodesk-platform-services/aps-aecdm-mcp-dotnet) | .NET MCP Server connecting Claude Desktop with the AEC Data Model API. Query design data, filter elements by category, and render models in the Viewer. | C# / .NET |
| [APS Revit MCP Tools Bundle](https://github.com/autodesk-platform-services/aps-sample-revit-mcp-tools-bundle) | AppBundle for Automation API for Revit 2026. Execute custom tools on Revit Cloud Models through MCP. | Python |
| [APS MCP Server (Python)](https://github.com/autodesk-platform-services/aps-mcp-server-python) | MCP server for Autodesk Platform Services with different authentication approaches. | Python |
| [Autodesk MCP Servers](https://www.autodesk.com/solutions/autodesk-ai/autodesk-mcp-servers) ⭐ | Official Autodesk MCP servers for Revit, AutoCAD, Inventor, and Navisworks. | - |
| [TeklaMCPServer](https://github.com/YuriyKirillov/TeklaMCPServer) | MCP server for Tekla Structures. Component insertion/removal, element selection, property management, and geometric operations. | Python |
| [APS Revit Automation MCP](https://github.com/autodesk-platform-services/aps-sample-mcp-server-revit-automation) | Cloud-native MCP server for headless Revit automation via the Automation API. Works with ACC/BIM360 Cloud Models — no local Revit needed. | C# / .NET |
| [AutoCAD MCP (PeterPerez01)](https://github.com/PeterPerez01/autocad-mcp) | MCP server for AutoCAD via Windows COM. Intelligent creation (walls, doors, windows, rooms, furniture), geometry, layer management, and entity inspection. | Python |
| [Blender MCP](https://github.com/ahujasid/blender-mcp) | MCP server for Blender with object manipulation, materials, geometry nodes, Poly Haven assets, Hunyuan3D, and Hyper3D Rodin model generation. 18,300+ stars. | Python |
| [FreeCAD MCP (ContextForm)](https://github.com/contextform/freecad-mcp) | AI-driven FreeCAD control — sketch creation, 3D operations (extrude, revolve, loft), parametric design, and multi-format file management. 65+ stars. | Python |
| [FreeCAD Robust MCP](https://github.com/spkane/freecad-robust-mcp-and-more) | Robust FreeCAD MCP server with XML-RPC/JSON-RPC, headless mode, Docker support, and document management tools. 55+ stars. | Python |
| [OpenSCAD MCP Server](https://github.com/jhacksman/OpenSCAD-MCP-Server) | Natural language to parametric 3D models. Multi-view generation, AI image generation (Gemini/Venice.ai), multi-format export, and 3D printer integration. 139+ stars. | Python |
| [That Open Engine (components)](https://github.com/ThatOpen/engine_components) | Open-source BIM toolkit — viewer, fragments, property management, spatial indexing, and more. Build full BIM web apps on Three.js. 624+ stars. | TypeScript |
| [That Open Engine (clay)](https://github.com/ThatOpen/engine_clay) | Lightweight open-source BIM modelling engine for creating and editing 3D BIM geometry programmatically. | TypeScript |
| [That Open Engine (fragments)](https://github.com/ThatOpen/engine_fragment) | High-performance 3D geometry engine optimized for loading and rendering large BIM models in the browser. 174+ stars. | TypeScript |

### 📐 IFC & openBIM

> Interaction with IFC (Industry Foundation Classes) files for openBIM workflows.

| Project | Description | Language |
|---------|-------------|----------|
| [ifcMCP](https://github.com/smartaec/ifcmcp) | MCP server for IFC file interaction. Entity retrieval, property queries, spatial analysis, and wall opening detection. | Python |
| [IfcOpenShell](https://ifcopenshell.org/) | Open-source library for reading/writing IFC files. Foundation for many AEC MCP servers. | Python / C++ |
| [MCP4IFC](https://github.com/Show2Instruct/ifc-bonsai-mcp) | Open-source framework enabling LLMs to directly create and modify IFC building data via MCP. Integrates with Blender/Bonsai add-on and IfcOpenShell. RAG-powered code generation. | Python |
| [That Open Engine (web-ifc)](https://github.com/ThatOpen/engine_web-ifc) | Reading and writing IFC files with JavaScript at native speeds. WebAssembly-based parser for browser and Node.js. 933+ stars. | TypeScript |
| [web-ifc-three](https://github.com/ThatOpen/web-ifc-three) | The official IFC Loader for Three.js. Enables rendering IFC models directly in 3D web viewers. 582+ stars. | JavaScript |

### 🎨 Parametric Design

> MCP servers for Rhino and Grasshopper integration, enabling AI-assisted parametric design.

| Project | Description | Language |
|---------|-------------|----------|
| [Cordyceps](https://github.com/brookstalley/cordyceps) | MCP server for Rhino 8.21+ with full Grasshopper control (components, wiring, groups) and Rhino integration (bake, layers, rendering). | C# |
| [GH_mcp_server](https://github.com/veoery/gh_mcp_server) | Direct LLM interaction with Rhino/Grasshopper. Analyze .3dm files, 3D modeling, and automatic GHPython code generation. | Python |
| [Grasshopper MCP (dongwoosuk)](https://playbooks.com/mcp/dongwoosuk/grasshopper-mcp) | Rhino/Grasshopper integration with AI-powered mentoring, ML-based layout optimization, and Python execution in Rhino. | Python |
| [AI-architecture](https://github.com/Xiaohu1009/AI-architecture) | Unified Rhino + Grasshopper integration with smart routing, object creation, parametric operations, and pattern recognition. | Python |

### 🔩 Structural Engineering & FEA

> Finite Element Analysis and structural engineering tools accessible via MCP.

| Project | Description | Language |
|---------|-------------|----------|
| [FEA-MCP](https://github.com/greatapo/fea-mcp) | MCP server for Finite Element Analysis. Unified API for FEA software (ETABS and LUSAS support). Geometric modeling, analysis, and post-processing. | Python |
| [StructureClaw](https://github.com/structureclaw/structureclaw) | AI-assisted structural engineering workspace. Conversational workflow from natural language to analysis artifacts with draft, validate, analyze, and code-check loop. 35+ stars. | TypeScript / Python |
| [Talk with Your ETABS Model (VIKTOR)](https://github.com/viktor-platform/talk-with-your-model) | AI agent for ETABS structural models. Query results, create heat maps, plot deformed shapes, and design pad foundations via natural language. | Python |

### ♻️ Energy Simulation & Sustainability

> Tools for building energy performance simulation.

| Project | Description | Language |
|---------|-------------|----------|
| [EnergyPlus-MCP](https://www.osti.gov/pages/biblio/3015372) | First open-source MCP server for EnergyPlus. 35 specialized tools for model management, editing, HVAC configuration, and simulation execution. | Python |
| [idfkit-mcp](https://github.com/idfkit/idfkit-mcp/) | MCP server for EnergyPlus energy simulation. Install via pip/uv, multi-client support (Claude, Cursor, VS Code). | Python |
| [OpenStudio MCP](https://github.com/NatLabRockies/openstudio-mcp) | 22 skills, 126 MCP tools for OpenStudio energy simulation. Create, modify, and simulate energy models via natural language. Docker support. 450+ tests. | Python |

### 🚧 Civil Engineering & Infrastructure

> Calculations and tools for civil engineering, hydrology, and infrastructure.

| Project | Description | Language |
|---------|-------------|----------|
| [Civil Engineering Tools Server](https://ubos.tech/mcp/mcp-civil-tools/overview/) | Specialized calculations: coordinate conversion, IDF curves, infiltration, slope stability, retaining walls, runoff, and drainage analysis. | Python |
| [Civil3D MCP](https://github.com/Sacred-G/Civil3D-mcp) | MCP server for Autodesk Civil 3D. Create, modify, and query civil design elements — points, alignments, profiles, surfaces, and line segments. | C# / TypeScript |

### 🌍 Geospatial & GIS

> Integration with GIS tools and geolocation services.

| Project | Description | Language |
|---------|-------------|----------|
| [QGIS MCP](https://github.com/jjsantos01/qgis_mcp) | QGIS integration with AI. Project/layer manipulation, processing algorithm execution, and PyQGIS code execution. 866+ stars. | Python |
| [ArcGIS Pro Bridge](https://market-mcp.com/mcp/arcgis-pro-bridge) | MCP framework connecting ArcGIS Pro to AI agents. Map queries and geoprocessing automation via natural language. | C# / .NET |
| [Mapbox MCP Server](https://github.com/mapbox/mcp-server) | Geocoding, POI search, multi-modal routing, travel time matrices, route optimization, and isochrones. | TypeScript |
| [gis-mcp](https://github.com/mahdin75/gis-mcp) | 100+ geospatial tools using Shapely, GeoPandas, PyProj, and Rasterio. Buffer, intersection, Voronoi, transformations, and vector I/O. 126+ stars. | Python |
| [Overture Maps MCP](https://github.com/srivinod1/overture-mcp-server) | Spatial analytics on Overture Maps data — Places, Buildings, Transportation, Divisions, and Land Use. DuckDB + GeoParquet, no credentials required. | Python |
| [Axion Planetary MCP](https://github.com/Dhenenjay/axion-planetary-mcp) | Google Earth Engine integration via MCP. 30+ satellite datasets (Landsat, Sentinel, MODIS), NDVI/NDWI, wildfire risk, flood modeling, and deforestation detection. 217+ stars. | Python |
| [geeViz MCP](https://geeviz.org/mcp_server.html) | Python toolkit for Google Earth Engine with 34 MCP tools. Execute code and inspect live GEE assets via AI assistants. | Python |

### 🤝 BIM Collaboration Platforms

> Collaboration platforms and BIM data sharing.

| Project | Description | Language |
|---------|-------------|----------|
| [Speckle MCP](https://github.com/bimgeek/speckle-mcp) | MCP server for Speckle — the collaborative data hub for AEC. Project listing, model versions, object queries, and property retrieval. | Python |
| [Trimble Connect](https://developer.tekla.com/trimble-connect) | Cloud-based collaboration platform with APIs for integration, data sync, and BCF 3.0 support. | - |
| [Procore MCP Server](https://github.com/zeniasupp0rt-cmyk/procore-mcp-server) | MCP server for Procore construction management. Projects, RFIs, submittals, documents, and budget access via AI assistants. OAuth2 auth. | TypeScript |

### 💰 Construction Management & Cost

> AI tools for estimates, planning, and construction project management.

| Project | Description | Type |
|---------|-------------|------|
| [Planaut](https://planaut.ai/) | AI co-pilot for construction management. Processes documents (2000+ pages), extracts scope with CSI MasterFormat, generates CPM schedules and cost estimates. | SaaS |
| [BuildEngine](https://buildengine.ai/) | Generates construction estimates in 6 minutes (40x faster). Simulates the entire construction process, identifies missing scopes. | SaaS |
| [BuildX Protocol](https://buildx.pro/) | 2,182 cost calculators, AI for construction cost questions, and subcontractor marketplace. | SaaS |
| [BEXEL Manager](https://bexelmanager.com/cost-estimator) | 5D BIM cost management. 4D+5D simulations, quantity takeoff, cost analysis, cash flow, and AI analytics. | Software |
| [OpenConstructionERP](https://github.com/datadrivenconstruction/OpenConstructionERP) | Open-source construction estimation platform. AI-powered takeoff (16 LLM providers), 55K+ cost items, 21 languages, 4D/5D planning, BIM viewer. AGPL-3.0. | Open Source |
| [Bidwright](https://github.com/braedonsaunders/bidwright) | AI-native construction estimating platform. Bid intake, drawing takeoff with annotations, pricing, scheduling, quote PDF generation, and MCP server. MIT. | Open Source |

### 📄 Documents & Files

> Tools for processing technical documents, contracts, and specifications.

| Project | Description | Language |
|---------|-------------|----------|
| [Fetch MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) | Efficient web content fetching and processing for AI consumption. | Python |
| [FileSystem MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | Direct local file system access with configurable permissions. | TypeScript |

### 🗄️ Databases

> Database access for project data storage and querying.

| Project | Description | Language |
|---------|-------------|----------|
| [PostgreSQL MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) | PostgreSQL integration — schema inspection and query execution. | TypeScript |
| [SQLite MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) | SQLite operations with built-in analysis features. | Python |
| [DuckDB MCP](https://github.com/modelcontextprotocol/servers) | DuckDB integration for high-performance local data analysis. | Python |

### 🔍 Search & Web

> Web search and browser automation for technical research.

| Project | Description | Language |
|---------|-------------|----------|
| [Brave Search MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) | Web search via Brave Search API. | TypeScript |
| [Puppeteer MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) | Browser automation for scraping and web interaction. | TypeScript |
| [Playwright MCP](https://github.com/executeautomation/mcp-playwright) | Browser automation via Playwright for testing and scraping. | TypeScript |
| [ArXiv MCP](https://github.com/modelcontextprotocol/servers) | Search scientific papers on ArXiv — useful for technical research. | Python |

### 📊 Data Visualization

> Chart and visualization generation for project data analysis.

| Project | Description | Language |
|---------|-------------|----------|
| [ECharts MCP](https://github.com/modelcontextprotocol/servers) | Dynamic chart generation with Apache ECharts via AI. | TypeScript |
| [Mermaid MCP](https://github.com/modelcontextprotocol/servers) | Diagram and flowchart generation with Mermaid via AI. | TypeScript |
| [VegaLite MCP](https://github.com/modelcontextprotocol/servers) | VegaLite visualizations from processed data. | TypeScript |

### 📷 Photogrammetry & Site Scanning

> Tools for photogrammetry pipelines, drone surveys, and 3D reconstruction.

| Project | Description | Language |
|---------|-------------|----------|
| [Metashape MCP](https://github.com/jenkinsm13/metashape-mcp) | AI-powered MCP server for Agisoft Metashape Professional 2.3+. 106 tools across 15 modules — full photogrammetry pipeline from alignment to orthomosaic export. Headless mode for CI. | Python |

### 🏠 IoT & Digital Twins

> Smart building platforms connecting IoT sensors, digital twins, and AI analytics.

| Project | Description | Language |
|---------|-------------|----------|
| [CONTEXUS](https://github.com/contexusio/contexus) | Open-source modular smart building framework. 13+ modules, IoT connectivity (LoRaWAN, MQTT, BACnet, Modbus), 3D BIM digital twin with real-time sensor overlays, and AI-powered predictive maintenance. MIT. | TypeScript / Shell |
| [Digital Twin MCP](https://github.com/aisystant/digital-twin-mcp) | Metamodel-driven digital twin MCP server with 65+ hierarchical indicators, access control, and Cloudflare Workers deployment. | TypeScript |

### 🛠️ Development Tools

> General development tools that support AEC workflows.

| Project | Description | Language |
|---------|-------------|----------|
| [GitHub MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/github) | GitHub API integration — repo management, PRs, issues. | TypeScript |
| [Git MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/git) | Direct Git operations for local repositories. | TypeScript |
| [Docker MCP](https://github.com/modelcontextprotocol/servers) | Docker operations for containers and compose stacks. | TypeScript |
| [That Open Engine (UI Components)](https://github.com/ThatOpen/engine_ui-components) | Collection of web components for building BIM application interfaces — panels, trees, property tables, and more. | TypeScript |
| [That Open Engine (Templates)](https://github.com/ThatOpen/engine_templates) | Starter templates for quickly bootstrapping BIM web applications with That Open Engine. | TypeScript |

---

## Skills & Rules for AEC

> Skills and Rules are persistent instructions that customize AI assistant behavior in IDEs like Cursor, VS Code, and others. Below are resources curated for AEC professionals — from workflow discipline skills to language-specific coding rules.

### What are they?

- **Rules** (`.cursor/rules/`): Always-on instructions that define coding standards, tech stack, and project conventions.
- **Skills** (`SKILL.md`): On-demand procedural instructions — "how-to" playbooks that agents apply when the task is relevant.
- **AGENTS.md**: Alternative file at the project root to guide AI agents.

### AEC-Specific Resources

| Resource | Description | Link |
|----------|-------------|------|
| [cad2data-Revit-IFC-DWG-DGN](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN) | Automated CAD/BIM conversion workflows with AI agent integration. Batch processing, validation, QTO reports, cost estimation, and carbon footprint analysis. No Autodesk license required. 284+ stars. | [GitHub](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN) |
| [Debugging Revit Plugins with Cursor](https://aps.autodesk.com/blog/debugging-revit-plugins-cursor-modern-developer-workflow) | Official Autodesk guide on debugging C# Revit add-ins using Cursor IDE with pre-configured debugging setup. | [Blog](https://aps.autodesk.com/blog/debugging-revit-plugins-cursor-modern-developer-workflow) |

### Workflow & Discipline Skills

> From [cursorskills](https://github.com/bluriesophos/cursorskills) — process-oriented skills that bring structure to AEC development. Install by copying the skill folder to `~/.cursor/skills/` (personal) or `.cursor/skills/` (project).

| Skill | What it does | Why it matters for AEC |
|-------|-------------|----------------------|
| [battle-plan](https://github.com/bluriesophos/cursorskills/tree/main/battle-plan) | Complete planning ritual before significant tasks — scope, risk assessment, estimation, confirmation. | Complex BIM automation and plugin development needs upfront planning. |
| [pre-mortem](https://github.com/bluriesophos/cursorskills/tree/main/pre-mortem) | Imagines failure scenarios and reorders the implementation plan to address high-risk items first. | Prevents costly mistakes in Revit transactions, IFC processing, and structural analysis scripts. |
| [split-decision](https://github.com/bluriesophos/cursorskills/tree/main/split-decision) | Presents 2-4 options as a comparison table with trade-offs before committing to architecture/technology choices. | Choosing between BIM APIs, data formats (IFC vs RVT), or simulation approaches. |
| [code-review](https://github.com/bluriesophos/cursorskills/tree/main/code-review) | Structured review against 14 quality criteria (design, security, performance, testing). | Essential for reviewing Revit add-ins and Grasshopper components before deployment. |
| [debug-to-fix](https://github.com/bluriesophos/cursorskills/tree/main/debug-to-fix) | Full debug cycle: clarify, investigate, fix, verify. Prevents jumping to fixes. | Debugging Revit API issues, Grasshopper data trees, and IFC parsing errors. |
| [prove-it](https://github.com/bluriesophos/cursorskills/tree/main/prove-it) | Verifies outcomes before declaring tasks complete. Run the code, test the fix. | Ensures BIM scripts actually produce correct geometry/data before sign-off. |
| [safe-refactor](https://github.com/bluriesophos/cursorskills/tree/main/safe-refactor) | Refactoring cycle with risk assessment, preparation, implementation, and verification. | Refactoring large Revit plugins or shared BIM utility libraries safely. |
| [trace-it](https://github.com/bluriesophos/cursorskills/tree/main/trace-it) | Traces all callers before modifying shared code (utils, types, configs). | Prevents "fixed one thing, broke three others" in shared BIM libraries. |
| [breadcrumbs](https://github.com/bluriesophos/cursorskills/tree/main/breadcrumbs) | Leaves notes for future sessions in `.cursor/breadcrumbs.md`. | Long-running BIM automation projects benefit from session-to-session memory. |
| [pair-mode](https://github.com/bluriesophos/cursorskills/tree/main/pair-mode) | Transforms agent into a pair programming partner that explains reasoning. | Learning Revit API, IfcOpenShell, or Grasshopper scripting with guided assistance. |
| [you-sure](https://github.com/bluriesophos/cursorskills/tree/main/you-sure) | Pauses before destructive/irreversible actions with impact checklist. | Prevents accidental model corruption in Revit transactions or database operations. |

### Domain-Specific Skills

> From [cursor-anthropic-skills](https://github.com/SteelMorgan/cursor-anthropic-skills) — 70+ specialized skills covering development, data, MCP, and more. The skills below are particularly relevant for AEC workflows.

**Document & Data Processing**

| Skill | Description | AEC Use Case |
|-------|-------------|-------------|
| [Document Processing (PDF)](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Create, merge, extract from PDFs. Fillable forms support. | Technical specs, construction docs, RFIs |
| [Document Processing (Excel)](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Spreadsheet creation, data analysis, charts, formulas. | BOQs, cost estimates, quantity takeoffs |
| [Document Processing (DOCX)](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Word document creation and report generation. | Project reports, meeting minutes, RFPs |
| [Document Processing (PPTX)](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Presentation and slide deck creation. | Client presentations, design reviews |
| [Visual OCR](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Text extraction from images via OCR. | Extracting text from scanned drawings and plans |
| [Document Structure Analysis](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Analyze document layouts and structure. | Parsing technical specifications and contracts |

**MCP Development**

| Skill | Description | AEC Use Case |
|-------|-------------|-------------|
| [MCP Server Architecture](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Design and implement MCP servers. | Building custom AEC MCP servers |
| [MCP Integration](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Multi-server orchestration and workflows. | Connecting Revit + IFC + GIS MCP servers |
| [MCP Protocol](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | MCP specification and standards compliance. | Ensuring MCP compliance for BIM tools |
| [MCP Testing](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Testing MCP server implementations. | QA for AEC MCP servers |

**Data & AI**

| Skill | Description | AEC Use Case |
|-------|-------------|-------------|
| [Data Engineering](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | ETL/ELT pipelines, data warehouses, infrastructure. | BIM data pipelines, IFC-to-database ETL |
| [Data Science](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Statistical modeling, predictive analytics, exploratory analysis. | Construction data analysis, trend prediction |
| [Computer Vision](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Image processing, recognition, and analysis. | Site monitoring, progress tracking from photos |
| [3D Art](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | 3D assets, modeling, and optimization. | 3D visualization for architectural models |

**Development & DevOps**

| Skill | Description | AEC Use Case |
|-------|-------------|-------------|
| [Debugging](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Structured error debugging and root cause analysis. | Debugging Revit add-ins and Grasshopper scripts |
| [Code Review](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Structured code quality review. | Review of BIM plugin code |
| [Docker Operations](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Container management, compose, health checks. | Containerized BIM processing, MCP server deployment |
| [PowerShell](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Windows scripting and automation. | Windows automation for AEC tools (most run on Windows) |
| [Mermaid Diagrams](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Flowcharts, sequence diagrams, ERDs, Gantt charts. | Process flows, project timelines, architecture diagrams |
| [Technical Writing](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | User guides, tutorials, technical documentation. | Plugin documentation, API guides |
| [API Documentation](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | OpenAPI specs, SDK generation, developer docs. | Documenting BIM APIs and MCP servers |
| [Git Flow](https://github.com/SteelMorgan/cursor-anthropic-skills/tree/main/custom-skills/claude-agent-skills) | Branch management, release management, Git workflow. | Version control for BIM plugin projects |

### Coding Rules (Language-Specific)

> From [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) (38,700+ stars) — `.cursorrules` files organized by language. Below are the ones most relevant to AEC development stacks.

**Python** (Dynamo, IfcOpenShell, MCP servers, data processing)

| Rule | Link |
|------|------|
| Python Best Practices | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/python-cursorrules-prompt-file-best-practices) |
| Python Developer | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/python-developer-cursorrules-prompt-file) |
| Python Projects Guide | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/python-projects-guide-cursorrules-prompt-file) |
| Python FastAPI Best Practices | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/python-fastapi-best-practices-cursorrules-prompt-f) |
| Python Containerization | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/python-containerization-cursorrules-prompt-file) |
| Python LLM/ML Workflow | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/python-llm-ml-workflow-cursorrules-prompt-file) |

**C# / .NET** (Revit API, Civil 3D, Tekla, ArcGIS Pro)

| Rule | Link |
|------|------|
| Unity C# (similar patterns to Revit C#) | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/unity-cursor-ai-c-cursorrules-prompt-file) |

**TypeScript** (MCP servers, web dashboards, Speckle integrations)

| Rule | Link |
|------|------|
| TypeScript Code Convention | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/typescript-code-convention-cursorrules-prompt-file) |
| TypeScript + Node.js + Next.js + AI | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/typescript-nodejs-nextjs-ai-cursorrules-prompt-fil) |
| TypeScript LLM Tech Stack | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/typescript-llm-tech-stack-cursorrules-prompt-file) |

**General**

| Rule | Link |
|------|------|
| Code Guidelines | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/code-guidelines-cursorrules-prompt-file) |
| Code Style Consistency | [GitHub](https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules/code-style-consistency-cursorrules-prompt-file) |

### Skill & Rule Generation Frameworks

| Resource | Description | Link |
|----------|-------------|------|
| [cursor-custom-agents-rules-generator](https://github.com/bmadcode/cursor-custom-agents-rules-generator) | Framework for automatic rule and custom agent generation. Useful as a base for creating AEC-specific rules. | [GitHub](https://github.com/bmadcode/cursor-custom-agents-rules-generator) |

### Community Skills & Rules (Open for Contribution)

We're building a collection of AEC-specific Skills and Rules. Topics we're looking for:

- **Revit API** — Coding conventions for C#/Python Revit plugins (transactions, FilteredElementCollector, parameters)
- **Dynamo / Python** — Standards for Dynamo scripts in BIM projects
- **IFC Processing** — Conventions for IfcOpenShell-based parsers and validators
- **Civil 3D API** — Patterns for Civil 3D .NET API development
- **Grasshopper / RhinoCommon** — Rules for Grasshopper component development and RhinoCommon scripting
- **Construction Documentation** — Rules for automated generation of technical documents and reports

> **Want to contribute?** See [CONTRIBUTING.md](CONTRIBUTING.md) for the template and guidelines.

---

## AI Applications for AEC

> AI tools and platforms (not necessarily MCP) that bring significant gains for AEC professionals.

### 💵 Cost Estimation

| Tool | Description |
|------|-------------|
| [Planaut](https://planaut.ai/) | AI for scope extraction, CPM schedules, and cost estimates from documents. |
| [BuildEngine](https://buildengine.ai/) | Estimates in 6 minutes simulating the construction process. |
| [BuildX Protocol](https://buildx.pro/) | 2,182 cost calculators with AI for US construction. |
| [BEXEL Manager](https://bexelmanager.com/) | 5D BIM management with 4D+5D simulations and AI. |
| [OpenConstructionERP](https://openconstructionerp.com/) | Free, open-source construction estimation. 55K+ cost items, 21 languages, AI takeoff from PDFs/photos/CAD. |
| [Bidwright](https://github.com/braedonsaunders/bidwright) | AI-native bid workflow — intake, takeoff, pricing, scheduling, and branded PDF quotes. Open-source (MIT). |

### 📋 Project Management & Planning

| Tool | Description |
|------|-------------|
| [Tekla 2026](https://www.tekla.com/) | AI assistant for modeling and fabrication drawings with natural language. |
| [Trimble Connect](https://connect.trimble.com/) | Cloud collaboration platform with BCF 3.0 and real-time sync. |
| [Speckle](https://speckle.systems/) | "Git for BIM" — open-source collaboration and interoperability across AEC tools. |
| [Procore](https://www.procore.com/) | Leading construction management platform with AI features, RFIs, submittals, budgets, and MCP integration. |
| [VIKTOR](https://www.viktor.ai/) | Engineering platform with AI agents and MCP integration. ETABS/SAP2000 integration, parametric web apps, and LLM-powered workflows. |

### 📡 Site Monitoring & LiDAR

| Tool | Description |
|------|-------------|
| [viLid (viact.ai)](https://www.viact.ai/vilid) | 4D LiDAR monitoring with AI for progress tracking and deviation detection. |
| [Carlson Point Cloud 2026](https://carlsonps.com/products/carlsonpointcloud) | Point cloud processing from LiDAR, photogrammetry, and drones. |

### 🎨 Generative Design & Assistants

| Tool | Description |
|------|-------------|
| [OpenPencil](https://github.com/open-pencil/open-pencil) | Open-source design editor with 90+ AI tools, MCP server, and Tailwind CSS export. |
| [StructureClaw](https://github.com/structureclaw/structureclaw) | AI-assisted structural engineering workspace — natural language to analysis artifacts with validation and code-checking. |
| [Structural LLaMA](https://github.com/joreilly86/structual_llama) | Open-source AI assistant for structural engineering built on Llama2-13b. Design guidance, Python code help, and code compliance. |

---

## Educational Resources

| Resource | Description |
|----------|-------------|
| [Awesome-AECO](https://github.com/osama-ata/Awesome-AECO) | Curated list of open-source tools for the built environment (BIM, CAD, simulation, digital twins). |
| [That Open Engine Docs](https://docs.thatopen.com/) | Official documentation for That Open Engine — open-source BIM libraries for web (IFC parsing, 3D viewer, fragments, components). |
| [MCP Protocol Docs](https://modelcontextprotocol.io/) | Official Model Context Protocol documentation. |
| [Modular Reference Architecture for MCP-Servers (Paper)](https://ui.adsabs.harvard.edu/abs/2026arXiv260100809H/abstract) | Academic paper proposing a modular reference architecture for MCP servers in agentic BIM interactions. |
| [MCP Servers in Construction (Autodesk Blog)](https://www.autodesk.com/blogs/construction/mcp-servers-in-construction/) | Autodesk blog post explaining MCP servers in the context of construction. |
| [AI Agents & MCP for Engineers (VIKTOR)](https://www.viktor.ai/blog/196/how-engineers-can-use-ai-agents-and-mcp-servers-to-work-smarter) | Practical guide on how engineers can use AI agents and MCP servers in day-to-day work. |
| [Cursor Rules Guide](https://skillsplayground.com/guides/cursor-rules/) | Complete guide on Rules and Skills in Cursor IDE. |
| [MCP4IFC Paper (arXiv)](https://arxiv.org/abs/2511.05533) | Research paper on IFC-based building design using LLMs via MCP. Framework for direct IFC manipulation with scene querying, predefined functions, and RAG-powered code generation. |
| [CONTEXUS Smart Building Docs](https://contexus.io/) | Documentation for the open-source smart building framework — IoT, digital twins, and AI analytics for facility management. |

---

## How to Contribute

Contributions are very welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to add new resources.

Ways to contribute:
- Add new MCP Servers for AEC
- Share Skills & Rules for AEC development
- Suggest relevant AI applications for the industry
- Fix outdated information
- Improve descriptions and categorization

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ⭐ | Official implementation |
| 🆕 | Recently added |
| 🔧 | Under active development |
| 📖 | Well documented |

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the authors have waived all copyright and related or neighboring rights to this work.
