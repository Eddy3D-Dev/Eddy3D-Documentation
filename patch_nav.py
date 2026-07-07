import re

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
