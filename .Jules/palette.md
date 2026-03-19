## 2024-03-01 - Add `title` to Loom iframes
**Learning:** Embedded Loom iframes within documentation were missing `title` attributes. Screen readers rely on these attributes to describe the content of the iframe to users.
**Action:** Always verify `<iframe>` and other embedded objects have descriptive `title` attributes that explain the content (e.g., "Loom video: Install UMCF Plugin") to improve accessibility.

## 2025-03-17 - Add `title` to Vimeo iframes and `alt` to Markdown images
**Learning:** Some Markdown images `![]()` and embedded Vimeo iframes (`<iframe title="vimeo-player">`) within the documentation were missing descriptive alt texts and specific titles. Screen readers rely on these attributes to describe the content of the images and iframes to users.
**Action:** Always verify `<iframe>` and other embedded objects have descriptive `title` attributes that explain the content (e.g., "Video tutorial: Simple wind analysis") and ensure that all Markdown images `![Alt text](url)` include descriptive alternative text to improve accessibility.

## 2025-03-18 - Generic Link Text Needs Context
**Learning:** Common navigation patterns like "Learn more" or "Read more" within grid cards lack context for screen readers when separated from the surrounding text visually. The `attr_list` markdown extension allows adding ARIA attributes to standard Markdown links.
**Action:** When creating repetitive "Learn more" links in documentation navigation cards, always append `{ aria-label="..." }` using the `attr_list` extension to provide specific destination context for accessibility tools.
## 2024-05-14 - Meaningful links

**Learning:** Ambiguous link texts like 'Download', 'here', and 'Installation guide' lack context for screen reader users and those navigating out of context. The `attr_list` Markdown extension provides a clean way to add `aria-label` attributes to these links in MkDocs without rewriting the visible text, maintaining visual design while greatly improving accessibility.
**Action:** Always scan documentation files for ambiguous links (e.g., 'click here', 'download') and append explicit `aria-label`s using the `{ aria-label="..." }` syntax.
