"""Sphinx configuration for the EduMirror user guide."""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

project = "EduMirror"
copyright = "2026, EduMirror"
author = "EduMirror"
release = ""

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sourcelink = False
html_title = "EduMirror 使用指南"
html_logo = "_static/edumirror-icon.png"
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "style_external_links": True,
}

language = "zh_CN"
source_suffix = {
    ".md": "markdown",
}
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_image",
    "substitution",
]

pygments_style = "sphinx"
