#!/usr/bin/env python3
"""
Simple documentation builder for deploy-to-pages.sh
Builds mdBook documentation in software/book/book/ directory.
"""

import sys
import subprocess
from pathlib import Path

def run_command(command: str, cwd: Path) -> bool:
    """Run a shell command and return success status."""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Command failed: {command}")
        return False

def main():
    """Build documentation for GitHub Pages deployment."""
    # Get project root (2 levels up from scripts)
    project_root = Path(__file__).parent.parent.parent
    book_path = project_root / "software" / "book"
    extract_script = Path(__file__).parent / "smart-extract-docs.py"
    
    print("Building documentation...")
    
    # Step 1: Extract content from READMEs
    print("Extracting content from README files...")
    if not run_command(f"python3 {extract_script}", project_root):
        sys.exit(1)
    
    # Step 2: Build mdBook
    print("Building mdBook...")
    if not run_command("mdbook build", book_path):
        sys.exit(1)
    
    # Step 3: Verify build
    built_path = book_path / "book"
    if not built_path.exists():
        print("ERROR: Build directory not created")
        sys.exit(1)
    
    index_html = built_path / "index.html"
    if not index_html.exists():
        print("ERROR: index.html not found")
        sys.exit(1)
    
    print("SUCCESS: Documentation built successfully")
    print(f"Output directory: {built_path}")

if __name__ == "__main__":
    main()
