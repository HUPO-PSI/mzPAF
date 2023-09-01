# mzPAF specification reference data files

The mzPAF specification uses these files as auxiliary reference data so that enumerated values can be extended without altering the specification document.

- reference_molecules.json - Easily software parsable list of "reference molecules" often seen in peptide fragmentation spectra, but
  not normal peptide fragments, including isobaric labeling reagent related molecules, monosaccharides, nucleotides, etc. These
  molecules may be inidividual charged ions (typically protonated), or may be used as neutral losses as appropriate.

- reference_molecules.md - Human-readable markdown tabular version of reference_molecules.json

- reference_molecule_schema.json - JSON schema for reference_molecules.json

- reference_mol_to_md.py - Python script to transform reference_molecules.json into a markdown table