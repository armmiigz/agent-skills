---
name: nextjs
description: Production-grade Next.js 15+ patterns. Covers App Router, Server Actions, "use cache", and Async Request APIs. Use for building performant full-stack apps.
metadata:
  version: "1.0"
  triggers:
    - "setup next.js"
    - "server components"
    - "server actions"
    - "next.js caching"
    - "app router"
---

# Next.js 15+ Ultimate Guide

## Core Principles
1. **Server-First**: Default to Server Components (RSC) to minimize client-side bundle size.
2. **Streaming & Suspense**: Use Suspense boundaries for non-blocking data fetching.
3. **Type Safety**: Leverage TypeScript for end-to-end safety from DB to UI.

## RSC Boundaries (Next.js 15+)
- **Invalid Patterns**: Do not use async client components. Client components MUST NOT receive non-serializable props (e.g., Functions, Promises) unless they are Server Actions.
- **Data Fetching**: Prefer fetching in Server Components. For client fetching, use `SWR` or `React Query`.

## Async APIs (Next.js 15+ BREAKING)
The following APIs are now asynchronous. You MUST `await` them:
- `params` and `searchParams` in Page/Layout props.
- `cookies()` and `headers()`.
```tsx
// Correct usage in Page
export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const cookieStore = await cookies();
  // ...
}
```

## Directives & Caching
- `'use client'`: Entry point for interactivity/hooks.
- `'use server'`: Mark functions as Server Actions.
- `'use cache'` (Experimental/Next.js 16): Opt-in to the new caching model.
- **Partial Prerendering (PPR)**: Wrap dynamic components in `Suspense` to allow static shell generation.

## Data Patterns & Waterfalls
- **Avoid Waterfalls**: Use `Promise.all()` for independent fetches.
- **Preloading**: Use the `preload` pattern or `React.cache()` to deduplicate fetches across the component tree.
- **Optimistic UI**: Use `useOptimistic` for instant feedback during Server Actions.

## UI & Optimization
- **Images**: Always use `next/image`. Configure `sizes` for responsiveness.
- **Fonts**: Use `next/font` with Tailwind CSS integration.
- **Navigation**: Prefer `Link` over `router.push` for prefetching.

## Gotchas
- **Hydration Errors**: Caused by using browser APIs (window, localStorage) directly in render or mismatched date formats. Fix using `useEffect` or `dynamic(() => ..., { ssr: false })`.
- **Search Params Bailout**: Using `searchParams` or `useSearchParams` will force the page into dynamic rendering. Wrap in `Suspense`.

## Verification Checklist
- [ ] All `params`, `searchParams`, `cookies()`, and `headers()` are awaited.
- [ ] Client components are minimized and at the leaves of the tree.
- [ ] No non-serializable props are passed to client components.
- [ ] `Suspense` boundaries are used for slow data fetching.
- [ ] Images have appropriate `alt` tags and `priority` for LCP.
