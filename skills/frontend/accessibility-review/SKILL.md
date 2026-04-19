---
name: accessibility-review
description: Audit and improve application accessibility. Covers WCAG 2.1 compliance, screen reader optimization, keyboard navigation, and color contrast auditing.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: File read/write for accessibility fixes"
  triggers:
    - "accessibility audit"
    - "a11y review"
    - "check wcag compliance"
    - "improve screen reader support"
    - "keyboard navigation check"
---

# Accessibility (A11y) Review

## Core Philosophy
1. **Inclusion**: Software should be usable by everyone, including people with visual, auditory, motor, or cognitive impairments.
2. **Standard-Based**: Adhere to WCAG 2.1 (AA level) as the baseline.
3. **Semantic HTML**: Use the correct HTML elements for their intended purpose to provide native accessibility.

## 1. Audit Categories
- **Semantic HTML**: Are we using `<button>` for actions and `<a>` for navigation?
- **ARIA Labels**: Are non-text elements (icons, complex components) properly labeled?
- **Color Contrast**: Do text/UI elements meet the minimum contrast ratio (4.5:1)?
- **Keyboard Navigation**: Can the entire app be used without a mouse (Focus states, Tab order)?
- **Screen Readers**: Is the document structure logical (H1-H6) and readable by AT (Assistive Technology)?

## 2. Review Tools
- **axe-core**: Automated accessibility testing (Integrated in Playwright).
- **Lighthouse**: Basic accessibility score.
- **VoiceOver/NVDA**: Manual screen reader testing.
- **WAVE**: Browser extension for visual auditing.

## 3. Common Fixes
- Adding `aria-label` to icon-only buttons.
- Ensuring `alt` text on all images.
- Fixing `tabindex` order.
- Adding `aria-expanded` and `aria-controls` to accordions/modals.

## Verification Checklist
- [ ] Automated A11y tests pass (Zero axe violations).
- [ ] Keyboard navigation is logical and visual (Focus rings).
- [ ] Color contrast meets WCAG AA standards.
- [ ] Forms have properly associated labels and error messages.
