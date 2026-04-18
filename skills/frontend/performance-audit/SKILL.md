---
name: performance-audit-vitals
description: Master Next.js 15+ performance. Focuses on Core Web Vitals (LCP, CLS, INP), Lighthouse 100/100 scores, and advanced optimization techniques (Streaming, PPR, Image optimization).
metadata:
  version: "1.0"
  triggers:
    - "audit performance"
    - "improve lighthouse score"
    - "fix core web vitals"
    - "optimize lcp"
    - "reduce cls"
    - "next.js performance optimization"
---

# Performance Audit & Web Vitals

## Core Metrics (Core Web Vitals)
1. **LCP (Largest Contentful Paint)**: Loading performance. Target: **< 2.5s**.
2. **CLS (Cumulative Layout Shift)**: Visual stability. Target: **< 0.1**.
3. **INP (Interaction to Next Paint)**: Responsiveness. Target: **< 200ms**.

## 1. Optimization Strategies
### Largest Contentful Paint (LCP)
- **Priority Images**: Use `priority` attribute on hero images.
- **Server Streaming**: Use `Suspense` to stream slow data while showing content immediately.
- **PPR (Partial Prerendering)**: Combine static shells with dynamic holes for instant loading.

### Cumulative Layout Shift (CLS)
- **Set Dimensions**: Always provide `width` and `height` for images and videos.
- **Aspect Ratio Boxes**: Use `aspect-ratio` in CSS to reserve space for dynamic content.
- **Font Display**: Use `next/font` with `display: swap` and local fallbacks to prevent layout shifts.

### Interaction to Next Paint (INP)
- **Reduce Main Thread Work**: Move heavy logic to Web Workers or optimize React re-renders.
- **Optimistic UI**: Use `useOptimistic` to show feedback before server confirmation.
- **Debouncing/Throttling**: Limit frequent events (scroll, resize, input).

## 2. Next.js 15 Specifics
- **`use cache`**: Explicitly cache expensive data fetching/computation.
- **Async APIs**: Be mindful of awaiting headers/cookies; use them as late as possible to avoid blocking the initial shell.
- **PPR**: Enable in `next.config.js` for the best balance of speed and freshness.

## 3. Auditing Workflow
1. **Lighthouse (Lab)**: Run in Incognito/Anonymous mode on a Production build.
2. **Search Console (Field)**: Real-user data from the Chrome User Experience Report (CrUX).
3. **Next.js Speed Insights**: Integrated monitoring for real-time vitals tracking.

## 4. Bundle Optimization
- **Dynamic Imports**: Use `next/dynamic` for heavy components (charts, editors) that are not needed immediately.
- **@next/bundle-analyzer**: Regularly check for large libraries and replace them with lighter alternatives (e.g., `date-fns` instead of `moment`).

## Verification Checklist
- [ ] Lighthouse score is 90+ in all categories.
- [ ] Images have `width`/`height` or `aspect-ratio`.
- [ ] Hero images use `priority`.
- [ ] Bundle analyzer shows no "unexpectedly large" dependencies.
- [ ] `Suspense` is used for slow data fetching.
- [ ] No layout shifts during font loading.
