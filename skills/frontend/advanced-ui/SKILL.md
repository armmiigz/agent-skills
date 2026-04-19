---
name: advanced-ui
description: Build high-performance, interactive UI. Covers complex tables (TanStack Table), advanced micro-animations (Framer Motion), and multi-step UX flow orchestration.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Local file modification only"
  triggers:
    - "build complex table"
    - "framer motion animations"
    - "ux flow builder"
    - "multi-step form flow"
    - "interactive dashboard"
---

# Advanced UI & Interaction

## 1. Complex Tables (TanStack Table)
For data-heavy applications, use TanStack Table for headless logic.
- **Features**: Sorting, Filtering, Pagination, Column Pinning, and Virtualization.
- **Pattern**: Keep the logic headless and style with Tailwind/shadcn-ui.

## 2. Micro-Animations (Framer Motion)
Enhance UX with subtle, meaningful motion.
- **Principles**: 
  - **Anticipation**: Brief movement before the main action.
  - **Stagger**: Animate children sequentially for a "ripple" effect.
  - **Layout**: Use `layoutId` for smooth shared element transitions.
- **Efficiency**: Keep animations fast (<300ms) to avoid blocking the user.

## 3. UX Flow Orchestration
Managing complex multi-step interactions (e.g., Onboarding, Checkouts).
- **State Machine**: Use simple state variables or XState for complex logic.
- **Persistent State**: Save progress to URL params or LocalStorage to handle page refreshes.

## 4. Interaction Patterns
- **Optimistic UI**: Update the UI before the server responds (e.g., liking a post).
- **Skeleton States**: Use skeletons instead of spinners for a perceived faster load time.

## Verification Checklist
- [ ] Tables are performant with large datasets (virtualized if >100 rows).
- [ ] Animations respect `prefers-reduced-motion`.
- [ ] Multi-step flows handle "back" and "refresh" correctly.
- [ ] Interactive elements provide clear visual feedback (hover, active, loading states).
