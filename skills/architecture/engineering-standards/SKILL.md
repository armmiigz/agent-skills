---
name: engineering-standards
description: Maintain a healthy codebase. Covers Tech Debt prioritization, Testing Coverage strategies, and continuous quality improvement for long-term project viability.
metadata:
  version: "1.0"
  triggers:
    - "prioritize tech debt"
    - "test coverage strategy"
    - "improve code quality"
    - "engineering standards"
    - "code audit"
---

# Engineering Standards & Maintenance

## 1. Tech Debt Prioritization
Tech debt is inevitable; managing it is optional.
- **Audit**: Regularly tag technical debt using `TODO: [TECH-DEBT]` or issue labels.
- **Prioritization Matrix**:
  - **Critical**: Blocks features or causes production bugs. (Fix Now)
  - **High**: Slows down development significantly. (Fix next sprint)
  - **Low**: Cleanliness/Consistency issues. (Fix during related work)

## 2. Testing Coverage Strategy
Don't aim for 100% coverage; aim for 100% **Critical Path** coverage.
- **Critical Paths**: Auth, Payments, Data Integrity. (Must be >90%)
- **Internal Logic**: Shared utilities, complex business rules. (Must be >70%)
- **UI/Representational**: Styles, static layouts. (Low priority)

## 3. Code Quality Standards
- **DRY (Don't Repeat Yourself)**: But avoid "Premature Abstraction". Two instances of duplication are okay; three require a shared utility.
- **KISS (Keep It Simple, Stupid)**: Favor readable code over "clever" one-liners.
- **SOLID**: Apply where it adds clarity, especially Dependency Inversion for testability.

## 4. Continuous Refactoring
- **Boy Scout Rule**: Always leave the code slightly cleaner than you found it.
- **Small Commits**: Refactor in separate commits from feature work to make reviews easier.

## Verification Checklist
- [ ] Tech debt is documented and prioritized.
- [ ] Critical paths have high test coverage (>90%).
- [ ] Code follows the team's style guide and architectural patterns.
- [ ] Dependencies are audited for security and obsolescence.
- [ ] Large files/components are broken down into smaller, focused units.
