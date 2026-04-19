---
name: composition-patterns
description: Advanced React composition patterns to build flexible and maintainable components. Avoid "prop drilling" and "prop proliferation" by using Compound Components, Inversion of Control, and React 19 APIs.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Local file modification only"
  triggers:
    - "react composition"
    - "compound components"
    - "component architecture"
    - "refactor component props"
    - "react 19 ref"
---

# React Composition Patterns

## Core Principles
- **Favor Composition over Props**: Don't use booleans (e.g., `showIcon`, `isSmall`) to control internal UI. Pass the UI as children or slots.
- **Inversion of Control**: Let the consumer decide the structure by providing sub-components.

## 1. Compound Components
Use shared context to link sub-components together. This is the standard for complex UI like Tabs, Selects, and Modals.
```tsx
<Select>
  <Select.Trigger />
  <Select.Content>
    <Select.Item value="1">Option 1</Select.Item>
  </Select.Content>
</Select>
```

## 2. Slots Pattern
Instead of `renderLeftIcon`, `renderRightIcon`, use explicit slots.
```tsx
function Button({ leftSlot, children, rightSlot }: Props) {
  return (
    <button>
      {leftSlot}
      {children}
      {rightSlot}
    </button>
  );
}
```

## 3. React 19 Patterns (Next.js 15+)
- **No more `forwardRef`**: In React 19, `ref` is passed as a normal prop.
- **Use `use()` instead of `useContext()`**: `use(Context)` can be called conditionally or in loops (unlike hooks).

## 4. Avoiding Prop Proliferation
- **Problem**: A component with 20+ props, mostly booleans.
- **Solution**: Break it down into smaller, composable pieces. If a component does too much, it's hard to test and maintain.

## Gotchas
- **Context Overuse**: Don't use context for everything. Only use it for truly shared state within a compound component.
- **Performance**: High-frequency state in a provider will re-render all consumers. Split contexts if necessary.

## Verification Checklist
- [ ] No boolean props used for internal UI that could be passed as children.
- [ ] Compound components use a stable context provider.
- [ ] `ref` is passed as a normal prop (if using React 19).
- [ ] Component API is intuitive and follows the "Slot" or "Compound" pattern.
