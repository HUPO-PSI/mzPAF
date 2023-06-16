import unittest

from mzpaf import (
    parse_annotation, Unannotated, MassError, SMILESAnnotation,
    ExternalIonAnnotation, FormulaAnnotation, PeptideFragmentIonAnnotation,
    ReferenceIonAnnotation)


class TestAnnotationParser(unittest.TestCase):
    def test_parse_unannotated(self):
        assert isinstance(parse_annotation("?^2")[0], Unannotated)

    def test_parse_annotation_complex(self):
        base = "b14"
        parsed = parse_annotation(base)[0]
        assert parsed.series == 'b'
        assert parsed.position == 14

        base += "-H2O-NH3+[Foo]"

        parsed = parse_annotation(base)[0]
        assert parsed.series == 'b'
        assert parsed.position == 14
        assert parsed.neutral_losses == ['-H2O', '-NH3', '[Foo]']

        base += "+2i"

        parsed = parse_annotation(base)[0]
        assert parsed.series == 'b'
        assert parsed.position == 14
        assert parsed.neutral_losses == ['-H2O', '-NH3', '[Foo]']
        assert parsed.isotope == 2

        base += "[M+NH4]^2"
        parsed = parse_annotation(base)[0]
        assert parsed.series == 'b'
        assert parsed.position == 14
        assert parsed.neutral_losses == ['-H2O', '-NH3', '[Foo]']
        assert parsed.isotope == 2
        assert parsed.charge == 2
        assert parsed.adducts == ["M", "NH4"]

        base += "/0.5ppm"

        parsed = parse_annotation(base)[0]
        assert parsed.series == 'b'
        assert parsed.position == 14
        assert parsed.neutral_losses == ['-H2O', '-NH3', '[Foo]']
        assert parsed.isotope == 2
        assert parsed.charge == 2
        assert parsed.adducts == ["M", "NH4"]
        assert parsed.mass_error == MassError(0.5, 'ppm')

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

    def test_parse_unannotated_labeled(self):
        base = "?17"
        parsed = parse_annotation(base)[0]
        assert isinstance(parsed, Unannotated)
        assert parsed.unannotated_label == '17'

    def test_parse_smiles(self):
        base = "s{CCC(=O)O}"
        parsed = parse_annotation(base)[0]
        assert isinstance(parsed, SMILESAnnotation)
        assert parsed.smiles == "CCC(=O)O"

    def test_parse_external(self):
        base = "_{foobar}"
        parsed = parse_annotation(base)[0]
        assert isinstance(parsed, ExternalIonAnnotation)
        assert parsed.label == 'foobar'

    def test_parse_formula(self):
        base = "f{C34H53N7O15}"
        parsed = parse_annotation(base)[0]
        assert isinstance(parsed, FormulaAnnotation)
        assert parsed.formula == "C34H53N7O15"

    def test_parse_ordinal_with_sequence(self):
        x, = parse_annotation("y1{{Glycan:Hex1}PEPTIDE}-H2O")
        assert x.sequence == "{Glycan:Hex1}PEPTIDE"
        assert x.neutral_losses == ["-H2O"]
        assert isinstance(x, PeptideFragmentIonAnnotation)

    def test_parse_reference(self):
        x: ReferenceIonAnnotation
        x, = parse_annotation("r[TMT126]")
        assert x.reference == 'TMT126'