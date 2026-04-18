---
name: state-management
description: High-performance state management for Next.js 15+. Combines TanStack Query for server-state (caching, fetching) and Zustand for lightweight global client-state. Optimized for token-efficiency and re-render reduction.
metadata:
  version: "1.0"
  triggers:
    - "setup state management"
    - "tanstack query config"
    - "zustand store"
    - "global state"
    - "server state caching"
    - "optimistic updates"
---

# State Management (Next.js 15+)

## Core Philosophy
1. **Server State != Client State**: Use TanStack Query for anything that comes from an API/DB. Use Zustand for UI state (modals, themes, local filters).
2. **Minimize Global State**: Keep state as local as possible. Only hoist to global stores when absolutely necessary.
3. **Immutability & Safety**: Use TypeScript for all store definitions.

## 1. Server State (TanStack Query)
The industry standard for fetching, caching, and synchronizing server state.
- **Key Features**: Auto-refetching, polling, background synchronization, and **Optimistic Updates**.
- **Next.js Integration**: Wrap the app in a `QueryClientProvider` (Client Component). Use `hydrate` for SSR support.
```tsx
// Example Query
const { data, isLoading } = useQuery({
  queryKey: ['products'],
  queryFn: fetchProducts,
});
```

## 2. Client State (Zustand)
A small, fast, and scalable barebones state-management solution.
- **Why Zustand?**: Zero boilerplate, handles async actions naturally, and no Context Provider nesting required.
- **Pattern**: Create small, focused stores instead of one giant store.
```tsx
// Example Store
const useCartStore = create((set) => ({
  items: [],
  addItem: (item) => set((state) => ({ items: [...state.items, item] })),
}));
```

## 3. Data Synchronization
- **Optimistic Updates**: Update the UI immediately while the Server Action/API is running, then roll back if it fails.
- **Invalidation**: Use `queryClient.invalidateQueries({ queryKey: [...] })` after a successful mutation to keep data fresh.

## 4. Best Practices
- **Select Over Destructure**: Always use selectors in Zustand to prevent unnecessary re-renders.
  - `const items = useCartStore(state => state.items)` (Good)
  - `const { items } = useCartStore()` (Bad - re-renders on any change)
- **SSR Hydration**: For Zustand, ensure state is hydrated correctly on the client to avoid hydration mismatches.

## Gotchas
- **Next.js 15 Fetch Defaults**: Next.js 15 defaults to `no-store`. TanStack Query provides a robust alternative for managing cache TTLs independently of the fetch behavior.
- **Zustand Persistence**: Use `persist` middleware for `localStorage` sync, but handle hydration carefully.

## Verification Checklist
- [ ] Server state is managed by TanStack Query.
- [ ] Global client state is managed by Zustand (not Context).
- [ ] Selectors are used in Zustand to optimize re-renders.
- [ ] Mutations include appropriate query invalidation or optimistic updates.
- [ ] Store definitions are fully typed with TypeScript.
