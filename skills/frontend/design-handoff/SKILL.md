---
name: design-handoff
description: Precision UI implementation from design specs. Bridges the gap between Figma/Design and Code, focusing on fidelity, responsiveness, and interaction accuracy.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: File read/write for UI implementation"
  triggers:
    - "implement from figma"
    - "design handoff"
    - "convert design to code"
    - "ui fidelity check"
    - "responsive implementation"
---

# Design Handoff & Implementation

## Core Philosophy
1. **Pixel Perfection**: Match the design's spacing, typography, and colors exactly using [design-system-management](../../frontend/design-system-management/SKILL.md).
2. **Dynamic Fidelity**: Designs are static; code must handle dynamic content, long text, and different screen sizes.
3. **Collaboration**: If a design is impossible or impractical to implement, discuss alternatives with the designer early.

## 1. The Handoff Checklist
- **Tokens**: Are we using the correct design tokens?
- **Assets**: Are images/icons exported in the correct format (SVG for icons)?
- **States**: Does the design cover Hover, Active, Disabled, Loading, and Error states?
- **Responsiveness**: How does the layout change on Mobile, Tablet, and Desktop?

## 2. Implementation Workflow
1. **Inspect**: Analyze the Figma file for layout (Flex/Grid), spacing, and typography.
2. **Deconstruct**: Break the UI into reusable components.
3. **Build Shell**: Create the layout and basic structure.
4. **Style**: Apply Tailwind classes/CSS based on design tokens.
5. **Interactive Layer**: Add animations (Framer Motion) and interactions.

## 3. Interaction & Motion
Refer to [advanced-ui](../../frontend/advanced-ui/SKILL.md) for micro-animations that weren't explicitly designed but enhance the UX.

## Verification Checklist
- [ ] UI matches the design mocks (Fidelity).
- [ ] Layout is responsive (Mobile to Desktop).
- [ ] All interactive states are implemented.
- [ ] Assets are optimized for performance.
- [ ] Code follows [composition-patterns](../../frontend/composition-patterns/SKILL.md).
