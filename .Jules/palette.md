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

## 2024-05-15 - Context for acronyms in image alt text

**Learning:** When images contain partner logos or acronyms (e.g., "PW" for Perkins&Will, "ETH"), using just the acronym in the alt text isn't sufficiently descriptive for screen readers. Expanding these to their full names (e.g., "Perkins&Will logo") provides better context.
**Action:** Always verify that image alt texts clearly describe the image's contents or the organization it represents, avoiding unexpanded acronyms unless they are widely understood. Add ` logo` to the end of logo alt texts.
## 2025-02-18 - Avoid Anti-Patterns in ARIA Labels for Links
**Learning:** Adding `aria-label` to links with poor visible text (like `[here]`) that doesn't contain the visible text is an anti-pattern and violates WCAG 2.5.3 (Label in Name). Screen readers might announce only the `aria-label` and the mismatch can confuse voice dictation users.
**Action:** Always prefer updating the visible text of the link to be descriptive rather than keeping poor link text and attempting to "fix" it with an `aria-label`. If `aria-label` must be used, it must include the visible text.
## 2024-05-24 - Accessibility anti-pattern for raw URL and file name links
**Learning:** Found a pattern where raw URLs or specific file names (e.g., executables) are used as visible link text. While adding an `aria-label` to these links might seem like a good idea to provide descriptive text, it often leads to anti-patterns. If the `aria-label` includes the raw URL to comply with WCAG 2.5.3 (Label in Name), the screen reader user still has to listen to the verbose raw URL. If it doesn't include the raw URL, it violates WCAG 2.5.3. Furthermore, adding redundant text before the `aria-label` (e.g., "- Download: [file.exe]{aria-label='Download file.exe'}") forces screen readers to announce "Download" twice.
**Action:** Always prefer updating the visible text of the link to be descriptive and human-readable (e.g., change `[https://github.com/...]` to `[GitHub repository]`, and `[file.exe]` to `[Download file]`). This is the most robust and accessible approach, avoiding the need for `aria-label` entirely and improving UX for all users.
## 2026-03-25 - Enhance Link Accessibility
**Learning:** Adding descriptive `aria-label`s to external links in Markdown ensures screen readers convey the link's purpose fully, satisfying WCAG 2.5.3. The Material for MkDocs theme supports the `attr_list` extension for this.
**Action:** Append `{ aria-label="Descriptive text" }` to links with less clear or generic text to improve accessibility.

## 2026-03-25 - Refine Link Accessibility
**Learning:** Adding `aria-label` attributes to links that obscure the visible text violates WCAG 2.5.3 (Label in Name), creating a disconnect for speech-recognition and screen reader users. Additionally, adding `aria-label`s to 'fix' links with poor visible text (like 'Download' or 'these instructions') is considered a bad practice.
**Action:** Always prefer updating the visible text of the link to be descriptive and human-readable, avoiding the need for `aria-label` entirely.

## 2026-03-25 - Avoid Aria-label Mismatch for Inline Links
**Learning:** Found a pattern where `aria-label`s were used on inline links to provide completely different, more descriptive text than what was visible (e.g., `[Download](url){ aria-label="Download Windows Installer" }`). This is a severe violation of WCAG 2.5.3 (Label in Name) because screen reader users searching for "Download" may not find it, and speech-recognition users saying "Click Download" might fail.
**Action:** Never use `aria-label` to replace poor link text. Instead, always update the visible text to be descriptive and self-sufficient (e.g., `[Download Windows Installer](url)`).
## 2025-03-29 - [Descriptive Link Text]
**Learning:** Using `aria-label` to fix generic link text (like "Learn more") is an anti-pattern when we can just make the visible text itself descriptive. Descriptive visible text helps all users, not just screen reader users, and avoids WCAG 2.5.3 (Label in Name) violations where the label might not contain the visible text perfectly.
**Action:** Always prefer updating the visible text of a link to be descriptive rather than adding an `aria-label` to generic text.

## 2026-03-25 - Avoid "these instructions" anti-pattern
**Learning:** Using link text like "these instructions for..." creates a poor experience for screen reader users and those navigating out of context. The link text should be fully self-descriptive without needing surrounding context.
**Action:** Always prefer updating the visible text of the link to be descriptive and human-readable (e.g., change `see [these instructions for matching MPI DLL files](...)` to `see the [CFD Online instructions for matching MPI DLL files](...)`).
## 2026-04-02 - Accessible External Links
**Learning:** When changing links to open in a new tab () to keep users in the application context, we MUST communicate this context shift to screen reader users by appending '(opens in a new tab)' to the `aria-label`. Additionally, `rel="noopener noreferrer"` is crucial for security.
**Action:** For all future external links that open in a new tab, include `target="_blank"`, `rel="noopener noreferrer"`, and an `aria-label` warning for screen readers.
## 2026-03-27 - Replace generic link text with specific descriptive visible text
**Learning:** When changing links for accessibility, instead of using 'Learn more' and fixing it via an `aria-label`, updating the visible text itself to be fully descriptive (e.g., 'View Eddy3D Outdoor Documentation') provides a better experience for all users and guarantees WCAG 2.5.3 compliance.
**Action:** Always prefer to update visible text to be self-descriptive instead of relying on `aria-label` attributes to patch generic link text.
## 2026-04-12 - Lazy Loading Large Images
**Learning:** Large GIFs in documentation can cause significant page jank and slow initial load times, negatively impacting the reading experience.
**Action:** Use the MkDocs `attr_list` extension to append `{ loading=lazy }` to heavy media elements like animated GIFs.
