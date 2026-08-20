import re

# NOTE: the nav entries this writes carry a ROOT-ABSOLUTE icon path
# (src='/images/icons/…'). That is only correct when the site is served from the
# domain root, which stopped being true when the docs became versioned — mike
# serves them under /latest/ and /<version>/. hooks/relative_paths.py rewrites
# these to page-relative at build time, so this script can keep its current
# output; do not "fix" it here without removing the hook as well.

with open("mkdocs.yml", "r") as f:
    text = f.read()

def repl(m):
    spaces = m.group(1)
    comp_name = m.group(2)
    filename = m.group(3)
    icon_name = filename[:-3]
    
    # Check if already patched
    if "<img" in comp_name:
        return m.group(0)
        
    return f"{spaces}- \"<img src='/images/icons/{icon_name}.png' class='nav-gh-icon' /> {comp_name}\": components/{filename}"

new_text = re.sub(r'^(\s*)-\s*"([^"]+)":\s*components/([^.]+\.md)$', repl, text, flags=re.MULTILINE)

with open("mkdocs.yml", "w") as f:
    f.write(new_text)
