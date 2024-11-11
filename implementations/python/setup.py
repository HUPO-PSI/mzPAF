"""Setup project."""

from setuptools import setup, find_packages

setup(
    name="mzpaf",
    packages=find_packages(exclude=("tests",)),
    requires=["pyteomics"],
    extras_require=dict(
        docs=[
            "sphinx",
            "sphinx-rtd-theme",
            "numpydoc>=1,<2",
            "sphinx_click",
            "myst-parser",
            "sphinx-autobuild",
            "pydata-sphinx-theme",
        ],
    ),
    version="0.2.0-alpha",
    description="HUPO-PSI Peptide peak annotation format",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Development Status :: 3 - Alpha",
    ],
)
