# Skill Development Standards

This document defines the requirements for high-quality, documentation-centric skills.

## 1. Anatomy of a Skill
Every skill must be self-contained in its own directory:

```
skills/skill-name/
├── SKILL.md (Required) - Level 2 logic & triggers
├── references/ (Required) - Level 3 deep-dive docs
├── scripts/ (Optional) - Automation and deterministic tasks
└── assets/ (Optional) - Static files like templates or icons
```

## 2. Progressive Disclosure
Skills are loaded in layers to optimize context windows:

- **Level 1: Metadata**: The name and description in `SKILL.md` frontmatter. Used by the agent for triggering.
- **Level 2: Instructions**: The body of `SKILL.md`. Contains high-level workflow and core logic.
- **Level 3: References**: Modular files in `references/`. Loaded only when a deep dive is needed.

## 3. Writing Patterns
- **Imperative Form**: Use "Do X", "Create Y", "Verify Z".
- **Trigger Clarity**: Descriptions should specify *exactly* when to use the skill and what it enables.
- **Relative Paths**: ALL internal links must use relative paths (e.g., `./references/doc.md`) to ensure the skill folder is portable.
- **English Only**: Maintain all documentation in English for maximum agent reliability.

## 4. Output Examples
Use the "Input/Output" pattern for clarity:
```markdown
**Example:**
Input: "Convert this palette to HSL"
Output: `--primary: hsl(240 100% 50%)`
```

## 5. Description Guidelines
- Avoid vague descriptions like "Helps with UI".
- Prefer specific ones: "Generates Tailwind v4 palettes using OKLCH. Use this skill when the user mentions brand colors, design tokens, or theme configuration."
