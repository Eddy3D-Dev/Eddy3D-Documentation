"""Rewrite root-absolute asset references to page-relative ones.

The nav in mkdocs.yml carries a component icon per entry as raw HTML with a
root-absolute src (``<img src='/images/icons/Foo.png' …>``), written there by
patch_nav.py. That works only while the site is served from the domain root.

Under mike the site moves into a per-version prefix — docs.eddy3d.com/latest/…
and docs.eddy3d.com/1.9.0.827/… — so ``/images/icons/Foo.png`` resolves to the
DOMAIN root, where nothing lives, and every sidebar icon 404s. 185 references
across 94 pages were affected when versioning was introduced.

Rewriting the nav by hand would fix the symptom for one release and reintroduce
it the next time patch_nav.py runs. This hook instead normalises at build time:
every root-absolute reference into images/ or assets/ becomes relative to the
page that carries it, which is correct at any prefix, versioned or not.
"""

import re

# Matches src="/images/…", href='/assets/…' AND the unquoted src=/images/… form.
# The unquoted case is not hypothetical: mkdocs-minify-plugin strips attribute
# quotes, and depending on event order this hook can see the minified output — a
# quotes-only pattern silently rewrites nothing while appearing to work.
_ABSOLUTE_ASSET = re.compile(
    r"""(src|href)=(?:(?P<q>["'])/(?P<qpath>(?:images|assets)/[^"']*)(?P=q)"""
    r"""|/(?P<upath>(?:images|assets)/[^\s>"']*))"""
)


def _prefix_for(page) -> str:
    """`../` repeated once per path segment of the page's URL."""
    depth = len([part for part in page.url.split("/") if part])
    return "../" * depth


def on_post_page(output: str, page, config) -> str:
    prefix = _prefix_for(page)

    def replace(match: "re.Match[str]") -> str:
        attr = match.group(1)
        quote = match.group("q")
        path = match.group("qpath") if quote else match.group("upath")
        if quote:
            return f"{attr}={quote}{prefix}{path}{quote}"
        return f"{attr}={prefix}{path}"

    return _ABSOLUTE_ASSET.sub(replace, output)
