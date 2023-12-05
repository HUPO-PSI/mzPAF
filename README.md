# mzPAF Peak Annotation Format

## About

The mzPAF proposed standard is a specification for a fragment ion peak annotation format for mass spectra, focused on
peptides. This provides for a standardized format for describing the origin of fragment ions to be used in spectral
libraries, other formats that aim to describe fragment ions, and software tools that annotate fragment ions.

- Official mzPAF homepage: [psidev.info/mzPAF](https://psidev.info/mzPAF)
- mzPAF documentation: [mzpaf.readthedocs.io](https://mzpaf.readthedocs.io)


## Specification status

Updated: 2023-09-01

The specification has been resubmitted to the PSI Document Process and is undergoing final community review. Ratification to formally become a PSI standard is anticipated near the end of 2023.

Your comments and suggestions are still very much welcome. Please submit an issue at the repo to
provide your feedback and send an e-mail to the HUPO-PSI editor Sylvie Ricard-Blum
(sylvie.ricard-blum@univ-lyon1.fr).


## In short

- mzPAF is a single string of characters, case sensitive, without length limit
- Multiple possible explanations are separated with a comma
- Deltas of observed – theoretical *m/z* values are prefixed with a slash (`/`)
- Confidences can be provided for different annotations prefixed with an asterisk (`*`)

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
- Mass deltas in ppm instead of *m/z* unit: `y1/-1.4ppm`
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

Read the [full specificiation](https://mzpaf.readthedocs.io/specification) for more details and
examples.


### Available Materials
- The current DRAFT specification: https://github.com/HUPO-PSI/mzPAF/blob/main/specification/mzPAF_specification_v1.0-draft14.docx?raw=true
- The GitHub repo associated with mzPAF: https://github.com/HUPO-PSI/mzPAF
- The GitHub repo associated with the related mzSpecLib standard: https://github.com/HUPO-PSI/mzSpecLib

