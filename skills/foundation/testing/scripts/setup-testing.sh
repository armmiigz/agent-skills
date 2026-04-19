#!/bin/bash

# Install dependencies
echo "Installing testing dependencies..."
npm install -D vitest @vitejs/plugin-react jsdom @testing-library/react @testing-library/jest-dom @playwright/test

# Create Vitest config
cat <<EOF > vitest.config.ts
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: './__tests__/setup.ts',
  },
})
EOF

# Create basic setup file
mkdir -p __tests__
cat <<EOF > __tests__/setup.ts
import '@testing-library/jest-dom'
EOF

echo "Testing setup complete!"
