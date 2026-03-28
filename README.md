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

### 📐 IFC & openBIM

> Interaction with IFC (Industry Foundation Classes) files for openBIM workflows.

| Project | Description | Language |
|---------|-------------|----------|
| [ifcMCP](https://github.com/smartaec/ifcmcp) | MCP server for IFC file interaction. Entity retrieval, property queries, spatial analysis, and wall opening detection. | Python |
| [IfcOpenShell](https://ifcopenshell.org/) | Open-source library for reading/writing IFC files. Foundation for many AEC MCP servers. | Python / C++ |

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

### 🌍 Geospatial & GIS

> Integration with GIS tools and geolocation services.

| Project | Description | Language |
|---------|-------------|----------|
| [QGIS MCP](https://github.com/jjsantos01/qgis_mcp) | QGIS integration with AI. Project/layer manipulation, processing algorithm execution, and PyQGIS code execution. 866+ stars. | Python |
| [ArcGIS Pro Bridge](https://market-mcp.com/mcp/arcgis-pro-bridge) | MCP framework connecting ArcGIS Pro to AI agents. Map queries and geoprocessing automation via natural language. | C# / .NET |
| [Mapbox MCP Server](https://github.com/mapbox/mcp-server) | Geocoding, POI search, multi-modal routing, travel time matrices, route optimization, and isochrones. | TypeScript |

### 🤝 BIM Collaboration Platforms

> Collaboration platforms and BIM data sharing.

| Project | Description | Language |
|---------|-------------|----------|
| [Speckle MCP](https://github.com/bimgeek/speckle-mcp) | MCP server for Speckle — the collaborative data hub for AEC. Project listing, model versions, object queries, and property retrieval. | Python |
| [Trimble Connect](https://developer.tekla.com/trimble-connect) | Cloud-based collaboration platform with APIs for integration, data sync, and BCF 3.0 support. | - |

### 💰 Construction Management & Cost

> AI tools for estimates, planning, and construction project management.

| Project | Description | Type |
|---------|-------------|------|
| [Planaut](https://planaut.ai/) | AI co-pilot for construction management. Processes documents (2000+ pages), extracts scope with CSI MasterFormat, generates CPM schedules and cost estimates. | SaaS |
| [BuildEngine](https://buildengine.ai/) | Generates construction estimates in 6 minutes (40x faster). Simulates the entire construction process, identifies missing scopes. | SaaS |
| [BuildX Protocol](https://buildx.pro/) | 2,182 cost calculators, AI for construction cost questions, and subcontractor marketplace. | SaaS |
| [BEXEL Manager](https://bexelmanager.com/cost-estimator) | 5D BIM cost management. 4D+5D simulations, quantity takeoff, cost analysis, cash flow, and AI analytics. | Software |

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

### 🛠️ Development Tools

> General development tools that support AEC workflows.

| Project | Description | Language |
|---------|-------------|----------|
| [GitHub MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/github) | GitHub API integration — repo management, PRs, issues. | TypeScript |
| [Git MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/git) | Direct Git operations for local repositories. | TypeScript |
| [Docker MCP](https://github.com/modelcontextprotocol/servers) | Docker operations for containers and compose stacks. | TypeScript |

---

## Skills & Rules for AEC

> Skills and Rules are persistent instructions that customize AI assistant behavior in IDEs like Cursor, VS Code, and others. Below are resources relevant to the AEC industry.

### What are they?

- **Rules** (`.cursor/rules/`): Always-on instructions that define coding standards, tech stack, and project conventions.
- **Skills** (`SKILL.md`): On-demand procedural instructions — "how-to" playbooks that agents apply when the task is relevant.
- **AGENTS.md**: Alternative file at the project root to guide AI agents.

### Collections & Frameworks

| Resource | Description | Link |
|----------|-------------|------|
| [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | The largest curated list of `.cursorrules` files. 38,700+ stars. Organized by framework and language. | [GitHub](https://github.com/PatrickJS/awesome-cursorrules) |
| [cursor-rules-and-prompts](https://github.com/thehimel/cursor-rules-and-prompts) | Comprehensive collection of rules and prompts for enforcing coding standards. | [GitHub](https://github.com/thehimel/cursor-rules-and-prompts) |
| [cursorskills](https://github.com/bluriesophos/cursorskills) | Reusable SKILL.md files — planning, code review, debugging, and data management workflows. | [GitHub](https://github.com/bluriesophos/cursorskills) |
| [cursor-anthropic-skills](https://github.com/SteelMorgan/cursor-anthropic-skills) | Anthropic-optimized cursor skills for structured agent workflows. | [GitHub](https://github.com/SteelMorgan/cursor-anthropic-skills) |

### AEC-Specific Resources

| Resource | Description | Link |
|----------|-------------|------|
| [cad2data-Revit-IFC-DWG-DGN](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN) | Automated CAD/BIM conversion workflows. Batch processing, validation, QTO reports, cost estimation, and carbon footprint analysis. No Autodesk license required. 284+ stars. | [GitHub](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN) |
| [Debugging Revit Plugins with Cursor](https://aps.autodesk.com/blog/debugging-revit-plugins-cursor-modern-developer-workflow) | Official Autodesk guide on debugging C# Revit add-ins using Cursor IDE with pre-configured debugging setup. | [Blog](https://aps.autodesk.com/blog/debugging-revit-plugins-cursor-modern-developer-workflow) |
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

### 📋 Project Management & Planning

| Tool | Description |
|------|-------------|
| [Tekla 2026](https://www.tekla.com/) | AI assistant for modeling and fabrication drawings with natural language. |
| [Trimble Connect](https://connect.trimble.com/) | Cloud collaboration platform with BCF 3.0 and real-time sync. |
| [Speckle](https://speckle.systems/) | "Git for BIM" — open-source collaboration and interoperability across AEC tools. |

### 📡 Site Monitoring & LiDAR

| Tool | Description |
|------|-------------|
| [viLid (viact.ai)](https://www.viact.ai/vilid) | 4D LiDAR monitoring with AI for progress tracking and deviation detection. |
| [Carlson Point Cloud 2026](https://carlsonps.com/products/carlsonpointcloud) | Point cloud processing from LiDAR, photogrammetry, and drones. |

### 🎨 Generative Design & Assistants

| Tool | Description |
|------|-------------|
| [OpenPencil](https://github.com/open-pencil/open-pencil) | Open-source design editor with 90+ AI tools, MCP server, and Tailwind CSS export. |

---

## Educational Resources

| Resource | Description |
|----------|-------------|
| [Awesome-AECO](https://github.com/osama-ata/Awesome-AECO) | Curated list of open-source tools for the built environment (BIM, CAD, simulation, digital twins). |
| [MCP Protocol Docs](https://modelcontextprotocol.io/) | Official Model Context Protocol documentation. |
| [Modular Reference Architecture for MCP-Servers (Paper)](https://ui.adsabs.harvard.edu/abs/2026arXiv260100809H/abstract) | Academic paper proposing a modular reference architecture for MCP servers in agentic BIM interactions. |
| [MCP Servers in Construction (Autodesk Blog)](https://www.autodesk.com/blogs/construction/mcp-servers-in-construction/) | Autodesk blog post explaining MCP servers in the context of construction. |
| [AI Agents & MCP for Engineers (VIKTOR)](https://www.viktor.ai/blog/196/how-engineers-can-use-ai-agents-and-mcp-servers-to-work-smarter) | Practical guide on how engineers can use AI agents and MCP servers in day-to-day work. |
| [Cursor Rules Guide](https://skillsplayground.com/guides/cursor-rules/) | Complete guide on Rules and Skills in Cursor IDE. |

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
