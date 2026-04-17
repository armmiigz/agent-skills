#!/bin/bash

# setup.sh - Automated shadcn/ui setup for Next.js projects
# Part of the Agent Skills project

set -e

# --- Helper Functions ---
log_stderr() {
  echo "$1" >&2
}

log_stdout() {
  echo "$1"
}

# --- 1. Environment Check ---
log_stderr "Checking environment..."

if ! command -v node &> /dev/null; then
  log_stderr "ERROR: node is not installed. Please install Node.js to continue."
  exit 1
fi

if ! command -v npx &> /dev/null; then
  log_stderr "ERROR: npx is not installed. npx is required to run shadcn CLI."
  exit 1
fi

if [ ! -f "package.json" ]; then
  log_stderr "ERROR: package.json not found. Please run this script in the root of your project."
  exit 1
fi

# --- 2. Detector ---
log_stderr "Detecting package manager..."
PKG_MANAGER="npm"
if [ -f "pnpm-lock.yaml" ]; then
  PKG_MANAGER="pnpm"
elif [ -f "yarn.lock" ]; then
  PKG_MANAGER="yarn"
elif [ -f "bun.lockb" ]; then
  PKG_MANAGER="bun"
fi

log_stderr "Using $PKG_MANAGER as package manager."

# --- 3. Dependency Installation (Tailwind v4 Focus) ---
log_stderr "Installing core dependencies (Tailwind CSS v4 & UTILS)..."

case $PKG_MANAGER in
  pnpm)
    pnpm add tailwindcss @tailwindcss/vite
    pnpm add -D tw-animate-css
    ;;
  yarn)
    yarn add tailwindcss @tailwindcss/vite
    yarn add -D tw-animate-css
    ;;
  bun)
    bun add tailwindcss @tailwindcss/vite
    bun add -D tw-animate-css
    ;;
  *)
    npm install tailwindcss @tailwindcss/vite
    npm install --save-dev tw-animate-css
    ;;
esac

# --- 4. shadcn/ui Initialization ---
log_stderr "Initializing shadcn/ui (Non-Interactive)..."

# Using -d for default settings as requested
npx shadcn@latest init -d

# --- 5. Post-Install Cleanup ---
if [ -f "tailwind.config.ts" ] || [ -f "tailwind.config.js" ]; then
  log_stderr "Cleaning up legacy v3 config files..."
  rm -f tailwind.config.ts tailwind.config.js
fi

# --- 6. Success Output ---
log_stderr "Setup complete!"
log_stdout "{\"status\": \"success\", \"message\": \"shadcn/ui initialized with defaults and Tailwind v4 dependencies installed.\"}"
