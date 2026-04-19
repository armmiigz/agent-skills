---
name: design-system-management
description: Manage and scale internal design systems. Covers token management (Colors, Typography), component libraries (shadcn/ui), documentation, and versioning for consistency.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: File read/write for UI components"
  triggers:
    - "manage design system"
    - "update design tokens"
    - "component library docs"
    - "scale ui"
    - "design system versioning"
---

# Design System Management

## Core Philosophy
1. **Single Source of Truth**: Design tokens (Tailwind config, CSS variables) must match the Figma source.
2. **Consistency**: Use a small set of reusable components instead of many ad-hoc ones.
3. **Accessibility by Default**: Every component in the design system must be WCAG compliant.

## 1. Token Management
Centralize all design values:
- **Colors**: Use OKLCH for better color management and accessibility.
- **Typography**: Define a clear hierarchy (Scale, Weights, Line-heights).
- **Spacing/Layout**: Use a consistent 4px or 8px grid system.

## 2. Component Library (shadcn/ui)
- **Ownership**: We own the components in `packages/ui` or `src/components/ui`.
- **Customization**: Extend shadcn/ui components with project-specific variants using `class-variance-authority`.
- **Documentation**: Use Storybook or a dedicated `/docs` site to showcase components.

## 3. Governance
- **Review**: Any change to a core component requires review from both Design and Engineering.
- **Deprecation**: Clearly mark and phase out old components to prevent codebase bloat.

## Verification Checklist
- [ ] Tokens match Figma design.
- [ ] Components are reusable and documented.
- [ ] Accessibility standards are met.
- [ ] Naming follows the design system convention.
