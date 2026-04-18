---
name: view-transitions
description: Implement smooth, native-feeling animations using React's View Transition API and Next.js 15+ experimental features. Covers shared element transitions, directional navigation, and CSS recipes.
metadata:
  version: "1.0"
  triggers:
    - "view transitions"
    - "page transitions next.js"
    - "shared element transition"
    - "animate route change"
    - "react view transition"
---

# View Transitions (Next.js 15+)

## Setup (Next.js 15+)
Enable the experimental flag in `next.config.js`:
```js
// next.config.js
experimental: {
  viewTransition: true
}
```

## Core Components
### 1. `<ViewTransition>`
Wrap your elements or pages to enable transitions.
- **Enter/Exit**: Animates when the component mounts or unmounts.
- **Update**: Animates when the component's state changes.
- **Share**: Used for "Shared Element Transitions" (morphing an element from one page to another).

### 2. Shared Element Transitions
To morph an element (e.g., an image) across routes, give them the same `name` on both pages.
```tsx
// Page A
<ViewTransition name="hero-image">
  <img src="..." />
</ViewTransition>

// Page B
<ViewTransition name="hero-image">
  <img src="..." />
</ViewTransition>
```

## CSS Recipes
The browser uses pseudo-elements for transitions:
- `::view-transition-old(*)`: The snapshot of the "before" state.
- `::view-transition-new(*)`: The live view of the "after" state.

### Fade Transition
```css
::view-transition-old(root) {
  animation: fade-out 0.3s ease-in-out;
}
::view-transition-new(root) {
  animation: fade-in 0.3s ease-in-out;
}
```

## Next.js Specific Patterns
- **Directional Transitions**: Use `transitionTypes` on `next/link` (if available) or `addTransitionType` in a Client Component.
- **Loading Boundaries**: Wrap skeletons in `loading.tsx` with `<ViewTransition>` for smooth skeleton-to-content reveals.
- **Reduced Motion**: Always respect user settings.
```css
@media (prefers-reduced-motion: reduce) {
  ::view-transition-old(*), ::view-transition-new(*) {
    animation: none !important;
  }
}
```

## Gotchas
- **Text Morphing**: Direct scaling of text snapshots can look blurry. Use `object-fit: none` or specific text-morphing techniques.
- **Nested Transitions**: Avoid nesting `<ViewTransition>` components as they might conflict.
- **Z-Index**: `::view-transition-group` creates a new stacking context. Use `z-index` on the pseudo-elements if needed.

## Verification Checklist
- [ ] `experimental.viewTransition` is enabled in `next.config.js`.
- [ ] Shared elements have unique and matching `name` props.
- [ ] `prefers-reduced-motion` is handled in CSS.
- [ ] Transition duration is fast (typical < 300ms) to avoid blocking user interaction.
