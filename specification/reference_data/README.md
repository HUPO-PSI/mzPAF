# mzPAF specification reference data files

The mzPAF specification uses `specification/reference_data/reference_molecules.json` as auxiliary
reference data. In this way, the set of reference molecules can be extended without updating the
specification document itself.

The following files are available:

- `reference_molecules.json`: Software parsable list of "reference molecules" often seen in
  peptide fragmentation spectra, but not normal peptide fragments. This includes isobaric labeling
  reagent related molecules, monosaccharides, nucleotides, etc. These molecules may be individual
  charged ions (typically protonated), or may be used as neutral losses as appropriate.

- `reference_molecule_schema.json`: JSON schema defining the structure of the JSON file

A human-readable table with all reference molecules is available on https://mzpaf.readthedocs.io.
