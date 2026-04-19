---
name: i18n
description: Internationalization (i18n) for Next.js 15+. Standardized patterns using next-intl for routing, translations, and localized SEO. optimized for performance and type-safety.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Local file modification only"
  triggers:
    - "setup i18n"
    - "add multi-language support"
    - "next-intl config"
    - "localized routing"
    - "translation patterns"
---

# Internationalization (i18n) (Next.js 15+)

## Core Philosophy
1. **Routing-Based**: Use URL prefixes (e.g., `/en`, `/th`) for better SEO and user sharing.
2. **Type-Safe**: Use TypeScript for translation keys to prevent missing translation errors.
3. **Server-First**: Prefer using translations in Server Components to minimize client bundle size.

## 1. Setup with `next-intl`
`next-intl` is the most robust solution for Next.js App Router.
- **Middleware**: Handles locale detection and URL redirection.
- **i18n.ts**: Central configuration for loading messages.
- **Navigation**: Use the provided `Link`, `usePathname`, and `useRouter` from `next-intl` to maintain the locale in the URL.

## 2. Directory Structure
```text
├── messages/            # JSON files for each locale
│   ├── en.json
│   └── th.json
├── src/
│   ├── app/
│   │   └── [locale]/    # Catch-all route for localized pages
│   │       ├── layout.tsx
│   │       └── page.tsx
│   ├── i18n.ts          # Request-level config
│   └── middleware.ts     # Locale detection
```

## 3. Usage Patterns
- **Server Components**:
```tsx
const t = await getTranslations('Index');
return <h1>{t('title')}</h1>;
```
- **Client Components**:
```tsx
const t = useTranslations('Index');
return <button>{t('label')}</button>;
```

## 4. Localized SEO
- **Metadata**: Use the `locale` parameter in `generateMetadata` to set localized titles and descriptions.
- **Alternates**: Configure `alternates` in metadata to tell search engines about other language versions of the page.

## Gotchas
- **Hydration**: Ensure messages are passed correctly to Client Components to avoid flickering or hydration errors.
- **Date/Time**: Use `next-intl`'s `useFormatter` for localized date, time, and currency formatting.

## Verification Checklist
- [ ] Localized routing is configured with `[locale]` segment.
- [ ] `next-intl` middleware is handling redirection correctly.
- [ ] Translation keys are type-safe.
- [ ] SEO metadata includes localized alternates.
- [ ] Dates and numbers are formatted according to the current locale.
