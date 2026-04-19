---
name: tech-debt-management
description: Systematically audit and resolve technical debt. Covers identifying debt types, prioritizing using impact matrices, and executing refactoring sprints without disrupting features.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: File read/write for refactoring"
  triggers:
    - "audit tech debt"
    - "prioritize refactor"
    - "clean up code"
    - "manage technical debt"
    - "refactoring plan"
---

# Technical Debt Management

## Core Philosophy
1. **Visibility**: If you can't see the debt, you can't manage it. Use `TODO: [TECH-DEBT]` tags.
2. **Interest Rate**: Debt that slows down critical features has a "High Interest Rate" and must be fixed first.
3. **Controlled Refactoring**: Refactor in small, verifiable steps. Never refactor and add features in the same PR.

## 1. Debt Categories
- **Code Debt**: Poor naming, complex functions, lack of tests.
- **Architectural Debt**: Tight coupling, leaked abstractions, outdated libraries.
- **Design Debt**: Inconsistent UI components, UX friction.
- **Documentation Debt**: Missing comments, outdated READMEs/Specs.

## 2. Prioritization Matrix
- **Urgent/Important**: Blocking production or critical features. (Action: Immediate)
- **Not Urgent/Important**: Slowing down the team, affecting scalability. (Action: Schedule in next sprint)
- **Urgent/Not Important**: Minor bugs, cosmetic issues. (Action: Fix during related work)

## 3. Execution Strategy
- **Refactoring Sprints**: Dedicate 10-20% of engineering time to debt cleanup.
- **Boy Scout Rule**: Leave code cleaner than you found it.
- **Regression Testing**: Always ensure high [testing](../../foundation/testing/SKILL.md) coverage before refactoring.

## Verification Checklist
- [ ] Debt is identified and categorized.
- [ ] Prioritization is aligned with business goals.
- [ ] Refactoring plan is documented and reviewed.
- [ ] No regression introduced (confirmed by tests).
- [ ] Documentation updated to reflect the new implementation.
