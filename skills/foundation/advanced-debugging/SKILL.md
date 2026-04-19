---
name: advanced-debugging
description: Methodical root cause analysis and debugging. Covers hypothesis-driven debugging, state isolation, performance profiling, and error tracing in complex systems.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Read/write access for log analysis and temporary instrumentation"
  triggers:
    - "debug error"
    - "fix bug"
    - "troubleshoot issue"
    - "root cause analysis"
    - "performance profiling"
---

# Advanced Debugging & RCA

## Core Philosophy
1. **Hypothesis-Driven**: Don't change code randomly. Form a hypothesis, then test it.
2. **Isolate the Variable**: Narrow down the cause by removing components until the error disappears.
3. **Trace the Flow**: Follow the data from input to the point of failure.

## 1. Debugging Workflow
1. **Reproduce**: Confirm the bug exists and find a consistent way to trigger it.
2. **Analyze Logs**: Check [observability](../../foundation/observability/SKILL.md) logs and correlation IDs.
3. **Instrument**: Add temporary logs or breakpoints to capture state at critical junctures.
4. **Identify**: Find the specific line or condition causing the failure.
5. **Fix & Verify**: Apply the fix and verify it doesn't cause regressions.
6. **Automate**: Add a regression test in the [testing](../../foundation/testing/SKILL.md) suite.

## 2. Tools & Techniques
- **React DevTools**: Inspect component tree, state, and props.
- **Chrome DevTools (Network)**: Check for failing requests, payload errors, or latency.
- **Node.js --inspect**: Remote debugging for backend services.
- **Profiling**: Use Flamegraphs to find CPU bottlenecks.

## 3. Common Anti-Patterns
- **"Shotgun Debugging"**: Making random changes and hoping something works.
- **Ignoring the Error Message**: Read the full stack trace; the answer is often in the first few lines.
- **Assuming "It must be X"**: Keep an open mind; bugs often hide in the most "stable" parts of the code.

## Verification Checklist
- [ ] Bug is consistently reproducible.
- [ ] Root cause is clearly identified (not just a symptom).
- [ ] Fix is verified by a regression test.
- [ ] No side effects introduced.
- [ ] Documentation/ADR updated if the fix involved architectural changes.
