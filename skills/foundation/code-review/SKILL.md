---
name: code-review
description: Professional code review standards. Focuses on architectural consistency, performance, security, and maintainability. Ensures code follows established repository skills and standards.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Read-only access to files for analysis"
  triggers:
    - "perform code review"
    - "check code quality"
    - "review pull request"
    - "audit implementation"
    - "standardize code"
---

# Code Review Standards

## Core Philosophy
1. **Be Constructive**: Focus on the code, not the person. Provide clear rationale and examples for improvements.
2. **Prioritize Correctness & Security**: Check for logical bugs, race conditions, and security vulnerabilities (XSS, Injection, Auth bypass).
3. **Consistency over Cleverness**: Favor established patterns and readable code over "clever" but complex solutions.

## 1. Review Categories
### Architectural Alignment
- Does the code follow the [architecture](../../foundation/architecture/SKILL.md) standards?
- Are dependencies managed correctly (e.g., no cross-workspace leaks)?

### Performance
- Are there unnecessary re-renders (React)?
- Is data fetching optimized (no waterfalls)?
- Are database queries indexed and efficient?

### Maintainability
- Is the code self-documenting?
- Are complex logics extracted into hooks or services?
- Is [testing-strategy](../../testing/testing-strategy/SKILL.md) followed?

## 2. Review Workflow
1. **Context Check**: Read the relevant [spec-driven-development](../../foundation/spec-driven-development/SKILL.md) docs first.
2. **Automated Check**: Run linting and unit tests.
3. **Line-by-Line Review**: Check for logic, naming, and patterns.
4. **Summary**: Provide a clear "Approve", "Request Changes", or "Comment" with categorized feedback.

## 3. Best Practices
- **Small PRs**: Reviewing 100 lines is more effective than reviewing 1000 lines.
- **Automate the Obvious**: Don't waste review time on formatting or linting (let the CI do it).
- **Check for "Why"**: If something looks weird, ask for the rationale before suggesting a change.

## Verification Checklist
- [ ] Code follows [react-best-practices](../../frontend/react-best-practices/SKILL.md).
- [ ] Code follows [app-security](../../backend/security/SKILL.md).
- [ ] Public APIs/Functions have [project-documentation](../../foundation/project-documentation/SKILL.md).
- [ ] Tests cover all critical paths.
- [ ] No regression in performance or accessibility.
