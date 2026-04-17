---
name: ui-foundations
description: Use this skill to design brand foundations including OKLCH color palettes and typographic systems. Trigger this WHENEVER the user mentions brand identity, design tokens, color variables, or font setup. It MUST be the source of truth for all UI design tokens.
license: MIT
compatibility: Designed for any Agent Skills-compliant client (e.g. Claude Code)
metadata:
  version: "1.3"
  triggers:
    - "design design system"
    - "ui foundations"
    - "generate color palette"
    - "setup tailwind 4 theme"
    - "brand identity"
    - "typography scale"
    - "font configuration"
    - "color variables"
    - "brand tokens"
    - "design foundations"
---

# UI Foundations Skill

This skill provides a systematic approach to designing brand identities and implementing them technically using the **Tailwind CSS v4** engine. It focuses on modern color theory (OKLCH), accessible typography, and seamless integration with **shadcn/ui**.

## Core Principles
1. **OKLCH First**: Use `oklch()` for perceptually uniform colors and better range.
2. **Modern Theming**: Leverage Tailwind v4's `@theme` CSS layer for performance and portability.
3. **Accessibility**: Ensure contrast ratios and legibility are part of the design process.

## Workflow
Progress:
- [ ] **Identity**: Define brand personality, primary colors, and font preferences.
- [ ] **Generation**: Produce a harmonious palette and topographic hierarchy.
- [ ] **Implementation**: Generate the CSS `@theme` block for `index.css`.
- [ ] **Handoff**: Transfer tokens to the `shadcn-ui` skill for implementation.

## Gotchas
- **Browser Support**: OKLCH is widely supported in modern browsers, but ensure fallbacks (HSL/RGB) are provided if targeting legacy environments.
- **Luminance Sensitivity**: Small changes in Lightness (L) in OKLCH can significantly impact accessibility. Always verify contrast ratios with a tool.
- **Thai Typography**: When designing for Multi-language (Thai) support, ensure line-heights are generous enough to prevent vowel clipping.
- **Tailwind v4 Layering**: Tokens must be defined within the `@theme` block to be picked up by Tailwind v4's utility generator.

## Reference Documentation
For detailed design logic and technical specs:
- [Tailwind v4 & shadcn/ui Mapping](./references/tailwind-v4.md)
- [OKLCH Palette Generator](./references/palette-generator.md)
- [Typography & Font Integration](./references/typography.md)

## Success Criteria
- Colors are defined in `oklch()` with proper fallback strategies.
- Typography scales are defined using Tailwind v4 fluid scaling or standard steps.
- The resulting design maps correctly to shadcn/ui CSS variables (e.g., `--primary`, `--accent`).

## Skill Handoff
Once the brand identity and design tokens are finalized:
1.  **Reference the Handoff**: Explicitly state that the design phase is complete.
2.  **Transition**: Instruct the user or sub-agent to invoke the `shadcn-ui` skill for technical project initialization and component installation.
3.  **Transfer Tokens**: Provide the generated `@theme` and `:root` blocks to the next phase as the "Source of Truth".

