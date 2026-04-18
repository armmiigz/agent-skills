---
name: shadcn-ui
description: Manage shadcn/ui components with Tailwind v4. Focuses on ownership, customization, and accessible UI patterns.
metadata:
  version: "2.0"
  triggers:
    - "add shadcn component"
    - "customize shadcn"
    - "setup shadcn with tailwind 4"
---

# shadcn/ui (Tailwind v4)

## Core Principles
1. **Ownership**: You own the code in `components/ui`. Modify it to fit your brand.
2. **Composition**: Build complex features by composing small, reusable UI primitives.
3. **Accessibility**: Leverage Radix UI primitives for keyboard navigation and screen reader support.

## Integration with Tailwind v4
Tailwind v4 uses CSS variables for theming. Ensure your `globals.css` maps variables correctly:

```css
@theme {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-primary: var(--primary);
  /* ... etc */
}

:root {
  --background: oklch(100% 0 0);
  --primary: oklch(60% 0.15 250);
}
```

## Workflow
- **Init**: `npx shadcn@latest init` (Select Tailwind v4 option).
- **Add**: `npx shadcn@latest add <component>` to get the source code.
- **Customization**: Change the JSX/TSX in `components/ui` directly. Avoid adding logic; keep it presentational.

## Best Practices
- **CN Utility**: Always use the `cn()` utility for merging classes and handling conditional styles.
- **Polymorphism**: Use the `asChild` prop from Radix primitives to maintain semantic HTML.
- **Client Components**: Wrap interactive UI (Dialog, Sheet, Tabs) in `'use client'` if using Next.js App Router.

## Success Criteria
- Components are installed in `src/components/ui`.
- Theming is handled via CSS variables in `@theme`.
- Zero hydration errors in Next.js.

