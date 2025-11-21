#!/bin/bash
# Build documentation for GitHub Actions deployment
# This script builds documentation using configurable parameters (no hardcoded values)

echo " Building documentation for GitHub Actions..."

# Load configuration with robust path handling
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/config.sh"

# Build documentation (does NOT modify docs/ directory)
echo " Building documentation..."
python3 .github/scripts/build_docs.py

if [ $? -ne 0 ]; then
    echo " Build failed!"
    exit 1
fi

# Check if book directory was created
if [ ! -d "${BUILD_DIR}" ]; then
    echo " ${BUILD_DIR}/ directory not found after build!"
    exit 1
fi

echo "Files in ${BUILD_DIR}/ directory:"
ls -la "${BUILD_DIR}/"

# Load navbar builder functions
source "$(dirname "$0")/navbar-builder.sh"

# Build navbar using configurable parameters
build_navbar_into_files "${BUILD_DIR}"

echo "Documentation built successfully!"

# Copy to docs/ directory for GitHub Pages deployment
echo "Copying documentation to ${DOCS_DIR}/ directory..."

# Remove existing content from docs/ (except PDFs if any)
find "${DOCS_DIR}" -name "*.html" -delete 2>/dev/null || true
find "${DOCS_DIR}" -name "*.css" -delete 2>/dev/null || true
find "${DOCS_DIR}" -name "*.js" -delete 2>/dev/null || true
find "${DOCS_DIR}" -type d -name "FontAwesome" -exec rm -rf {} + 2>/dev/null || true
find "${DOCS_DIR}" -type d -name "fonts" -exec rm -rf {} + 2>/dev/null || true
find "${DOCS_DIR}" -type d -name "css" -exec rm -rf {} + 2>/dev/null || true
find "${DOCS_DIR}" -type d -name "resources" -exec rm -rf {} + 2>/dev/null || true
find "${DOCS_DIR}" -type d -name "hardware" -exec rm -rf {} + 2>/dev/null || true
find "${DOCS_DIR}" -type d -name "software" -exec rm -rf {} + 2>/dev/null || true

# Copy new built content to docs/
cp -r "${BUILD_DIR}"/* "${DOCS_DIR}/"

echo "Updated ${DOCS_DIR}/ directory contents:"
ls -la "${DOCS_DIR}/" | head -10

# Force commit the updated docs/ directory
echo "Committing updated documentation to ${DOCS_DIR}/..."
git add "${DOCS_DIR}/"

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "ℹNo changes detected in ${DOCS_DIR}/ directory"
else
    # Force commit changes
    echo "Committing documentation updates..."
    git commit -m "Auto-update documentation in ${DOCS_DIR}/

    - Built from latest README content  
    - Generated: $(date)
    - Updated navbar with configurable ${SHOP_TITLE} and ${REPO_TITLE} icons
    - Commit: $(git rev-parse --short HEAD)"
    
    # Push to repository to trigger deployment
    echo "📡 Pushing to trigger GitHub Pages deployment..."
    git push origin "${GIT_BRANCH}"
    
    if [ $? -eq 0 ]; then
        echo "Documentation successfully updated and pushed!"
        echo "GitHub Pages will deploy automatically in a few minutes"
        echo "Check deployment status at: ${REPO_URL}/actions"
    else
        echo "Failed to push to repository!"
        exit 1
    fi
fi

echo "Documentation deployment process completed!"