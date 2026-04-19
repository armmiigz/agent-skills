---
name: ux-writing
description: Craft clear and helpful interface copy. Focuses on microcopy, error messages, onboarding flows, and maintaining a consistent tone of voice for better user experience.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: File read/write for copy updates"
  triggers:
    - "ux writing"
    - "improve microcopy"
    - "write error message"
    - "onboarding copy"
    - "interface text"
---

# UX Writing & Microcopy

## Core Philosophy
1. **Be Concise**: Use as few words as possible while remaining clear.
2. **Be Helpful**: Tell the user what happened and, more importantly, how to fix it.
3. **Be Consistent**: Use the same terminology across the entire application.

## 1. Writing for UI
- **Buttons**: Use action-oriented verbs (e.g., "Save Changes" instead of "Submit").
- **Error Messages**: Avoid jargon. Be specific, polite, and actionable.
  - *Bad*: "Invalid input."
  - *Good*: "Password must be at least 8 characters long."
- **Empty States**: Explain why it's empty and how to get started (Call to Action).

## 2. Tone & Voice
- **Tone**: Adjust based on the situation (e.g., serious for errors, celebratory for success).
- **Voice**: Maintain a consistent personality (e.g., Professional yet approachable).

## 3. Localization (i18n)
Work with [i18n](../../frontend/i18n/SKILL.md) to ensure copy translates well and respects cultural nuances. Avoid idioms that don't translate.

## Verification Checklist
- [ ] Copy is clear and jargon-free.
- [ ] Tone is appropriate for the context.
- [ ] Error messages provide clear solutions.
- [ ] Terminology is consistent throughout the app.
- [ ] Copy is accessible (Simple language, no image-only text).
