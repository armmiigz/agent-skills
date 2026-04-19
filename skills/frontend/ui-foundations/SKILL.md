---
name: ui-foundations
description: Design brand foundations with OKLCH colors and Tailwind CSS v4. Use for theme configuration, typography scales, and design tokens.
metadata:
  security_assessment:
    - "Risk: Low"
    - "Permissions: Local file modification only"

  version: "2.0"
  triggers:
    - "setup tailwind 4"
    - "oklch colors"
    - "design system tokens"
    - "typography setup"
---

# UI Foundations (Tailwind v4)

## Design System Principles

### 1. OKLCH Color Space
Use `oklch()` for consistent luminance and better color ranges.
```css
@theme {
  --color-primary: oklch(60% 0.15 250);
  --color-accent: oklch(75% 0.12 150);
}
```

### 2. Fluid Typography
Define typography scales using modular steps or fluid scaling.
```css
@theme {
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
}
```

### 3. Tailwind v4 Architecture
- **CSS-Only Config**: Everything goes into your main CSS file within the `@theme` block.
- **Zero Config**: No more `tailwind.config.js` unless necessary for legacy plugins.

## Implementation Steps
1.  **Define Palette**: Generate 50-950 scales using OKLCH.
2.  **Setup CSS**: Populate `@theme` in `globals.css` or `index.css`.
3.  **Map to shadcn**: Connect CSS variables to shadcn/ui tokens (e.g., `--primary`, `--background`).

## Best Practices
- **Contrast**: Use `oklch` L-value to target WCAG accessibility targets (e.g., L > 70% for dark text, L < 40% for light text).
- **Responsive**: Use `clamp()` for fluid spacing and font-sizes.
- **Micro-animations**: Use CSS variables for consistent transition timings.


