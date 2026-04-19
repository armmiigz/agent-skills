---
name: testing-strategy
description: High-level testing strategy and planning. Defines the test pyramid, selecting the right tools (Unit, Integration, E2E), and establishing coverage standards for quality assurance.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Planning only"
  triggers:
    - "plan testing strategy"
    - "test pyramid"
    - "qa strategy"
    - "coverage standards"
    - "testing roadmap"
---

# Testing Strategy & Quality Assurance

## Core Philosophy
1. **The Test Pyramid**: Favor fast, isolated unit tests over slow, brittle E2E tests.
2. **Shift Left**: Start testing as early as possible in the development lifecycle.
3. **Deterministic Tests**: Avoid "flaky" tests. If a test fails occasionally, fix it or delete it.

## 1. The Testing Layers
- **Unit Tests (Vitest)**: Test individual functions and logic in isolation. (Target: 70-90% coverage)
- **Integration Tests**: Test how components or services work together. (Target: 40-60% coverage)
- **E2E Tests (Playwright)**: Test critical user journeys (Login, Checkout). (Target: Top 10-20 user paths)
- **Visual Regression**: Test UI consistency using tools like Chromatic or Playwright snapshots.

## 2. Coverage Standards
Focus on **Critical Path Coverage** over raw percentage.
- **Critical**: Auth, Data Persistence, Payments. (Must be >90%)
- **Core**: Business logic, API handlers. (Must be >70%)
- **UI**: Display logic, formatting. (Low priority)

## 3. CI/CD Integration
- Run Unit/Integration tests on every PR.
- Run E2E tests on staging/pre-production environments.
- Block merging if tests fail or coverage drops below the threshold.

## Verification Checklist
- [ ] Strategy follows the Test Pyramid.
- [ ] Critical paths are fully identified.
- [ ] Tools are correctly selected for each layer.
- [ ] Coverage goals are realistic and enforced.
