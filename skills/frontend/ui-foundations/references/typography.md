# Typography & Font Integration

A strong typographic system defines the scale, weight, and hierarchy of your brand.

## 1. Type Scales
Tailwind v4 provides standard scales, but you can define custom brand scales using CSS variables.

```css
@theme {
  /* Fluid Scaling Example */
  --font-size-hero: clamp(2rem, 5vw, 4rem);
  
  /* Brand Scales */
  --font-size-display: 3.5rem;
  --font-size-heading: 2rem;
  --font-size-body: 1rem;
}
```

## 2. Custom Font Integration
To integrate a brand font (e.g., from Google Fonts or local assets):

### CSS Import
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

@theme {
  --font-sans: "Inter", ui-sans-serif, system-ui;
  --font-display: "Clash Display", var(--font-sans);
}
```

## 3. Typographic Hierarchy for UI
Ensure clear distinction between semantic levels.

### Base Styles
```css
@layer base {
  h1 { @apply text-4xl font-bold tracking-tight; }
  h2 { @apply text-2xl font-semibold; }
  p { @apply text-base text-muted-foreground leading-relaxed; }
}
```

## 4. Multi-language Typography

When designing for global audiences, ensure your typography remains legible and harmonious across different scripts.

### Thai Typography (Case Study)
Thai script has no word spaces and uses diacritical marks above and below the baseline. This requires specific adjustments:

- **Line Height**: Standard Latin line-height (1.2-1.5) often clips Thai tonal marks. Use at least `1.8` for body text.
- **Font Pairing**: Match the personality of the Latin and Thai fonts.
    - **Modern/Clean**: Pair *Inter* (Latin) with *Kanit* or *Sukhumvit Set* (Thai).
    - **Academic/Formal**: Pair *Times New Roman* or *Merriweather* (Latin) with *Sarabun* (Thai).
- **Legibility**: Ensure the "Bor-height" of Thai consonants aligns visually with the x-height of Latin characters.

### Multi-language Theme Config (Tailwind v4)
Use specific font stacks to ensure global support.

```css
@theme {
  /* Global Sans-Serif Stack */
  --font-sans: "Inter", "Kanit", "Sarabun", ui-sans-serif, system-ui;
  
  /* Applying specific fonts for Thai language blocks */
  --font-thai: "Sarabun", var(--font-sans);
}

/* Technical implementation for Thai blocks */
[lang="th"] {
  font-family: var(--font-thai);
  line-height: 1.8;
}
```

### UI Component Alignment
Thai characters (especially those with tonal marks like `่ ้ ๊ ๋`) require more vertical space than Latin characters. This can cause "bottom-clipping" or "top-clipping" in tight UI elements.

- **Buttons & Badges**: Use `padding-bottom` offsets to visually center Thai text.
- **Leading**: Avoid `leading-none` for Thai; use `leading-normal` or `leading-relaxed`.

```css
/* Utility for Thai-centered buttons */
@utility th-btn {
  padding-top: 0.25rem;
  padding-bottom: 0.4rem; /* Extra bottom padding for Thai diacritics */
  line-height: 1.2;
}

/* Base adjustment for global components */
.th button, .th .badge {
  @apply th-btn;
}
```

## 5. Performance & Performance Checklist
- **Font Display**: Always use `font-display: swap`.
- **Subsetting**: Only load the specific character sets (Latin, Thai) you need.
- **Variable Fonts**: Prefer variable fonts (Woff2) to reduce bundle size.
