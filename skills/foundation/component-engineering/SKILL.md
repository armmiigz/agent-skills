---
name: component-engineering
description: Industrial-grade component development. Covers component scaffolding, Storybook integration for documentation, and custom React hook patterns for reusability.
metadata:
  version: "1.0"
  triggers:
    - "create new component"
    - "setup storybook"
    - "write custom hook"
    - "component scaffolding"
    - "ui documentation"
---

# Component Engineering

## 1. Scaffolding Pattern
Every component should follow a consistent file structure:
```text
Component/
├── index.ts             # Clean export
├── Component.tsx        # Implementation
├── Component.stories.tsx # Storybook docs
├── Component.test.tsx    # Unit tests
└── Component.module.css  # Scoped styles (if needed)
```

## 2. Storybook Documentation
Use Storybook to build components in isolation.
- **Goal**: Document every state (Loading, Error, Empty, Success) of the UI.
- **Controls**: Use ArgTypes to allow interactive testing of component props.

## 3. Custom Hook Standards
Hooks should be used to encapsulate logic, keeping components purely representational (UI).
- **Naming**: Always prefix with `use` (e.g., `useDebounce`).
- **Return Pattern**: Return an object for clarity and future-proofing, unless it's a simple state-pair (like `useState`).

## 4. Reusability Guidelines
- **Open-Closed Principle**: Components should be open for extension (via props/slots) but closed for modification.
- **Prop Drilling**: Avoid drilling more than 2 levels. Use [composition-patterns](../frontend/composition-patterns/SKILL.md) instead.

## Verification Checklist
- [ ] Component follows the standard directory structure.
- [ ] Storybook stories cover all major UI states.
- [ ] Logic is extracted into custom hooks where applicable.
- [ ] Props are strictly typed and documented.
- [ ] Component is accessible (checked via Storybook A11y addon).
