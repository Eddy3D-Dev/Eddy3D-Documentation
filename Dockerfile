FROM squidfunk/mkdocs-material

   # Install additional Python packages
   RUN apk add --no-cache bash && \
      pip install \
      mkdocs-material \
      mkdocs-multirepo-plugin \
      mkdocs-git-revision-date-localized-plugin \
      mkdocs-minify-plugin \
      mkdocs-git-authors-plugin \
      mkdocs-git-committers-plugin-2 \
      mkdocs-title-casing-plugin \
      mkdocs-glightbox \
      markdown-include \
      mkdocs-redirects \
      mkdocs-video \
      mkdocs-awesome-pages-plugin \
       

   # You can add more RUN pip install commands for other packages