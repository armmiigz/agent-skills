# OKLCH Palette Generator

Using OKLCH allows us to create color palettes that are perceptually uniform (brightness is consistent across different hues).

## 1. OKLCH Parameters
- **L (Lightness)**: 0.0 to 1.0 (0% to 100%)
- **C (Chroma/Intensity)**: 0.0 to 0.4 (Saturation)
- **H (Hue)**: 0 to 360 (Angle on the color wheel)

## 2. Brand Palette Structure

### Primary Color (The Core)
Start with your brand's core hue.
- **Vibrant**: `oklch(0.6 0.25 <hue>)`
- **Pastel**: `oklch(0.9 0.05 <hue>)`
- **Deep**: `oklch(0.3 0.1 <hue>)`

### Secondary & Analogous Colors
Modify the hue (+/- 30-40 degrees) while maintaining similar Lightness and Chroma.
- **Success (Green)**: `oklch(0.7 0.15 140)`
- **Warning (Yellow/Orange)**: `oklch(0.8 0.18 70)`
- **Error (Red)**: `oklch(0.6 0.2 25)`

### Semantic Neutrals
Keep Chroma very low (0.01 - 0.03) to create "tinted neutrals" that feel cohesive with the brand.
- **Background**: `oklch(0.98 0.01 <hue>)`
- **Muted**: `oklch(0.9 0.02 <hue>)`

## 3. Contrast & Accessibility
When generating palettes, always verify the **WCAG 2.1 Contrast Ratio**.
- **Normal Text**: 4.5:1 ratio against background.
- **Large Text**: 3:1 ratio.

### Tools for OKLCH
- [OKLCH.com](https://oklch.com): Visual picker and contrast checker.
- [Colorkit](https://colorkit.io/oklch-color-picker): Palette visualization.

## 4. Example Branding Block
```css
/* Identity: "Electric Ocean" */
--brand-primary: oklch(0.55 0.22 245);
--brand-secondary: oklch(0.65 0.18 200);
--brand-accent: oklch(0.75 0.15 160);
```
