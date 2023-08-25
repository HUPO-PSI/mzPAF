import unittest
import json
import json

from pathlib import Path
import warnings

import jsonschema

from mzpaf import (
    parse_annotation, Unannotated, MassError, SMILESAnnotation,
    NamedCompoundIonAnnotation, FormulaAnnotation, PeptideFragmentIonAnnotation,
    ReferenceIonAnnotation, IonAnnotationBase)


SPEC_PATH = Path(__file__).parent / "../../../specification/"
SCHEMA_PATH = SPEC_PATH / "annotation-schema.json"

HAS_SCHEMA = SCHEMA_PATH.exists()

if HAS_SCHEMA:
    SCHEMA = json.load(SCHEMA_PATH.open('rt'))
else:
    SCHEMA = None


class TestAnnotationParser(unittest.TestCase):
    def _matches_schema(self, annotation: IonAnnotationBase):
        if not HAS_SCHEMA:
            warnings.warn(f"Cannot validate {annotation} against JSONSchema, {SCHEMA_PATH} does not exist")
            return True
        jsonschema.validate(annotation.to_json(), SCHEMA)
        return True

    def test_parse_unannotated(self):
        x, = parse_annotation("?^2")
        assert isinstance(x, Unannotated)
        self._matches_schema(x)

    def test_parse_annotation_complex(self):
        base = "b14"
        parsed = parse_annotation(base)[0]
        assert parsed.series == 'b'
        assert parsed.position == 14
        self._matches_schema(parsed)

        base += "-H2O-NH3+[Foo]"

        parsed = parse_annotation(base)[0]
        assert parsed.series == 'b'
        assert parsed.position == 14
        assert parsed.neutral_losses == ['-H2O', '-NH3', '[Foo]']
        self._matches_schema(parsed)

        base += "+2i"

        parsed = parse_annotation(base)[0]
        assert parsed.series == 'b'
        assert parsed.position == 14
        assert parsed.neutral_losses == ['-H2O', '-NH3', '[Foo]']
        assert parsed.isotope == 2
        self._matches_schema(parsed)

        base += "[M+NH4]^2"
        parsed = parse_annotation(base)[0]
        assert parsed.series == 'b'
        assert parsed.position == 14
        assert parsed.neutral_losses == ['-H2O', '-NH3', '[Foo]']
        assert parsed.isotope == 2
        assert parsed.charge == 2
        assert parsed.adducts == ["M", "NH4"]
        self._matches_schema(parsed)

        base += "/0.5ppm"

        parsed = parse_annotation(base)[0]
        assert parsed.series == 'b'
        assert parsed.position == 14
        assert parsed.neutral_losses == ['-H2O', '-NH3', '[Foo]']
        assert parsed.isotope == 2
        assert parsed.charge == 2
        assert parsed.adducts == ["M", "NH4"]
        assert parsed.mass_error == MassError(0.5, 'ppm')
        self._matches_schema(parsed)

        base = "2@" + base

        parsed = parse_annotation(base)[0]
        assert parsed.series == 'b'
        assert parsed.position == 14
        assert parsed.neutral_losses == ['-H2O', '-NH3', '[Foo]']
        assert parsed.isotope == 2
        assert parsed.charge == 2
        assert parsed.adducts == ["M", "NH4"]
        assert parsed.mass_error == MassError(0.5, 'ppm')
        assert parsed.analyte_reference == '2'
        assert parsed == base
        self._matches_schema(parsed)

        base = base + '*0.05'

        parsed = parse_annotation(base)[0]
        assert parsed.series == 'b'
        assert parsed.position == 14
        assert parsed.neutral_losses == ['-H2O', '-NH3', '[Foo]']
        assert parsed.isotope == 2
        assert parsed.charge == 2
        assert parsed.adducts == ["M", "NH4"]
        assert parsed.mass_error == MassError(0.5, 'ppm')
        assert parsed.analyte_reference == '2'
        assert parsed.confidence == 0.05
        assert parsed == base
        self._matches_schema(parsed)

        base = '&%s' % base
        parsed = parse_annotation(base)[0]
        assert parsed.series == 'b'
        assert parsed.position == 14
        assert parsed.neutral_losses == ['-H2O', '-NH3', '[Foo]']
        assert parsed.isotope == 2
        assert parsed.charge == 2
        assert parsed.adducts == ["M", "NH4"]
        assert parsed.mass_error == MassError(0.5, 'ppm')
        assert parsed.analyte_reference == '2'
        assert parsed.confidence == 0.05
        assert parsed.is_auxiliary
        assert parsed == base
        self._matches_schema(parsed)

    def test_parse_unannotated_labeled(self):
        base = "?17"
        parsed = parse_annotation(base)[0]
        assert isinstance(parsed, Unannotated)
        assert parsed.unannotated_label == '17'
        self._matches_schema(parsed)

    def test_parse_smiles(self):
        base = "s{CCC(=O)O}"
        parsed = parse_annotation(base)[0]
        assert isinstance(parsed, SMILESAnnotation)
        assert parsed.smiles == "CCC(=O)O"
        self._matches_schema(parsed)

    def test_parse_external(self):
        base = "_{foobar}"
        parsed = parse_annotation(base)[0]
        assert isinstance(parsed, NamedCompoundIonAnnotation)
        assert parsed.compound_name == 'foobar'
        self._matches_schema(parsed)

    def test_parse_formula(self):
        base = "f{C34H53N7O15}"
        parsed = parse_annotation(base)[0]
        assert isinstance(parsed, FormulaAnnotation)
        assert parsed.formula == "C34H53N7O15"
        self._matches_schema(parsed)

    def test_parse_ordinal_with_sequence(self):
        x, = parse_annotation("y1{{Glycan:Hex1}PEPTIDE}-H2O")
        self._matches_schema(x)
        assert x.sequence == "{Glycan:Hex1}PEPTIDE"
        assert x.neutral_losses == ["-H2O"]
        assert isinstance(x, PeptideFragmentIonAnnotation)
        self._matches_schema(x)

    def test_parse_reference(self):
        x: ReferenceIonAnnotation
        x, = parse_annotation("r[TMT126]")
        assert x.reference == 'TMT126'
        self._matches_schema(x)
