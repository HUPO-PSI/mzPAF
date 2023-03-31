# `mzpaf`

A reference implementation of the mzPAF peak annotation parser based upon a
regular expression.

## Library Usage

The main interface is `parse_annotation`, a function which takes a string and returns
a list of zero or more `IonAnnotationBase` objects.

```python
from typing import List

import mzpaf

annotations: List[mzpaf.IonAnnotationBase] = mzpaf.parse_annotation("y1")

annot: mzpaf.PeptideFragmentIonAnnotation = annotation[0]
assert annot.series == 'y'
assert annot.position == 1
assert annot.charge == 1


annotations: List[mzpaf.IonAnnotationBase] = mzpaf.parse_annotation("p-H2O")

annot: mzpaf.PrecursorIonAnnotation = annotation[0]
assert annot.series == 'precursor'
assert annot.neutral_losses == ['-H2O']

annot, annot2 = mzpaf.parse_annotation("y6,b15+2i^3")
assert annot.position == 6

assert annot2.isotope == 2
assert annot2.charge == 3
```

## Script

See `../../examples/parse.py` for a script that reads from `STDIN` and writes out the
JSON data model.

```bash
python parse.py < Example2_ManyInternalFragments.txt
```
```json
{
  "annotations": [
    [
      {
        "adducts": [],
        "analyte_reference": "1",
        "charge": 1,
        "confidence": null,
        "isotope": 0,
        "mass_error": {
          "unit": "ppm",
          "value": 1.3
        },
        "molecule_description": {
          "amino_acid": "H",
          "series_label": "immonium"
        },
        "neutral_losses": []
      }
    ],
    ...
```