#!/usr/bin/env python3
"""
Generate GitHub profile SVGs for both light and dark modes.
GitHub-compatible version without filters or complex features.
"""

import datetime
from pathlib import Path


def generate_svg(mode="light"):
    """Generate GitHub-compatible SVG for the specified theme mode."""

    # Theme colors from portfolio CSS
    themes = {
        "light": {
            "bg": "#ffffff",
            "border": "#d1d5db",
            "header": "#1e40af",        # --accent-color (primary)
            "key": "#1e3a8a",           # --accent-hover (secondary - darker blue)
            "value": "#1e40af",         # --accent-color (primary)
            "text": "#1a1a1a",          # --text-color
            "section": "#1e3a8a",       # --accent-hover (secondary - darker blue)
            "divider": "#d1d5db",       # --border-color
        },
        "dark": {
            "bg": "#0f172a",            # --white (dark bg)
            "border": "#475569",        # --border-color
            "header": "#60a5fa",        # --accent-color (primary)
            "key": "#93c5fd",           # --accent-hover (secondary - lighter blue)
            "value": "#60a5fa",         # --accent-color (primary)
            "text": "#f9fafb",          # --text-color
            "section": "#93c5fd",       # --accent-hover (secondary - lighter blue)
            "divider": "#475569",       # --border-color
        }
    }

    c = themes[mode]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400">
<rect width="900" height="400" fill="{c['bg']}" rx="12"/>
<rect x="2" y="2" width="896" height="396" fill="none" stroke="{c['border']}" stroke-width="2" rx="10"/>

<!-- Header -->
<text x="30" y="45" fill="{c['header']}" font-size="28" font-weight="700" font-family="monospace">
Mohammad Sadegh Sirjani
</text>
<text x="30" y="75" fill="{c['text']}" font-size="14" font-family="monospace">
Ph.D. Student in Computer Science
</text>
<line x1="30" y1="95" x2="870" y2="95" stroke="{c['divider']}" stroke-width="2"/>

<!-- Education -->
<g fill="{c['text']}" font-size="14" font-family="monospace">
<text x="50" y="130">
<tspan fill="{c['key']}" font-weight="600">University:</tspan>
<tspan fill="{c['value']}" dx="10">University of Texas at San Antonio</tspan>
</text>

<text x="50" y="160">
<tspan fill="{c['key']}" font-weight="600">Location:</tspan>
<tspan fill="{c['value']}" dx="10">San Antonio, Texas, USA</tspan>
</text>
</g>

<line x1="30" y1="185" x2="870" y2="185" stroke="{c['divider']}" stroke-width="2"/>

<!-- Research Interests -->
<text x="50" y="220" fill="{c['section']}" font-size="16" font-weight="700" font-family="monospace">
Research Interests
</text>

<g fill="{c['text']}" font-size="13" font-family="monospace">
<text x="70" y="245">
<tspan fill="{c['value']}">IoT • Embedded Systems • Edge AI • Tiny AI</tspan>
</text>
<text x="70" y="265">
<tspan fill="{c['value']}">Energy Harvesting • Deep Learning</tspan>
</text>
</g>

<!-- Technical Skills -->
<text x="50" y="295" fill="{c['section']}" font-size="16" font-weight="700" font-family="monospace">
Technical Skills
</text>

<g fill="{c['text']}" font-size="13" font-family="monospace">
<text x="70" y="325">
<tspan fill="{c['key']}" font-weight="600">Languages:</tspan>
<tspan fill="{c['value']}" dx="6">Python • C • C++ • C#</tspan>
</text>

<text x="70" y="350">
<tspan fill="{c['key']}" font-weight="600">ML/DL:</tspan>
<tspan fill="{c['value']}" dx="6">TensorFlow • PyTorch • Keras • scikit-learn</tspan>
</text>
</g>

<!-- Contact -->
<text x="500" y="220" fill="{c['section']}" font-size="16" font-weight="700" font-family="monospace">
Contact
</text>

<g fill="{c['text']}" font-size="13" font-family="monospace">
<text x="520" y="250">
<tspan fill="{c['key']}" font-weight="600">Email:</tspan>
</text>
<text x="520" y="270" fill="{c['value']}">mohammadsadegh.sirjani@utsa.edu</text>

<text x="520" y="305">
<tspan fill="{c['key']}" font-weight="600">Website:</tspan>
</text>
<text x="520" y="325" fill="{c['value']}">msadeqsirjani.com</text>
</g>

<!-- Footer -->
<text x="30" y="385" fill="{c['text']}" opacity="0.5" font-size="10" font-family="monospace">
Last updated: {datetime.datetime.now().strftime('%B %d, %Y')}
</text>

</svg>'''

    return svg


def main():
    """Generate both light and dark mode SVGs."""
    print("Generating GitHub-compatible Profile SVGs...\n")

    # Create output directory
    output_dir = Path("docs")
    output_dir.mkdir(exist_ok=True)

    # Generate both themes
    for mode in ["light", "dark"]:
        svg_content = generate_svg(mode)
        output_file = output_dir / f"{mode}_mode.svg"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(svg_content)

        print(f"Generated {output_file}")

    print("\nUsage in README.md:")
    print("```markdown")
    print("![Profile](docs/light_mode.svg#gh-light-mode-only)")
    print("![Profile](docs/dark_mode.svg#gh-dark-mode-only)")
    print("```")


if __name__ == "__main__":
    main()
