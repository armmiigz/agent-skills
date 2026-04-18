#!/bin/bash

# setup-lint.sh - Automated Quality Gate Setup
# Part of the Agent Skills project

set -e

log_stderr() {
  echo "$1" >&2
}

# --- 1. Environment Check ---
if [ ! -f "package.json" ]; then
  log_stderr "ERROR: package.json not found. Run this in the project root."
  exit 1
fi

# --- 2. Install Dependencies ---
log_stderr "Installing linting & formatting dependencies..."
npm install --save-dev eslint prettier typescript-eslint eslint-config-prettier

# --- 3. Create ESLint Config (Flat Config) ---
log_stderr "Creating eslint.config.js..."
cat <<EOF > eslint.config.js
import js from '@eslint/js';
import tseslint from 'typescript-eslint';
import eslintConfigPrettier from 'eslint-config-prettier';

export default tseslint.config(
  { ignores: ['dist/', 'node_modules/'] },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  eslintConfigPrettier,
  {
    rules: {
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/explicit-function-return-type': 'error',
      'no-console': 'warn',
    }
  }
);
EOF

# --- 4. Create Prettier Config ---
log_stderr "Creating .prettierrc..."
cat <<EOF > .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5"
}
EOF

# --- 5. Finalize ---
log_stderr "Linting setup complete with STRICT rules."
