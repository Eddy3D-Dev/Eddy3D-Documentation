# auth.md: docs.eddy3d.com

**Audience:** AI agents and automated clients.

**No authentication.** This is the public documentation of Eddy3D: component reference, tutorials, methods and release notes. It
needs no account, key or token, and it has no API of its own. There is no registration or provisioning endpoint and no OAuth server,
so there is no protected-resource or authorization-server metadata to publish.

## How to use it

- Send plain `GET` requests. Honour [`/robots.txt`](https://docs.eddy3d.com/robots.txt) and its content signals, and identify yourself
  with a descriptive `User-Agent`.
- The current documentation is under `/latest/`; every release is also kept under its own version number. The sitemap is
  [`/sitemap.xml`](https://docs.eddy3d.com/sitemap.xml).
- The one public data API of the project, the AIJ wind-benchmark data, is at <https://aij.eddy3d.com/api/> and needs no credentials
  either; it is listed in [`/.well-known/api-catalog`](https://docs.eddy3d.com/.well-known/api-catalog).

## Contact

<https://github.com/Eddy3D-Dev/Eddy3D-Documentation/issues>
