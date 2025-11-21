#!/usr/bin/env python3
"""
Smart content extractor that does NOT duplicate titles.
Extracts ONLY useful content without altering the original READMEs.
"""

import os
import json
import re
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Any

def clean_emoji_from_title(text: str) -> str:
    """Remove emoji characters from text for clean URLs."""
    # Remove emoji characters (broader range to include ⚙️ and other symbols)
    cleaned = re.sub(r'[\U0001F000-\U0001F9FF]', '', text)  # Extended range
    cleaned = re.sub(r'[\u2600-\u26FF]', '', cleaned)      # Additional symbol range  
    cleaned = re.sub(r'[\u2700-\u27BF]', '', cleaned)      # Dingbats range (includes ⚙️)
    # Remove extra whitespace
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned if cleaned else text

def encode_url_spaces(url: str) -> str:
    """Encode spaces in URLs for better web compatibility."""
    return url.replace(' ', '%20')

def get_github_repo_url():
    """Try to detect GitHub repository URL from git remote."""
    try:
        import subprocess
        result = subprocess.run(['git', 'remote', 'get-url', 'origin'], 
                              capture_output=True, text=True, cwd=Path.cwd())
        if result.returncode == 0:
            url = result.stdout.strip()
            # Convert SSH to HTTPS format
            if url.startswith('git@github.com:'):
                url = url.replace('git@github.com:', 'https://github.com/')
            if url.endswith('.git'):
                url = url[:-4]
            return url
    except:
        pass
    return None

def get_github_pages_url():
    """Generate GitHub Pages URL from repository URL."""
    repo_url = get_github_repo_url()
    if repo_url and 'github.com' in repo_url:
        # Extract owner and repo from https://github.com/owner/repo
        parts = repo_url.split('/')
        if len(parts) >= 5:
            owner = parts[-2]
            repo = parts[-1]
            return f"https://{owner}.github.io/{repo}"
    return None

def print_status(message: str, emoji: str = ""):
    """Print a formatted status message."""
    print(f"{message}")

def read_file_content(file_path):
    """Read content from a file with error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
        return ""

def write_file_content(file_path, content):
    """Write content to a file with proper directory creation."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")
        return False

def fix_image_sizes(content: str) -> str:
    """Fix image sizes for better display in mdBook, preserving HTML link structure."""
    
    # First, handle HTML link structures with images - these should be preserved as-is but with better styling
    # Pattern: <a href="..."><img src="..." width="..." ...><br/> Text</a>
    content = re.sub(
        r'<a href="([^"]+)"><img src="([^"]+)"[^>]*><br/>\s*([^<]*)</a>',
        r'<div align="center"><a href="\1"><img src="\2" style="max-width: 500px; height: auto;" alt="\3"><br/> \3</a></div>',
        content
    )
    
    # Handle standalone img tags with width attribute (not part of links)
    # We'll temporarily mark linked images to avoid processing them
    temp_placeholder = "___LINKED_IMG___"
    
    # Temporarily replace linked images
    linked_images = []
    def store_linked_img(match):
        linked_images.append(match.group(0))
        return f"{temp_placeholder}{len(linked_images)-1}___"
    
    content = re.sub(r'<a[^>]*>.*?<img[^>]*>.*?</a>', store_linked_img, content, flags=re.DOTALL)
    
    # Now process standalone images
    content = re.sub(
        r'<img src="([^"]+)" width="[^"]*"([^>]*)>',
        r'<img src="\1" style="max-width: 80%; height: auto;"\2>',
        content
    )
    
    # Fix other standalone HTML img tags
    content = re.sub(
        r'<img src="([^"]+)" alt="([^"]*)"[^>]*>',
        r'<div align="center"><img src="\1" alt="\2" style="max-width: 80%; height: auto;"></div>',
        content
    )
    
    # Fix markdown images by adding HTML wrapper for sizing
    content = re.sub(
        r'!\[([^\]]*)\]\(([^)]+)\)',
        r'<div align="center"><img src="\2" alt="\1" style="max-width: 70%; height: auto;"></div>',
        content
    )
    
    # Restore linked images
    for i, linked_img in enumerate(linked_images):
        content = content.replace(f"{temp_placeholder}{i}___", linked_img)
    
    return content

