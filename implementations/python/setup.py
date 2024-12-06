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
    version="0.2.0-beta",
    description="HUPO-PSI Peptide peak annotation format",
    classifiers=[
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Development Status :: 4 - Beta",
    ],
)
