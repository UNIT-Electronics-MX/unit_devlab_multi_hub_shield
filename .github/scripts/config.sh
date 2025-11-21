#!/bin/bash
# Configuration file for documentation deployment
# This file contains all configurable parameters to avoid hardcoded values

# Navigation Links
SHOP_URL="https://uelectronics.com/"
# Use GitHub Actions context variable if available, fallback to hardcoded URL
REPO_URL="${GITHUB_SERVER_URL:-https://github.com}/${GITHUB_REPOSITORY:-UNIT-Electronics-MX/unit_devlab_i2c_bme688_environmental_4_in_1_sensor}"

# Icons (using Unicode emojis)
SHOP_ICON="🛒"
REPO_ICON="📋"

# Titles
SHOP_TITLE="Shop"
REPO_TITLE="Repository"

# Styling
LINK_COLOR="#666"
LINK_PADDING="4px"
LINK_FONT_SIZE="14px"
LINK_MARGIN="4px"
BORDER_COLOR="#ddd"
BORDER_RADIUS="3px"
LINK_WIDTH="24px"
LINK_HEIGHT="24px"
LINE_HEIGHT="16px"

# Hover states
HOVER_BORDER_COLOR="#999"
HOVER_BG_COLOR="#f5f5f5"

# Timing
NAVBAR_INJECTION_DELAY="100"

# Build directories
BUILD_DIR="software/book/book"
DOCS_DIR="docs"

# Git configuration
GIT_BRANCH="main"