def preserve_external_links(content: str) -> str:
    """Preserve HTML and PDF links as-is, fix local resource paths."""
    
    # Fix local image src references to use resources folder with URL encoding
    def fix_src_resources(match):
        filename = match.group(1)
        encoded_filename = encode_url_spaces(filename)
        return f'src="../resources/{encoded_filename}"'
    
    content = re.sub(
        r'src="\./resources/([^"]+)"',
        fix_src_resources,
        content
    )
    
    content = re.sub(
        r'src="resources/([^"]+)"',
        lambda m: f'src="../resources/{encode_url_spaces(m.group(1))}"',
        content
    )
    
    # Fix href links to local resources with URL encoding
    def fix_href_resources(match):
        filename = match.group(1)
        encoded_filename = encode_url_spaces(filename)
        return f'href="../resources/{encoded_filename}"'
    
    content = re.sub(
        r'href="\./resources/([^"]+)"',
        fix_href_resources,
        content
    )
    
    # Fix href links to PDF files in root hardware directory
    content = re.sub(
        r'href="\./([^"]+\.pdf)"',
        r'href="../resources/\1"',
        content
    )
    
    # Fix markdown image references
    content = re.sub(
        r'!\[([^\]]*)\]\(\./resources/([^)]+)\)',
        r'![\1](../resources/\2)',
        content
    )
    
    return content

