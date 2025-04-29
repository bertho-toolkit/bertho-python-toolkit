#!/bin/bash

# Usage:
# bash release.sh 1.0.0

VERSION=$1

if [ -z "$VERSION" ]; then
  echo "❌ Please provide a version. Example: bash release.sh 1.0.0"
  exit 1
fi

echo "⚡ Preparing to release version v$VERSION..."
read -p "❓ Confirm release v$VERSION? (y/n): " CONFIRM

if [[ "$CONFIRM" != "y" ]]; then
  echo "❌ Release cancelled."
  exit 1
fi

# Update version inside pyproject.toml and setup.cfg
sed -i "s/^version = .*/version = \"$VERSION\"/" pyproject.toml
sed -i "s/^version = .*/version = $VERSION/" setup.cfg

echo "📋 Version updated in pyproject.toml and setup.cfg."

# Git operations
git add .
git commit -m "chore: release v$VERSION"
git push origin main

git tag v$VERSION
git push origin v$VERSION

echo "✅ Release v$VERSION pushed successfully!"

# Deploy MkDocs site to GitHub Pages
echo "🚀 Deploying documentation to GitHub Pages..."
mkdocs gh-deploy --clean

echo "✅ Documentation deployed!"
