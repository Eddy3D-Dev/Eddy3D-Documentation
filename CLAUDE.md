# CLAUDE.md

Documentation site for Eddy3D (MkDocs). Rendered docs live at https://docs.eddy3d.com/.

## Branch model — read before pushing

- **`dev` is the working branch**: land all changes here directly (no gated PRs between
  feature branches and dev needed).
- **`main` is the published branch and it is protected**: direct pushes are rejected
  (GH013 "Changes must be made through a pull request"). Nothing you push to `dev` is
  visible on the live site until a `dev → main` PR is merged.
- Publishing flow: push `dev` → `gh pr create --base main --head dev` → `gh pr merge --merge`.

## Release coupling

On every Eddy3D plugin release (see the main repo's `.claude/skills/release-eddy3d/SKILL.md`):

- `mkdocs.yml` → `latest_eddy_version` pin.
- `docs/components/Select_Template.md` → `Version:` line.
- Then the `dev → main` PR — the release is not done until it merges.

Component pages under `docs/components/` are regenerated from the plugin
(`tools/export_components.py` in this repo); hand-edits to generated pages get
overwritten on the next export.
