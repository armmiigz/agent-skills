---
name: spec-driven-development
description: Workflow for turning design specifications into verified code. Uses the "Spec-First" approach (plan.md, spec.md, tasks.md) to ensure implementation matches business requirements and TDD standards.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: File read/write (for creating specs and updating tasks)"
    - "Execution: Runs local python scripts for scaffolding"
  triggers:
    - "follow specifications"
    - "update tasks.md"
    - "implement user story"
    - "verify against spec"
    - "tdd workflow"
---

# Spec-Driven Development (SDD)

## Core Philosophy
1. **Design Before Code**: Never write implementation without a corresponding `spec.md` and `tasks.md`.
2. **TDD Mandatory**: Every task must have a failing test before implementation.
3. **Traceability**: Every line of code should be traceable back to a user story in the specifications.

## 1. Specification Artifacts
The `specs/` directory is the source of truth.
- **plan.md**: High-level technical strategy and architecture.
- **spec.md**: User stories, functional requirements, and acceptance criteria.
- **data-model.md**: Definition of domain entities and state structures.
- **tasks.md**: Granular TODO list. Each task must have a unique ID (e.g., T001) and an "Independent Test".

## 2. Implementation Workflow
1. **Analyze**: Read all files in `specs/[feature]/` to understand the full context.
2. **Test First**: Write a failing test (Unit or E2E) based on the "Independent Test" in `tasks.md`.
3. **Implement**: Write the minimum code required to pass the test.
4. **Refactor**: Clean up code using [react-best-practices](../frontend/react-best-practices/SKILL.md) and [composition-patterns](../frontend/composition-patterns/SKILL.md).
5. **Mark Done**: Update `tasks.md` with `[x]` only after the test passes.

## 3. Independent Verification
Each User Story must be testable in isolation.
- **Check**: "If I only run the tests for US1, does it pass without needing US2?"
- **Integration**: Use [api-mocking](../../testing/api-mocking/SKILL.md) to isolate features during development.

## 4. Maintenance & Synchronization
- **Sync**: If the implementation logic changes, the `data-model.md` or `spec.md` must be updated first.
- **Review**: Use [engineering-standards](../../architecture/engineering-standards/SKILL.md) to review code against the original spec.

## Gotchas
- **Spec Drift**: Implementing features that are not in the spec (Over-engineering).
- **Stale Tasks**: Forgetting to update `tasks.md` after completion.
- **Test Omission**: Skipping the failing test step (Breaking TDD).

## Verification Checklist
- [ ] Implementation matches all requirements in `spec.md`.
- [ ] `tasks.md` is updated with current progress.
- [ ] All "Independent Tests" for the current phase pass.
- [ ] Data structures match `data-model.md`.
- [ ] Code follows the architectural plan in `plan.md`.
