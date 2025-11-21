#!/bin/bash
# Navbar builder functions
# This file contains reusable functions for building navbar elements

# Load configuration with robust path handling
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/config.sh"

# Function to generate navbar JavaScript injection
generate_navbar_js() {
    cat << EOF
<script>
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        const menuBar = document.querySelector(".menu-bar .right-buttons");
        if (menuBar) {
            // Shop Link
            const shopLink = document.createElement("a");
            shopLink.href = "${SHOP_URL}";
            shopLink.target = "_blank";
            shopLink.innerHTML = "${SHOP_ICON}";
            shopLink.title = "${SHOP_TITLE}";
            shopLink.style.cssText = "color: ${LINK_COLOR}; text-decoration: none; padding: ${LINK_PADDING}; font-size: ${LINK_FONT_SIZE}; margin-right: ${LINK_MARGIN}; border: 1px solid ${BORDER_COLOR}; border-radius: ${BORDER_RADIUS}; transition: all 0.2s ease; display: inline-block; text-align: center; width: ${LINK_WIDTH}; height: ${LINK_HEIGHT}; line-height: ${LINE_HEIGHT};";
            shopLink.onmouseover = function() { this.style.borderColor = "${HOVER_BORDER_COLOR}"; this.style.backgroundColor = "${HOVER_BG_COLOR}"; };
            shopLink.onmouseout = function() { this.style.borderColor = "${BORDER_COLOR}"; this.style.backgroundColor = "transparent"; };
            
            // Repository Link
            const repoLink = document.createElement("a");
            repoLink.href = "${REPO_URL}";
            repoLink.target = "_blank";
            repoLink.innerHTML = "${REPO_ICON}";
            repoLink.title = "${REPO_TITLE}";
            repoLink.style.cssText = "color: ${LINK_COLOR}; text-decoration: none; padding: ${LINK_PADDING}; font-size: ${LINK_FONT_SIZE}; margin-right: ${LINK_MARGIN}; border: 1px solid ${BORDER_COLOR}; border-radius: ${BORDER_RADIUS}; transition: all 0.2s ease; display: inline-block; text-align: center; width: ${LINK_WIDTH}; height: ${LINK_HEIGHT}; line-height: ${LINE_HEIGHT};";
            repoLink.onmouseover = function() { this.style.borderColor = "${HOVER_BORDER_COLOR}"; this.style.backgroundColor = "${HOVER_BG_COLOR}"; };
            repoLink.onmouseout = function() { this.style.borderColor = "${BORDER_COLOR}"; this.style.backgroundColor = "transparent"; };
            
            // Insert links in correct order
            menuBar.insertBefore(repoLink, menuBar.firstChild);
            menuBar.insertBefore(shopLink, menuBar.firstChild);
        }
    }, ${NAVBAR_INJECTION_DELAY});
});
</script>
EOF
}

# Function to build navbar into HTML files
build_navbar_into_files() {
    local build_dir="$1"
    
    echo " Building configurable navbar links..."
    
    # Generate the JavaScript code
    local navbar_js=$(generate_navbar_js)
    
    # Create temporary file with the JavaScript
    local temp_js_file=$(mktemp)
    echo "$navbar_js" > "$temp_js_file"
    
    # Inject into all HTML files
    for html_file in "${build_dir}"/*.html "${build_dir}"/*/*.html "${build_dir}"/*/*/*.html; do
        if [ -f "$html_file" ]; then
            # Insert navbar JavaScript before closing body tag (without escape characters)
            sed -i "/<\/body>/r $temp_js_file" "$html_file"
        fi
    done
    
    # Clean up
    rm "$temp_js_file"
    
    echo "Navbar build completed using configuration variables!"
}
