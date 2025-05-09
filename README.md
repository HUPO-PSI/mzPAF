# mzPAF Peak Annotation Format

## About

mzPAF is a specification for a fragment ion peak annotation format for mass spectra, focused on
peptides. This provides for a standardized format for describing the origin of fragment ions to be
used in spectral libraries, other formats that aim to describe fragment ions, and software tools
that annotate fragment ions.

- Official mzPAF homepage: [psidev.info/mzPAF](https://psidev.info/mzPAF)
- mzPAF documentation: [mzpaf.readthedocs.io](https://mzpaf.readthedocs.io)

## Status

_Updated: 2024-10-15_

The specification has been resubmitted to the PSI Document Process and is undergoing final
community review. It is anticipated to become a formal PSI standard near the end of 2024.

- The current DRAFT specification: [mzPAF_specification_v1.0-draft15.pdf](https://github.com/HUPO-PSI/mzPAF/blob/main/specification/mzPAF_specification_v1.0-draft15.pdf?raw=true)
- Example annotated spectra: [Examples](https://github.com/HUPO-PSI/mzPAF/tree/main/examples)

## In short

- mzPAF is a single string of characters, case sensitive, without length limit
- Multiple possible explanations are comma-separated
- Deltas of observed – theoretical _m/z_ values are prefixed with a slash (`/`)
- Confidence of annotations are prefixed with an asterisk (`*`)

The basic format of each annotation is:

```
annotation1/delta,annotation2/delta,...
```

or:

```
annotation1/delta*confidence,annotation2/delta*confidence,...
```

For example:

```
b2-H2O/3.2ppm,b4-H2O^2/3.2ppm
```

or:

```
b2-H2O/3.2ppm*0.75,b4-H2O^2/3.2ppm*0.25
```

mzPAF supports:

- Annotations of multiple analytes: `1@y12/0.13,2@b9-NH3/0.23`
- Mass deltas in ppm instead of _m/z_ unit: `y1/-1.4ppm`
- Confidence levels per annotation: `y1/-1.4ppm*0.75`
- Advanced ion notation: `[ion type](neutral loss)(isotope)(adduct type)(charge)`, e.g.: `y4-H2O+2i[M+H+Na]^2`:
  - Ion types:
    - Peptide ion series (a, b, c, x, y, z): `y4`
    - Unknown ions: `?`
    - Immonium ions: `IY`
    - Internal fragment ions: `m3:6`
    - Intact precursor ions: `p^2`
    - A set of reference ions: `r[TMT127N]`
    - Named compounds: `_{Urocanic Acid}`
    - Chemical formulas: `f{C16H22O}`
    - Smiles: `s{CN=C=O}[M+H]`
    - Embedded ProForma annotations: `0@b2{LC[Carbamidomethyl]}`
  - Neutral gains and losses: `y2+CO-H2O`
  - Isotopes: `y2+2i`
  - Adduct types: `y2[M+H]`
  - Charge states: `^2`
- Multiple peaks per annotation: `&y7/-0.001` and `y7/0.000*0.95`

Read the
[full DRAFT specificiation](https://github.com/HUPO-PSI/mzPAF/blob/main/specification/mzPAF_specification_v1.0-draft14.docx?raw=true)
for more details and examples.

## Getting started

### mzPAF in Python

The [mzPAF Python package](https://mzpaf.readthedocs.io/en/latest/implementations/python/) can
parse mzPAF strings into their components, convert to the JSON representation, or serialize back
to an mzPAF string.

```python
>>> import mzpaf
>>> annotations = mzpaf.parse_annotation("b2-H2O/3.2ppm*0.75,b4-H2O^2/3.2ppm*0.25")
>>> print(annotations[0].to_json())
{'neutral_losses': ['-H2O'], 'isotope': 0, 'adducts': [], 'charge': 1, 'analyte_reference': None, 'mass_error': {'value': 3.2, 'unit': 'ppm'}, 'confidence': 0.75, 'molecule_description': {'series_label': 'peptide', 'series': 'b', 'position': 2, 'sequence': None}}
>>> print(anno[0].serialize())
'b2-H2O/3.2ppm*0.75'
```

Learn more at the
[package documentation](https://mzpaf.readthedocs.io/en/latest/implementations/python/).

### mzPAF regular expressions

The mzPAF specification includes regular expressions for parsing mzPAF strings. These can be used
in any programming language that supports regular expressions.

Learn more at the
[mzPAF regex documentation](https://mzpaf.readthedocs.io/en/latest/implementations/regex/).

### mzPAF Lark grammar

mzPAF has also been defined as a
[Lark grammar](https://mzpaf.readthedocs.io/en/latest/implementations/lark/).

### Links

- The mzPAF GitHub repo: [github.com/HUPO-PSI/mzPAF](https://github.com/HUPO-PSI/mzPAF)
- The GitHub repo for the related mzSpecLib standard: [github.com/HUPO-PSI/mzSpecLib](https://github.com/HUPO-PSI/mzSpecLib)
- HUPO-PSI homepage: [psidev.info](https://www.psidev.info/)
