# Coding Standards & Best Practices

To maintain a healthy shadcn/ui codebase, follow these standards.

## Best Practices (The Do's)

### 1. Own Your UI Components
Treat files in `components/ui` as part of your source code, not an external dependency.
- **Do**: Modify the source code if you need a specific behavior or style change that props don't cover.
- **Do**: Add custom variants using `class-variance-authority` (CVA) inside the component file.

### 2. Composition Over Logic
Keep your UI components "dumb" and presentational.
- **Do**: Create wrapper components (e.g., `components/auth/login-form.tsx`) that use UI components (`Button`, `Input`) and handle state/API calls.
- **Do**: Use the `asChild` prop from Radix UI to allow custom triggers without extra DOM nodes.

### 3. Use the `cn()` Utility
Always use the provided `cn()` utility to merge Tailwind classes.
- **Do**: `<div className={cn("base-class", className)} />`
- **Why**: It handles class merging and deduplication correctly (using `tailwind-merge`).

### 4. Accessibility First
shadcn/ui is built on Radix UI, which is accessible by default.
- **Do**: Keep the ARIA attributes and keyboard interaction logic intact when modifying components.

---

## Worst Case Scenarios (The Don'ts)

### 1. Treating UI Components as a Black Box
- **Worst Case**: Attempting to override deeply nested styles using highly specific CSS selectors or `!important`.
- **Result**: Brittle UI that breaks on updates or theme changes.
- **Fix**: Modify the component source code directly.

### 2. Business Logic in UI Directory
- **Worst Case**: Importing API clients, hooks (`useAuth`), or business logic into `components/ui/dialog.tsx`.
- **Result**: Circular dependencies and impossible-to-reuse UI components.
- **Fix**: Move logic to a feature-specific component or a hook.

### 3. Ignoring Shadow DOM / Hydration
- **Worst Case**: Using random IDs or browser-only APIs (`window`) inside components without checking for server-side execution.
- **Result**: Next.js hydration mismatches.
- **Fix**: Use `useEffect` for browser-only logic or standard React state.

### 4. Over-customizing Base Components
- **Worst Case**: Adding 20+ props to a simple `Button` to handle every single design edge case.
- **Result**: Unreadable, unmaintainable code.
- **Fix**: Use CVA variants or create a new dedicated component if it's significantly different.