def extract_content_without_main_title(content: str, page_title: str) -> str:
    """Extract content removing the main title to avoid duplication."""
    
    # Clean YAML frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL | re.MULTILINE)
    
    # Remove HTML comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Remove template instructions
    template_phrases = [
        r'This file serves as an input.*?(?=\n#|\n\n|$)',
        r'Fill in each section.*?(?=\n#|\n\n|$)',
        r'FILL HERE.*?(?=\n|\s)',
        r'========================================.*?========================================',
        r'Edita los valores.*?(?=\n|\s)',
        r'El formato se mantendrá.*?(?=\n|\s)'
    ]
    
    for phrase in template_phrases:
        content = re.sub(phrase, '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Split into lines and process
    lines = content.split('\n')
    result_lines = []
    skip_first_title = True
    
    for line in lines:
        # Skip the first main title (# Title) to avoid duplication
        if skip_first_title and line.strip().startswith('# '):
            skip_first_title = False
            continue
        
        # Add all other content
        result_lines.append(line)
    
    # Clean up multiple empty lines
    result = '\n'.join(result_lines)
    result = re.sub(r'\n\s*\n\s*\n+', '\n\n', result)
    
    # Fix image paths
    result = re.sub(r'hardware/resources/', 'resources/', result)
    result = re.sub(r'\.\./\.\./\.\./\.\./hardware/resources/', 'resources/', result)
    
    # Preserve external links and fix local paths
    result = preserve_external_links(result)
    
    # Fix image sizes
    result = fix_image_sizes(result)
    
    return result.strip()

def process_main_readme() -> str:
    """Process main README extracting only content after the main title."""
    
    readme_path = Path.cwd() / "README.md"
    if not readme_path.exists():
        return "No main README found. Please create a README.md file in the project root."
    
    content = readme_path.read_text(encoding='utf-8', errors='ignore')
    
    # Extract the project title from the first # heading
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    project_title = title_match.group(1).strip() if title_match else "Project"
    
    # Extract content after the main title
    extracted = extract_content_without_main_title(content, "Introduction")
    
    # For introduction.md, fix paths to use resources/ (relative to src directory)
    extracted = re.sub(r'src="\.\./resources/', 'src="resources/', extracted)
    extracted = re.sub(r'href="\.\./resources/', 'href="resources/', extracted)
    extracted = re.sub(r'src="\./', 'src="resources/', extracted)
    extracted = re.sub(r'href="\./', 'href="resources/', extracted)
    
    return f"# {project_title}\n\n{extracted}"

def process_hardware_readme() -> Dict[str, str]:
    """Process hardware README extracting sections without title duplication."""
    
    hardware_path = Path.cwd() / "hardware" / "README.md"
    pages = {}
    
    if not hardware_path.exists():
        # Create minimal default structure if no README exists
        pages["overview.md"] = """# Hardware Overview

No hardware README.md found. Please create hardware/README.md with your hardware documentation.
"""
        return pages
    
    content = hardware_path.read_text(encoding='utf-8', errors='ignore')
    
    # Create main hardware overview page
    clean_content = extract_content_without_main_title(content, "Hardware")
    pages["overview.md"] = f"# Hardware Overview\n\n{clean_content}"
    
    # Extract specific sections for individual pages from original content
    sections = {}
    
    # Look for section headers and extract their content
    section_matches = list(re.finditer(r'^## (.+?)$', content, re.MULTILINE))
    
    for i, match in enumerate(section_matches):
        section_title = match.group(1).strip()
        # Clean the title for key generation (remove emojis for clean URLs)
        clean_title = clean_emoji_from_title(section_title)
        section_start = match.end()
        
        # Find the end of this section (start of next section or end of content)
        if i + 1 < len(section_matches):
            section_end = section_matches[i + 1].start()
        else:
            section_end = len(content)
        
        section_content = content[section_start:section_end].strip()
        sections[clean_title.lower().replace(' ', '_').replace('-', '_')] = section_content
    
    # Create pages from sections found in README
    for section_key, section_content in sections.items():
        if section_content.strip():  # Only create if there's content
            # Clean section name for filename
            clean_section_name = section_key.replace('_', '-')
            section_display_name = section_key.replace('_', ' ').title()
            
            # Process content to fix images and links
            processed_content = preserve_external_links(fix_image_sizes(section_content))
            
            pages[f"{clean_section_name}.md"] = f"# {section_display_name}\n\n{processed_content}"
    
    return pages

def process_software_content() -> Dict[str, str]:
    """Process software documentation extracting examples from files."""
    
    pages = {}
    
    # Process software README.md (Getting Started)
    software_readme_path = Path.cwd() / "software" / "README.md"
    
    if software_readme_path.exists():
        content = software_readme_path.read_text(encoding='utf-8', errors='ignore')
        # Extract content without main title duplication
        clean_content = extract_content_without_main_title(content, "Getting Started")
        pages["getting-started.md"] = f"# Getting Started\n\n{clean_content}"
    else:
        # Fallback if no README exists
        pages["getting-started.md"] = """# Getting Started

Please create a software/README.md file with getting started instructions.
"""
    
    # Extract real code examples from files
    examples_content = "# Examples\n\n"
    
    # Add examples overview
    examples_content += """## Arduino/C++ Examples

The following examples demonstrate various features of this development board.

"""
    
    # Process C/Arduino examples
    c_example_dir = Path.cwd() / "software" / "examples" / "c"
    github_url = get_github_repo_url()
    
    if c_example_dir.exists():
        # First, look for .ino files directly in the c/ directory (current structure)
        for code_file in c_example_dir.glob("*.ino"):
            try:
                code_content = code_file.read_text(encoding='utf-8', errors='ignore')
                
                # Extract first 20 lines as preview
                lines = code_content.split('\n')
                preview_lines = lines[:20]
                preview = '\n'.join(preview_lines)
                
                # Generate GitHub link if repository URL is available
                code_link = ""
                if github_url:
                    relative_path = f"software/examples/c/{code_file.name}"
                    code_link = f"[See complete code on GitHub]({github_url}/blob/main/{relative_path})"
                else:
                    code_link = f"[See complete code on GitHub: {code_file.name}](#{code_file.stem.lower()})"
                
                examples_content += f"""### {code_file.stem}
```cpp
{preview}
```
{code_link}

"""
            except Exception as e:
                continue
        
        # Then look for .ino files in subdirectories (backward compatibility)
        for example_dir in c_example_dir.iterdir():
            if example_dir.is_dir():
                for code_file in example_dir.rglob("*.ino"):
                    try:
                        code_content = code_file.read_text(encoding='utf-8', errors='ignore')
                        
                        # Extract first 20 lines as preview
                        lines = code_content.split('\n')
                        preview_lines = lines[:20]
                        preview = '\n'.join(preview_lines)
                        
                        # Generate GitHub link if repository URL is available
                        code_link = ""
                        if github_url:
                            # Create GitHub blob URL for the file
                            relative_path = f"software/examples/c/{example_dir.name}/{code_file.name}"
                            code_link = f"[See complete code on GitHub]({github_url}/blob/main/{relative_path})"
                        else:
                            code_link = f"[See complete code on GitHub: {code_file.name}](#{example_dir.name.lower()})"
                        
                        examples_content += f"""### {example_dir.name}: {code_file.name}
```cpp
{preview}
```
{code_link}

"""
                    except Exception as e:
                        continue
    
    # Process MicroPython examples
    micropython_example_dir = Path.cwd() / "software" / "examples" / "micropython"
    
    if micropython_example_dir.exists():
        examples_content += """

## MicroPython Examples

The following MicroPython examples demonstrate usage with microcontrollers.

"""
        
        # Look for .py files in micropython directory
        for code_file in micropython_example_dir.glob("*.py"):
            try:
                code_content = code_file.read_text(encoding='utf-8', errors='ignore')
                
                # Extract first 20 lines as preview
                lines = code_content.split('\n')
                preview_lines = lines[:20]
                preview = '\n'.join(preview_lines)
                
                # Generate GitHub link if repository URL is available
                code_link = ""
                if github_url:
                    relative_path = f"software/examples/micropython/{code_file.name}"
                    code_link = f"[See complete code on GitHub]({github_url}/blob/main/{relative_path})"
                else:
                    code_link = f"[See complete code on GitHub: {code_file.name}](#{code_file.stem.lower()})"
                
                examples_content += f"""### {code_file.stem}
```python
{preview}
```
{code_link}

"""
            except Exception as e:
                continue
    
    # Also check regular python directory for backward compatibility
    python_example_dir = Path.cwd() / "software" / "examples" / "python"
    if python_example_dir.exists():
        if not micropython_example_dir.exists():
            examples_content += """

## Python Examples

The following Python examples demonstrate usage with the sensor.

"""
        
        for code_file in python_example_dir.glob("*.py"):
            try:
                code_content = code_file.read_text(encoding='utf-8', errors='ignore')
                
                # Extract first 20 lines as preview
                lines = code_content.split('\n')
                preview_lines = lines[:20]
                preview = '\n'.join(preview_lines)
                
                # Generate GitHub link if repository URL is available
                code_link = ""
                if github_url:
                    relative_path = f"software/examples/python/{code_file.name}"
                    code_link = f"[See complete code on GitHub]({github_url}/blob/main/{relative_path})"
                else:
                    code_link = f"[See complete code on GitHub: {code_file.name}](#{code_file.stem.lower()})"
                
                examples_content += f"""### {code_file.stem}
```python
{preview}
```
{code_link}

"""
            except Exception as e:
                continue
    
    # Add default message if no examples found
    if examples_content == "# Examples\n\n## Arduino/C++ Examples\n\nThe following examples demonstrate various features of the UNIT JUN R3 Development Board.\n\n":
        examples_content += """No code examples found. Please add example files to software/examples/ directory.

## Directory Structure Supported:
```
software/examples/
├── c/
│   ├── light_sensor.ino        # Direct files (current structure)
│   ├── example1/               # Or in subdirectories
│   │   └── example1.ino
│   └── example2/
│       └── example2.ino
├── micropython/                # Preferred for MicroPython
│   ├── light_sensor.py
│   └── other_example.py
└── python/                     # Alternative Python location
    ├── example1.py
    └── example2.py
```
"""
    
    pages["examples.md"] = examples_content
    
    # Create individual example pages
    pages["examples/arduino.md"] = """# Arduino Examples

This section contains Arduino/C++ examples extracted from the software/examples/c/ directory.

## Supported Structures
The system detects examples in the following locations:
- Direct files: `software/examples/c/example_name.ino`
- Subdirectories: `software/examples/c/example_name/example_name.ino`

The examples will be automatically detected and displayed here.
"""

    pages["examples/micropython.md"] = """# MicroPython Examples

This section contains MicroPython examples extracted from the software/examples/ directory.

## Supported Structures
The system detects Python examples in the following locations:
- Preferred: `software/examples/micropython/example_name.py`
- Alternative: `software/examples/python/example_name.py`

MicroPython examples will be automatically detected and displayed here.
"""
    
    return pages

def process_license() -> str:
    """Extract license content and create license page."""
    
    license_path = Path.cwd() / "LICENSE"
    
    if license_path.exists():
        license_content = license_path.read_text(encoding='utf-8', errors='ignore')
        return f"""# License

{license_content}

---

*This project is licensed under the MIT License - see the LICENSE file for details.*
"""
    else:
        return """# License

No license file found in the repository.
"""

def create_resources_page() -> str:
    """Create resources page with hardware documentation and product PDF."""
    
    # Detect schematic PDF dynamically
    project_root = Path.cwd()
    schematic_link = None
    schematic_filename = None
    
    # Search for unit_sch_*.pdf in hardware and hardware/resources directories
    search_paths = [
        project_root / "hardware",
        project_root / "hardware" / "resources"
    ]
    
    for search_path in search_paths:
        if search_path.exists():
            for pdf_file in search_path.glob("unit_sch_*.pdf"):
                schematic_filename = pdf_file.name
                schematic_link = f"resources/{schematic_filename}"
                break
        if schematic_link:
            break
    
    # Find product PDF in hardware directory
    hardware_dir = project_root / "hardware"
    product_pdf = None
    
    # Look for unit_product_*.pdf
    for pdf_file in hardware_dir.glob("unit_product_*.pdf"):
        product_pdf = pdf_file
        break
    
    resources_content = """# Hardware Documentation & Resources

## Product Datasheet

Official product documentation with complete technical specifications.
"""
    
    # Add product PDF if found
    if product_pdf:
        product_filename = product_pdf.name
        resources_content += f"""
**[Download Product Datasheet](hardware/{product_filename})** - Official PDF documentation

"""
    else:
        resources_content += """
Product datasheet not found in hardware directory.

"""
    
    resources_content += """
## Hardware Resources
"""
    
    if schematic_link and schematic_filename:
        resources_content += f"- [Schematic Diagram]({schematic_link}) - Complete circuit schematic\n"
    else:
        resources_content += "- Schematic Diagram - Not found (looking for unit_sch_*.pdf)\n"
    
    resources_content += """- [Pinout Reference](hardware/pinout.md) - Pin configuration details

"""
    
    # Find product PDF in hardware directory
    hardware_dir = project_root / "hardware"
    product_pdf = None
    
    # Look for unit_product_*.pdf
    for pdf_file in hardware_dir.glob("unit_product_*.pdf"):
        product_pdf = pdf_file
        break
    
    resources_content = """# Hardware Documentation & Resources

## Product Datasheet

Official product documentation with complete technical specifications.
"""
    
    # Add product PDF if found
    if product_pdf:
        product_filename = product_pdf.name
        resources_content += f"""
**[Download Product Datasheet](hardware/{product_filename})** - Official PDF documentation

"""
    else:
        resources_content += """
Product datasheet not found in hardware directory.

"""
    
    resources_content += """
## Hardware Resources
"""
    
    if schematic_link and schematic_filename:
        resources_content += f"- [Schematic Diagram]({schematic_link}) - Complete circuit schematic\n"
    else:
        resources_content += "- Schematic Diagram - Not found (looking for unit_sch_*.pdf)\n"
    
    resources_content += """- [Pinout Reference](hardware/pinout.md) - Pin configuration details

## Software Resources
- [Getting Started Guide](software/getting-started.md) - Setup and first steps  
- [Code Examples](software/examples.md) - Arduino sketches and demos
- [Development Setup](software/getting-started.md#development-environment) - IDE configuration

## External Links
"""

    # Add GitHub link if available
    github_url = get_github_repo_url()
    if github_url:
        resources_content += f"- [Source Code Repository]({github_url}) - Complete project files\n"
    
    resources_content += """
## Quick Reference

| Resource | Description | Link |
|----------|-------------|------|"""
    
    # Add product PDF to quick reference
    if product_pdf:
        product_filename = product_pdf.name
        resources_content += f"""
| **Product Datasheet** | Official technical documentation | [PDF](hardware/{product_filename}) |"""
    
    # Add schematic
    if schematic_link and schematic_filename:
        resources_content += f"""
| **Schematic** | Circuit diagram | [PDF]({schematic_link}) |"""
    else:
        resources_content += f"""
| **Schematic** | Circuit diagram | Not found |"""
    
    resources_content += """
| **Pinout** | Pin configuration | [View](hardware/pinout.md) |
| **Examples** | Code samples | [View](software/examples.md) |
| **Setup Guide** | Getting started | [View](software/getting-started.md) |

---

*Hardware documentation extracted from project files.*
"""
    
    return resources_content

def copy_resources():
    """Copy image resources and PDFs without duplication."""
    
    project_root = Path.cwd()
    book_path = project_root / "software" / "book"
    hardware_resources = project_root / "hardware" / "resources"
    hardware_dir = project_root / "hardware"
    docs_dir = project_root / "docs"
    
    # Copy images
    if hardware_resources.exists():
        # Copy to both locations for maximum compatibility
        targets = [
            book_path / "src" / "resources",
            book_path / "src" / "hardware" / "resources"
        ]
        
        copied = 0
        for target_dir in targets:
            target_dir.mkdir(parents=True, exist_ok=True)
            
            for resource_file in hardware_resources.rglob("*"):
                if resource_file.is_file():
                    try:
                        target_file = target_dir / resource_file.name
                        shutil.copy2(resource_file, target_file)
                        if target_dir == targets[0]:  # Count only once
                            copied += 1
                    except Exception:
                        pass
        
        if copied > 0:
            print_status(f"Imágenes copiadas: {copied} archivos")
    
    # Copy PDFs from hardware directory (including product PDF)
    hardware_target = book_path / "src" / "hardware"
    hardware_target.mkdir(parents=True, exist_ok=True)
    
    pdf_copied = 0
    
    # Copy all PDFs from hardware directory
    if hardware_dir.exists():
        for pdf_file in hardware_dir.glob("*.pdf"):
            try:
                target_file = hardware_target / pdf_file.name
                shutil.copy2(pdf_file, target_file)
                pdf_copied += 1
                print_status(f"Copied hardware PDF: {pdf_file.name}")
            except Exception as e:
                print_status(f"Warning: Could not copy {pdf_file.name}: {e}")
    
    # Also copy to resources for compatibility
    pdf_targets = [
        book_path / "src" / "resources",
        book_path / "src" / "hardware" / "resources"
    ]
    
    pdf_sources = [docs_dir, hardware_dir]  # Add hardware_dir as PDF source
    
    for source_dir in pdf_sources:
        if source_dir.exists():
            for pdf_file in source_dir.glob("*.pdf"):
                for target_dir in pdf_targets:
                    target_dir.mkdir(parents=True, exist_ok=True)
                    try:
                        target_file = target_dir / pdf_file.name
                        shutil.copy2(pdf_file, target_file)
                        if target_dir == pdf_targets[0]:  # Count only once
                            pdf_copied += 1
                    except Exception:
                        pass
    
    if pdf_copied > 0:
        print_status(f"PDFs copiados: {pdf_copied} archivos")
    
    return copied + pdf_copied

def create_summary() -> str:
    """Create SUMMARY.md based on actually generated content."""
    
    summary = """# Summary

[Introduction](./introduction.md)

# Hardware

- [Overview](./hardware/overview.md)"""
    
    # Add hardware sections dynamically based on what was extracted
    hardware_path = Path.cwd() / "hardware" / "README.md"
    if hardware_path.exists():
        content = hardware_path.read_text(encoding='utf-8', errors='ignore')
        section_matches = list(re.finditer(r'^## (.+?)$', content, re.MULTILINE))
        
        for match in section_matches:
            section_title = match.group(1).strip()
            # Use clean title for both display and filename
            clean_title = clean_emoji_from_title(section_title)
            clean_section_name = clean_title.lower().replace(' ', '-').replace('_', '-')
            summary += f"\n- [{clean_title}](./hardware/{clean_section_name}.md)"
    
    summary += """

# Software

- [Getting Started](./software/getting-started.md)
- [Examples](./software/examples.md)

# Resources

- [Datasheet & Documentation](./resources.md)

# Additional Information

- [License](./license.md)
"""
    
    return summary

def main():
    """Main execution."""
    
    print_status("Extrayendo contenido SIN duplicar títulos...")
    
    # Setup directories
    project_root = Path.cwd()
    book_path = project_root / "software" / "book"
    src_path = book_path / "src"
    
    (src_path / "hardware").mkdir(parents=True, exist_ok=True)
    (src_path / "software" / "examples").mkdir(parents=True, exist_ok=True)
    
    # Process content intelligently
    print_status("Procesando README principal...")
    intro_content = process_main_readme()
    
    print_status("Procesando hardware (sin duplicar títulos)...")
    hardware_pages = process_hardware_readme()
    
    print_status("Procesando software...")
    software_pages = process_software_content()
    
    print_status("Procesando licencia...")
    license_content = process_license()
    
    print_status("Creando página de recursos...")
    resources_content = create_resources_page()
    
    # Prepare all files
    all_files = {
        "introduction.md": intro_content,
        "license.md": license_content,
        "resources.md": resources_content,
        "SUMMARY.md": create_summary()
    }
    
    # Add hardware pages
    for filename, content in hardware_pages.items():
        all_files[f"hardware/{filename}"] = content
        
    # Add software pages  
    for filename, content in software_pages.items():
        all_files[f"software/{filename}"] = content
    
    # Write all files
    extraction_report = {
        "files_created": [],
        "files_failed": [],
        "resources_copied": 0
    }
    
    for filename, content in all_files.items():
        file_path = src_path / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            file_path.write_text(content, encoding='utf-8')
            extraction_report["files_created"].append(filename)
        except Exception as e:
            print(f"Error writing {filename}: {e}")
            extraction_report["files_failed"].append(filename)
    
    # Copy resources
    extraction_report["resources_copied"] = copy_resources()
    
    # Write extraction report
    report_path = book_path / "extraction_report.json"
    with open(report_path, 'w') as f:
        json.dump(extraction_report, f, indent=2)
    
    print_status(f"Generados {len(extraction_report['files_created'])} archivos SIN títulos duplicados", "✅")
    print_status("¡Contenido limpio y sin duplicaciones!", "🎉")
    
    return len(extraction_report['files_failed']) == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
