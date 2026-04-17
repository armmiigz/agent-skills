# Installation & Branding Configuration

This document covers the initial setup and branding of a shadcn/ui project.

## 1. Initialization
Run the following command to start the setup:

```bash
npx shadcn@latest init
```

### Configuration Options
During initialization, you will be prompted for:
- **Style**: New York (recommended) or Default.
- **Base Color**: Slate, Gray, Zinc, Neutral, or Stone.
- **CSS Variables**: Yes (allows for easy theming).

## 2. UI Foundations Configuration

### CSS Variables (`globals.css`)
To apply your design system tokens, update the CSS variables in your global CSS file. 

```css
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --primary: 221.2 83.2% 53.3%; /* Your Brand Primary */
  --primary-foreground: 210 40% 98%;
  --radius: 0.5rem; /* Your Brand Border Radius */
}

.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  --primary: 217.2 91.2% 59.8%;
}
```

### Tailwind Config (`tailwind.config.ts`)
Ensure your `tailwind.config.ts` is configured to use these variables. This is usually handled automatically by the CLI, but you can add custom brand colors here:

```typescript
// tailwind.config.ts
export default {
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#f0f9ff",
          // ... 100-900
          500: "hsl(var(--primary))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
}
```

### Components JSON (`components.json`)
This file tracks your configuration. Avoid modifying it manually unless changing the directory structure.

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "app/globals.css",
    "baseColor": "zinc",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  }
}
```

## 3. Adding Components
After initialization, add components as needed:

```bash
npx shadcn@latest add button dialog select
```
