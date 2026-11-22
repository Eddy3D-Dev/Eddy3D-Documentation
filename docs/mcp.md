# Climate data for AI agents (MCP)

[climate.eddy3d.com](https://climate.eddy3d.com) has a Model Context Protocol (MCP) server. An AI agent connected to it can find weather stations and read each station's climate facts, weather-file downloads and chart links, without opening the website.

| | |
|---|---|
| Address | `https://climate.eddy3d.com/mcp` |
| Transport | Streamable HTTP |
| Sign-in | None |
| Access | Read-only |

## What an agent can do

| Tool | What it returns |
|---|---|
| `find_stations` | Stations matching every word of a query: a city, an airport name, a region code or a three-letter country code, such as `Furth DEU` or `Newark USA`. |
| `nearest_stations` | The stations closest to a latitude and longitude, nearest first, with the distance in km. |
| `get_station` | For one station: ASHRAE climate zone, Köppen class, design temperatures, degree days, elevation and coordinates; the download link of each weather file; a link to each climate chart; and the nearest other stations. |
| `list_charts` | The charts the site draws and what each one shows. |

A chart is returned as a link to its page, not as an image file. The page draws the chart and offers it as SVG, PDF or PNG.

The catalogue holds about 16,000 stations with typical-year weather files (EPW) from [climate.onebuilding.org](https://climate.onebuilding.org/) and the [EnergyPlus weather library](https://energyplus.net/weather).

## Connect a coding agent

=== "Claude Code"

    ```bash
    claude mcp add --transport http eddy3d-climate https://climate.eddy3d.com/mcp
    ```

    Add `--scope user` to have it in every project.

=== "Codex CLI"

    ```bash
    codex mcp add eddy3d-climate --url https://climate.eddy3d.com/mcp
    ```

    Or in `~/.codex/config.toml`:

    ```toml
    [mcp_servers.eddy3d-climate]
    url = "https://climate.eddy3d.com/mcp"
    ```

=== "Gemini CLI"

    ```bash
    gemini mcp add --transport http eddy3d-climate https://climate.eddy3d.com/mcp
    ```

    Or in `~/.gemini/settings.json`:

    ```json
    { "mcpServers": { "eddy3d-climate": { "httpUrl": "https://climate.eddy3d.com/mcp" } } }
    ```

=== "Cursor"

    In `.cursor/mcp.json` in a project, or `~/.cursor/mcp.json` for every project:

    ```json
    { "mcpServers": { "eddy3d-climate": { "url": "https://climate.eddy3d.com/mcp" } } }
    ```

=== "VS Code (Copilot)"

    In `.vscode/mcp.json`:

    ```json
    { "servers": { "eddy3d-climate": { "type": "http", "url": "https://climate.eddy3d.com/mcp" } } }
    ```

    Or from the Command Palette: **Chat: Open Customizations** → **MCP Servers** → **+** → **HTTP**, then enter the address.

=== "Antigravity"

    In `~/.gemini/config/mcp_config.json`, or `.agents/mcp_config.json` in a workspace:

    ```json
    { "mcpServers": { "eddy3d-climate": { "serverUrl": "https://climate.eddy3d.com/mcp" } } }
    ```

## Connect a chat app

=== "Claude"

    1. Open **Customize** → **Connectors**.
    2. Select **+ Add** → **Add custom connector**.
    3. Enter the address `https://climate.eddy3d.com/mcp`.

    On Team and Enterprise plans an owner adds it under **Organization settings** → **Connectors**.

=== "ChatGPT"

    1. On the web, open **Plugins**, select the plus button and choose **Add custom MCP server**.
    2. Enter a name and the address `https://climate.eddy3d.com/mcp`.
    3. Choose **No authentication**, accept the notice and create it.

    Type `@` in a chat to use it.

=== "Le Chat"

    1. Open the **Connectors** page and select **+ Add Connector**.
    2. Switch to **Custom MCP Connector**.
    3. Enter a name without spaces and the address `https://climate.eddy3d.com/mcp`, then **Connect**.

## Use it from an API

=== "Claude API"

    Send the beta header `anthropic-beta: mcp-client-2025-11-20` and add to the request:

    ```json
    "mcp_servers": [{ "type": "url", "url": "https://climate.eddy3d.com/mcp", "name": "eddy3d-climate" }],
    "tools": [{ "type": "mcp_toolset", "mcp_server_name": "eddy3d-climate" }]
    ```

=== "OpenAI Responses API"

    ```json
    "tools": [{
      "type": "mcp",
      "server_label": "eddy3d-climate",
      "server_url": "https://climate.eddy3d.com/mcp",
      "require_approval": "never"
    }]
    ```

=== "xAI API"

    ```json
    "tools": [{ "type": "mcp", "server_label": "eddy3d-climate", "server_url": "https://climate.eddy3d.com/mcp" }]
    ```

Any other MCP client that connects to a server over HTTP takes the same address.

!!! note "These steps follow each vendor's documentation as of November 2026"
    Menu names and file locations change. If a step no longer matches, look for "MCP" or "connectors" in that product's settings and use the address above.

## Without MCP

The site also answers in Markdown. A request with the header `Accept: text/markdown` to `https://climate.eddy3d.com/` or to a station page such as `https://climate.eddy3d.com/station/DEU_BY_Furth.107620` returns the same facts and links as text.

Station pages are listed in [`https://climate.eddy3d.com/sitemap.xml`](https://climate.eddy3d.com/sitemap.xml).
