#!/usr/bin/env python3
"""
Generate GitHub profile SVGs for both light and dark modes.
GitHub-compatible version without filters or complex features.
"""

import datetime
from dateutil import relativedelta
from pathlib import Path


def calculate_age(birthday):
    """Calculate age from birthday and return formatted string."""
    diff = relativedelta.relativedelta(datetime.datetime.today(), birthday)
    years = f"{diff.years} year{'s' if diff.years != 1 else ''}"
    months = f"{diff.months} month{'s' if diff.months != 1 else ''}"
    days = f"{diff.days} day{'s' if diff.days != 1 else ''}"
    birthday_emoji = " 🎂" if diff.months == 0 and diff.days == 0 else ""
    return f"{years}, {months}, {days}{birthday_emoji}"


def generate_svg(age_data, mode="light"):
    """Generate GitHub-compatible SVG for the specified theme mode."""

    # Theme colors
    themes = {
        "light": {
            "bg": "#ffffff",
            "border": "#d0d7de",
            "header": "#0969da",
            "key": "#cf222e",
            "value": "#0969da",
            "text": "#24292f",
            "section": "#d73a49",
            "divider": "#d8dee4",
        },
        "dark": {
            "bg": "#0d1117",
            "border": "#30363d",
            "header": "#58a6ff",
            "key": "#ffa657",
            "value": "#79c0ff",
            "text": "#c9d1d9",
            "section": "#ffa657",
            "divider": "#21262d",
        }
    }

    c = themes[mode]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="500" viewBox="0 0 900 500">
<rect width="900" height="500" fill="{c['bg']}" rx="12"/>
<rect x="2" y="2" width="896" height="496" fill="none" stroke="{c['border']}" stroke-width="2" rx="10"/>

<!-- Header -->
<text x="30" y="45" fill="{c['header']}" font-size="28" font-weight="700" font-family="monospace">
Mohammad Sadegh Sirjani
</text>
<line x1="30" y1="60" x2="870" y2="60" stroke="{c['divider']}" stroke-width="2"/>

<!-- Profile -->
<g fill="{c['text']}" font-size="14" font-family="monospace">
<text x="50" y="95">
<tspan fill="{c['key']}" font-weight="600">⏱  Uptime:</tspan>
<tspan fill="{c['value']}" dx="10">{age_data}</tspan>
</text>

<text x="50" y="125">
<tspan fill="{c['key']}" font-weight="600">🌍 Origin:</tspan>
<tspan fill="{c['value']}" dx="17">Iran</tspan>
</text>

<text x="50" y="155">
<tspan fill="{c['key']}" font-weight="600">📍 Location:</tspan>
<tspan fill="{c['value']}" dx="6">San Antonio, Texas, USA</tspan>
</text>

<text x="50" y="185">
<tspan fill="{c['key']}" font-weight="600">🎓 University:</tspan>
<tspan fill="{c['value']}" dx="0">University of Texas at San Antonio</tspan>
</text>

<text x="50" y="215">
<tspan fill="{c['key']}" font-weight="600">💻 Major:</tspan>
<tspan fill="{c['value']}" dx="21">Computer Science</tspan>
</text>

<text x="50" y="245">
<tspan fill="{c['key']}" font-weight="600">🖥  OS:</tspan>
<tspan fill="{c['value']}" dx="36">macOS • Ubuntu • Windows</tspan>
</text>
</g>

<line x1="30" y1="270" x2="870" y2="270" stroke="{c['divider']}" stroke-width="2"/>

<!-- Left Column -->
<text x="50" y="305" fill="{c['section']}" font-size="16" font-weight="700" font-family="monospace">
💬 Languages
</text>

<g fill="{c['text']}" font-size="13" font-family="monospace">
<text x="70" y="335">
<tspan fill="{c['key']}" font-weight="600">code:</tspan>
<tspan fill="{c['value']}" dx="6">C# • Python • C • C++</tspan>
</text>

<text x="70" y="360">
<tspan fill="{c['key']}" font-weight="600">speak:</tspan>
<tspan fill="{c['value']}" dx="6">English • Persian</tspan>
</text>
</g>

<text x="50" y="400" fill="{c['section']}" font-size="16" font-weight="700" font-family="monospace">
🎯 Interests
</text>

<g fill="{c['text']}" font-size="13" font-family="monospace">
<text x="70" y="430">
<tspan fill="{c['key']}" font-weight="600">software:</tspan>
<tspan fill="{c['value']}" dx="6">Problem Solving</tspan>
</text>

<text x="70" y="455">
<tspan fill="{c['key']}" font-weight="600">hobbies:</tspan>
<tspan fill="{c['value']}" dx="7">Dark Soulsing • Working Out</tspan>
</text>
</g>

<!-- Right Column -->
<text x="480" y="305" fill="{c['section']}" font-size="16" font-weight="700" font-family="monospace">
📬 Connect
</text>

<g fill="{c['text']}" font-size="13" font-family="monospace">
<text x="500" y="335" fill="{c['key']}" font-weight="600">✉  email:</text>
<text x="510" y="355" fill="{c['value']}">mohammadsadegh.sirjani@utsa.edu</text>

<text x="500" y="390" fill="{c['key']}" font-weight="600">💼 linkedin:</text>
<text x="510" y="410" fill="{c['value']}">Mohammad Sadegh Sirjani</text>

<text x="500" y="445" fill="{c['key']}" font-weight="600">🌐 website:</text>
<text x="510" y="465" fill="{c['value']}">msadeqsirjani.com</text>
</g>

<!-- Footer -->
<text x="30" y="488" fill="{c['text']}" opacity="0.5" font-size="10" font-family="monospace">
Last updated: {datetime.datetime.now().strftime('%B %d, %Y')}
</text>

</svg>'''

    return svg


def main():
    """Generate both light and dark mode SVGs."""
    print("🎨 Generating GitHub-compatible Profile SVGs...\n")

    # Calculate age
    birthday = datetime.datetime(2000, 4, 27)
    age = calculate_age(birthday)

    # Create output directory
    output_dir = Path("docs")
    output_dir.mkdir(exist_ok=True)

    # Generate both themes
    for mode in ["light", "dark"]:
        svg_content = generate_svg(age, mode)
        output_file = output_dir / f"{mode}_mode.svg"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(svg_content)

        print(f"✓ Generated {output_file}")

    print(f"\n📅 Age: {age}")
    print("\n💡 Usage in README.md:")
    print("```markdown")
    print("![Profile](docs/light_mode.svg#gh-light-mode-only)")
    print("![Profile](docs/dark_mode.svg#gh-dark-mode-only)")
    print("```")


if __name__ == "__main__":
    main()
