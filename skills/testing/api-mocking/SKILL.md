---
name: api-mocking
description: Decouple frontend from backend development. Covers API mocking using Mock Service Worker (MSW), generating realistic mock data (Faker.js), and testing failure scenarios.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Local file modification only"
  triggers:
    - "setup msw"
    - "mock api response"
    - "test without backend"
    - "generate mock data"
    - "simulate api error"
---

# API Mocking (MSW)

## Core Philosophy
1. **Develop in Isolation**: Frontend shouldn't be blocked by backend availability.
2. **Reliable Testing**: Tests should not depend on real network calls or external servers.
3. **Edge Case Validation**: Easily simulate 500 errors, timeouts, and slow networks.

## 1. Mock Service Worker (MSW)
The gold standard for API mocking.
- **Service Worker**: Intercepts requests at the network level in the browser.
- **Node Integration**: Intercepts requests in Vitest/Playwright tests.

## 2. Generating Mock Data (Faker.js)
Avoid static "test" strings. Use `faker` to generate realistic names, dates, and amounts.
- **Benefit**: Catches UI issues like text overflow or unexpected date formats.

## 3. Simulating Scenarios
- **Delay**: Simulate high-latency networks to test loading states.
- **Errors**: Return `res(ctx.status(500))` to ensure the UI handles crashes gracefully.
- **Empty States**: Return `[]` to test "No data found" views.

## 4. Integration with TanStack Query
Ensure your mocks match the schema expected by your [state-management](../frontend/state-management/SKILL.md) layer.

## Verification Checklist
- [ ] MSW is configured for both browser (Dev) and Node (Tests).
- [ ] Handlers are organized by domain (e.g., `auth.handlers.ts`).
- [ ] Mock data is generated using Faker for realism.
- [ ] Error scenarios (404, 500) are mocked and tested.
- [ ] Mocks are updated when the real API schema changes.
