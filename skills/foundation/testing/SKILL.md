---
name: testing
description: Comprehensive testing strategy for Next.js 15+. Covers unit/component testing with Vitest and End-to-End (E2E) testing with Playwright. Focuses on testing user behavior, SSR validation, and performance.
metadata:
  version: "1.0"
  triggers:
    - "setup testing"
    - "write unit test"
    - "write e2e test"
    - "playwright config"
    - "vitest config"
    - "test react component"
---

# Testing Strategy (Next.js 15+)

## Core Philosophy
1. **User-Centric**: Test what the user sees and interacts with, not internal implementation details.
2. **Hybrid Approach**:
   - **Vitest**: Fast, isolated unit and component tests (Client side logic).
   - **Playwright**: Real-browser E2E tests (SSR, navigation, full flows).
3. **Efficiency**: Test against production builds (`npm run build && npm run start`) for E2E to ensure real-world behavior.

## 1. Unit & Component Testing (Vitest)
Use Vitest for logic and UI components in isolation.
- **Tools**: Vitest, React Testing Library, `@vitejs/plugin-react`.
- **Naming**: `*.test.ts` or `*.test.tsx`.
- **Best Practice**: Mock heavy dependencies or API calls using `vi.mock()` or MSW.

## 2. E2E Testing (Playwright)
Use Playwright for critical user journeys (Auth, Checkout, Form Submission).
- **Tools**: Playwright Test, `@playwright/test`.
- **Config**: Always set `webServer` to run `npm run build && npm run start`.
- **State Persistence**: Reuse authentication state via `storageState` to speed up tests.
- **Visual Testing**: Use `expect(page).toHaveScreenshot()` for pixel-perfect regression checking.

## 3. Recommended Directory Structure
```text
├── __tests__/           # Vitest Unit/Component tests
│   ├── unit/            # Utility functions
│   └── components/      # UI Components
├── e2e/                 # Playwright E2E tests
│   ├── auth.setup.ts    # Global setup (e.g., login)
│   └── flows/           # User journeys
├── playwright.config.ts
└── vitest.config.ts
```

## Scripts (`package.json`)
```json
{
  "test": "vitest",
  "test:ui": "vitest --ui",
  "test:e2e": "playwright test",
  "test:e2e:ui": "playwright test --ui"
}
```

## Gotchas
- **Hydration Mismatches**: Vitest might not catch these; Playwright will.
- **Server Components**: Hard to test in isolation with RTL/Vitest. Use E2E tests for RSC-heavy pages.
- **Environment Variables**: Ensure `.env.test` is loaded correctly in both environments.

## Verification Checklist
- [ ] Vitest and Playwright are configured in separate directories.
- [ ] E2E tests run against a production build (`npm run build`).
- [ ] Critical paths (Login, CRUD) have E2E coverage.
- [ ] Unit tests cover complex business logic in `lib/` or `utils/`.
- [ ] CI pipeline runs both test suites on Pull Requests.
