"""Setup project."""

from setuptools import setup, find_packages

setup(
    name='mzpaf',
    packages=find_packages(exclude=('tests',)),
    version='0.1.0-alpha',
    description='HUPO-PSI Peptide peak annotation format',
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Development Status :: 3 - Alpha"
    ],
)
