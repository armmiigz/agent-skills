# Tailwind v4 & shadcn/ui Mapping

Tailwind v4 introduces a CSS-first configuration. This document explains how to map your brand tokens to the theme.

## 1. The `@theme` Block
Instead of `tailwind.config.js`, define your theme directly in your CSS (e.g., `src/index.css`).

```css
@import "tailwindcss";

@theme {
  /* Brand Colors in OKLCH */
  --color-primary: oklch(0.6 0.25 240);
  --color-secondary: oklch(0.7 0.15 180);
  --color-accent: oklch(0.8 0.2 300);
  
  /* Semantic Colors for shadcn/ui */
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-muted: var(--muted);
  --color-destructive: var(--destructive);
  
  /* Radii */
  --radius-xl: 1rem;
  --radius-lg: var(--radius);
  --radius-md: calc(var(--radius) - 2px);
  --radius-sm: calc(var(--radius) - 4px);
}
```

## 2. shadcn/ui Variables
Map the CSS variables that shadcn/ui components expect. Use `oklch()` for modern browsers.

```css
:root {
  --background: oklch(1 0 0);
  --foreground: oklch(0.1 0.02 240);
  
  --primary: oklch(0.6 0.25 240);
  --primary-foreground: oklch(0.98 0.01 240);
  
  --muted: oklch(0.96 0.01 240);
  --muted-foreground: oklch(0.45 0.02 240);
  
  --accent: oklch(0.96 0.01 240);
  --accent-foreground: oklch(0.1 0.02 240);
  
  --destructive: oklch(0.6 0.2 20);
  --destructive-foreground: oklch(0.98 0.01 20);
  
  --border: oklch(0.9 0.01 240);
  --input: oklch(0.9 0.01 240);
  --ring: oklch(0.6 0.25 240);
  
  --radius: 0.5rem;
}

.dark {
  --background: oklch(0.1 0.02 240);
  --foreground: oklch(0.98 0.01 240);
  /* Add other dark mode overrides here */
}
```

## 3. Legacy HSL Compatibility
Many existing shadcn/ui components use the `hsl(var(--primary))` pattern in their source code.

> [!WARNING]
> If your project uses components with internal `hsl()` wrappers, providing a raw `oklch()` value in the CSS variable will break the rendering.

### Recommendation
1.  **Detect**: Check existing `components/ui` files for the `hsl(var(...))` pattern.
2.  **Recommend**: If detected, recommend converting your brand OKLCH values to **HSL format** before populating the variables.
3.  **Conversion**: Use external tools (e.g., [oklch.com](https://oklch.com)) to get the accurate HSL equivalents for your brand tokens.

## 4. Deployment Considerations
- **Vite Integration**: Ensure `@tailwindcss/vite` is used.
- **PostCSS**: v4 handles naming and nesting internally.
