#!/bin/bash

# Double-click on macOS to serve the Eddy3D documentation locally via Docker.

# Move to the folder this script is in (so double-clicking works from anywhere).
cd "$(dirname "$0")" || exit 1

# First, build the image.
echo "Building the docs image..."
docker build -t custom-mkdocs-material .

# Then serve it. Live-reloads as you edit (the repo is mounted into the container).
echo ""
echo "Serving the docs at http://localhost:8080  (press Ctrl+C to stop)"
echo ""
docker run --rm -it \
  -p 8080:8000 \
  -v "$(pwd)":/docs \
  custom-mkdocs-material \
  serve -a 0.0.0.0:8000 -c --watch docs
