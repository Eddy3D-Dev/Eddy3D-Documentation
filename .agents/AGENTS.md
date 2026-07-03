# Eddy3D-Documentation — Agent Rules

## Architecture

The documentation site is built with **MkDocs**. All component documentation
(`.md` files under `docs/components/`, category pages under `docs/categories/`,
component images, icons, and nav YAML) is **machine-generated** by:

    tools/export_components.py

This script runs inside **Grasshopper** (Rhino 8, CPython 3) and is the
**single source of truth** for all generated content. It reads live component
metadata from the loaded Eddy3D plugin and writes markdown, images, icons,
category pages, and the nav YAML.

### What this means for you

- **NEVER** edit files under `docs/components/`, `docs/categories/`,
  `docs/images/components/`, `docs/images/icons/`, or `docs/components_nav.yml`
  directly. Any manual edits will be overwritten the next time the user runs the
  export from Grasshopper.
- **ALWAYS** edit `tools/export_components.py` to change generated output.
  The user will re-run it from Grasshopper to regenerate everything.

## Repository layout

```
Eddy3D-Documentation/          ← this repo
├── mkdocs.yml                 ← MkDocs config (hand-edited, NOT generated)
├── tools/
│   └── export_components.py   ← THE generator script (source of truth)
└── docs/
    ├── components/            ← generated .md per component
    ├── categories/            ← generated .md per category
    ├── components_nav.yml     ← generated nav block
    └── images/
        ├── components/        ← generated screenshots (.png + -crop.png)
        └── icons/             ← generated 24×24 icons
```

## Sibling repos (same parent directory)

| Directory name         | Contents                                      |
|------------------------|-----------------------------------------------|
| `Eddy3D`               | C# plugin source (`.cs` files, CMP components) |
| `Eddy3D-Website`       | Marketing website                              |

The generator resolves sibling repos by walking up from the `.gh` file location.

## Script conventions

- `USE_CROPPED_IMAGES = True` — the markdown references `{name}-crop.png`.
  The script auto-crops screenshots and saves both raw and cropped versions.
- `DISABLE_SOLVER = True` — disables the GH solver during export to prevent
  downstream components from firing.
- Source code links are resolved dynamically by scanning `.cs` files in the
  sibling `Eddy3D` repo for `class ClassName` declarations. No hardcoded
  dictionaries or mappings.
- The script must be **platform and user independent** — no hardcoded absolute
  paths. Path resolution uses `os.path.expanduser("~")` and directory traversal.

## Rules

1. Do not hardcode source code links.
2. Do not hardcode user-specific or platform-specific paths.
3. `Version X.X.X.XXX` must be stripped from all component descriptions.
4. For the "Wind Speed (V)" param-naming pattern, only change documentation —
   do not touch the plugin C# source.
5. Component headings use `#` (h1) so MkDocs does not generate a redundant
   page title from the nav.
