"""Configuration file for the Sphinx documentation builder."""

# Scripts
import json
import shutil
from pathlib import Path

import jsonschema2md
import pandas as pd


CONF_DIR = Path(__file__).parent
STATIC_DIR = CONF_DIR / '_static'
IMG_DIR = STATIC_DIR / 'img'


def get_jsonschema_docs(input_json, output_markdown):
    """Generate markdown documentation from a JSON schema."""
    parser = jsonschema2md.Parser()
    with open(input_json, encoding="utf-8") as f_in:
        output_md = parser.parse_schema(json.load(f_in))

    with open(output_markdown, "w", encoding="utf-8") as f_out:
        f_out.writelines(output_md)


def get_reference_molecules_md(input_json, output_markdown):
    """Generate a markdown table of reference molecules."""
    df = pd.read_json(input_json).T
    buf = df.to_markdown().replace(' nan ', '     ')
    with open(output_markdown, 'wt') as fh:
        fh.write(buf)


get_jsonschema_docs(
    "../specification/annotation-schema.json",
    "../specification/annotation-schema.md"
)
get_jsonschema_docs(
    "../specification/reference_data/reference_molecule_schema.json",
    "../specification/reference_data/reference_molecule_schema.md"
)

get_reference_molecules_md(
    "../specification/reference_data/reference_molecules.json",
    "../specification/reference_data/reference_molecules.md"
)

if not STATIC_DIR.exists():
    STATIC_DIR.mkdir(exist_ok=True)

if not IMG_DIR.exists():
    IMG_DIR.mkdir(exist_ok=True)

if not (IMG_DIR / "lark-railroad-diagram.svg").exists():
    shutil.copy(
        "../specification/grammars/schema_images/Annotation.svg",
        (IMG_DIR / "lark-railroad-diagram.svg"),
    )


# Project information
project = "mzPAF"
author = "HUPO-PSI"
github_project_url = "https://github.com/HUPO-PSI/mzPAF"
github_doc_root = "https://github.com/HUPO-PSI/mzPAF/tree/master/docs"

# General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_click.ext",
    "myst_parser",
]
source_suffix = [".rst", ".md"]
master_doc = "index"
exclude_patterns = ["_build"]

# Options for HTML output
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/HUPO-PSI/mzPAF",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        }
    ]
}

# Autodoc options
autodoc_default_options = {"members": True, "show-inheritance": True}
autodoc_member_order = "bysource"
autodoc_typehints = "description"
autoclass_content = "init"

# Intersphinx options
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "psims": ("https://mobiusklein.github.io/psims/docs/build/html/", None),
    "pyteomics": ("https://pyteomics.readthedocs.io/en/stable/", None),
    "mzspeclib": ("https://mzspeclib.readthedocs.io/en/latest/", None),
}


def setup(app):
    config = {"enable_eval_rst": True}  # noqa: F841
