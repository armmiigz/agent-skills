---
name: accessibility-a11y
description: Build inclusive web applications following WCAG 2.1 standards. Covers ARIA roles, keyboard navigation, semantic HTML, and automated a11y testing.
metadata:
  version: "1.0"
  triggers:
    - "setup accessibility"
    - "improve a11y"
    - "aria labels"
    - "keyboard navigation"
    - "wcag compliance"
    - "screen reader support"
---

# Accessibility (a11y)

## Core Philosophy
1. **Inclusive by Design**: Accessibility is not a checklist; it's a fundamental requirement.
2. **Semantic HTML First**: Use the right tag for the right job (`<button>` vs `<div>`) to get 80% of a11y for free.
3. **Keyboard Ready**: Everything that can be clicked must be reachable and triggerable via keyboard.

## 1. Semantic HTML & ARIA
- **Headings**: Use `<h1>` to `<h6>` in a logical hierarchy. Never skip levels.
- **Landmarks**: Use `<header>`, `<main>`, `<footer>`, `<nav>`, and `<aside>`.
- **ARIA Roles**: Only use ARIA when native HTML isn't enough.
  - `aria-label`: For elements without visible text.
  - `aria-hidden="true"`: For decorative elements.
  - `aria-expanded`: For togglable UI (modals, accordions).

## 2. Keyboard Navigation
- **Focus Indicators**: Never remove the focus ring (`outline: none`) without providing a visible alternative.
- **Tab Order**: Ensure the tab order follows the visual flow of the page.
- **Skip Links**: Provide a "Skip to main content" link for keyboard users.

## 3. Visual Accessibility
- **Color Contrast**: Maintain at least 4.5:1 for normal text and 3:1 for large text.
- **Form Labels**: Every input must have a visible `<label>` or a valid `aria-label`.
- **Focus Management**: When a modal opens, move focus inside it. When it closes, return focus to the trigger.

## 4. Automated Testing
- **eslint-plugin-jsx-a11y**: Catch common errors during development.
- **axe-core**: Run automated audits in the browser or via Playwright.

## Gotchas
- **Clickable Divs**: If you must use a `<div>` as a button, you MUST add `role="button"`, `tabIndex={0}`, and an `onKeyDown` handler for Space/Enter.
- **Dynamic Content**: Use `aria-live` (polite or assertive) to announce dynamic updates to screen readers.

## Verification Checklist
- [ ] No `outline: none` without a custom focus state.
- [ ] Semantic HTML tags are used correctly (e.g., buttons are `<button>`).
- [ ] All images have descriptive `alt` text (or `alt=""` if decorative).
- [ ] Form fields have associated labels.
- [ ] Page passes an `axe` audit with zero critical violations.
- [ ] UI is fully navigable and usable using only the keyboard.
