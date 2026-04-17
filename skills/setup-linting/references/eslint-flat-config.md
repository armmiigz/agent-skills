# Modern ESLint Flat Config (Strict)

ESLint 9+ uses a new configuration system called **Flat Config**. This document provides a strict boilerplate for TypeScript projects.

## 1. `eslint.config.js` Boilerplate

```javascript
import js from '@eslint/js';
import tseslint from 'typescript-eslint';
import eslintConfigPrettier from 'eslint-config-prettier';

export default tseslint.config(
  // Global ignores
  { ignores: ['dist/', 'node_modules/', 'coverage/'] },
  
  // Base JS & TS Recommended
  js.configs.recommended,
  ...tseslint.configs.recommended,
  
  // Prettier Conflict Resolution (Must be last)
  eslintConfigPrettier,
  
  // --- STRICT QUALITY GATE RULES ---
  {
    rules: {
      /* Errors: Zero-tolerance for bad patterns */
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/explicit-function-return-type': 'error',
      '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
      'no-console': ['warn', { allow: ['warn', 'error'] }],
      
      /* Preferences */
      'prefer-const': 'error',
      'no-var': 'error',
    }
  }
);
```

## 2. Best Practices
- **Explicit Returns**: Forcing return types improves code readability and ensures the function actually returns what you expect.
- **No Any**: Use `unknown` or generics. `any` is a security risk and a bug magnet.
- **Unused Variables**: Prevents code rot. Always prefix unused arguments with an underscore (e.g., `_req`).

## 3. Integration with Prettier
Ensure `eslint-config-prettier` is the **very last** item in your export array. This ensures that ESLint doesn't throw errors for formatting choices that Prettier is handling.
