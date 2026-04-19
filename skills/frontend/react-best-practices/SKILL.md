---
name: react-best-practices
description: React performance and architecture best practices from Vercel Engineering. Covers hooks optimization, re-render reduction, bundle size control, and composition patterns.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Local file modification only"
  triggers:
    - "react best practices"
    - "optimize react component"
    - "reduce re-renders"
    - "react component composition"
    - "hooks optimization"
---

# React Best Practices (Vercel Standards)

## Core Priorities
1. **Eliminate Waterfalls**: Start async operations as early as possible.
2. **Minimize Re-renders**: Keep component state local and use memoization wisely.
3. **Optimize Bundles**: Import only what you need; avoid barrel files.

## 1. Async & Performance
- **Parallel Operations**: Use `Promise.all()` for independent sync/async calls.
- **Cheap Checks First**: Validate sync conditions before awaiting remote flags.
- **Defer Await**: Move `await` inside the conditional branch where the data is actually needed.

## 2. Re-render Optimization
- **Functional setState**: Use `setState(prev => prev + 1)` to keep callbacks stable.
- **Primitive Dependencies**: Use primitive values (strings, numbers) in `useEffect` or `useMemo` dependencies rather than objects.
- **Derived State**: Calculate values during render, not in `useEffect`.
- **Memoization**:
  - Use `React.memo` for components with expensive renders.
  - Use `useCallback` for functions passed to memoized children.
  - Use `useMemo` for expensive calculations.

## 3. Component Composition
- **Inversion of Control**: Pass components as props (`children` or slots) to keep logic decoupled.
- **No Inline Components**: Never define a component inside another component's render function (it causes full re-mounts).
- **Stable References**: Hoist static JSX or configuration objects outside the component.

## 4. Bundle Optimization
- **Avoid Barrel Files**: Import directly from `components/UI/Button` instead of `components/UI`.
- **Dynamic Imports**: Use `next/dynamic` for heavy components (e.g., Charts, Modals) that aren't needed on initial load.
- **Conditional Loading**: Only load modules when a specific feature flag or user interaction occurs.

## Gotchas
- **&& vs Ternary**: Use `{count > 0 ? <Child /> : null}` instead of `{count && <Child />}` to avoid rendering `0` in the UI.
- **Effect Events**: Use `useEffectEvent` (experimental) for logic that shouldn't trigger the effect but needs the latest state.
- **Batching**: Group CSS/DOM changes into a single class or `cssText` update.

## Verification Checklist
- [ ] No components defined inside other components.
- [ ] Expensive calculations are wrapped in `useMemo`.
- [ ] `Promise.all` is used for independent async calls.
- [ ] Barrel imports are avoided for core UI components.
- [ ] State is as local as possible to minimize re-render scope.
