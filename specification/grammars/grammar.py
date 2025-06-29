import os
import string

import railroad
from railroad import (
    Diagram,
    Choice,
    Group,
    Optional,
    Terminal,
    NonTerminal,
    Sequence,
    OneOrMore,
    ZeroOrMore,
    Stack,
)
import io

from pyteomics.mass import std_aa_comp, nist_mass

railroad.ESCAPE_HTML = True
railroad.DEBUG = True

image_dir = "schema_images/"
os.makedirs(image_dir, exist_ok=True)

elements = sorted(nist_mass.keys())
if 'e*' in elements:
    elements.remove('e*')


UPPER_CASE_LETTER = Choice(0, *string.ascii_uppercase)

LOWER_CASE_LETTER = Choice(0, *string.ascii_lowercase)

SYMBOL = Choice(0, *[(c) for c in string.punctuation])

DIGIT = Choice(0, *string.digits)


ELEMENT = Choice(0, *elements)

ISOTOPE_ATOM_COUNT = Sequence(
    "[",
    OneOrMore(NonTerminal("DIGIT")),
    NonTerminal("UPPER_CASE_LETTER"),
    ZeroOrMore(NonTerminal("LOWER_CASE_LETTER")),
    ZeroOrMore(NonTerminal("DIGIT")),
    "]",
)

ATOM_COUNT = Sequence(
    NonTerminal("UPPER_CASE_LETTER"),
    ZeroOrMore(NonTerminal("LOWER_CASE_LETTER")),
    ZeroOrMore(NonTerminal("DIGIT")),
)

NUMBER = Sequence(
    OneOrMore(NonTerminal("DIGIT")),
    Optional(Sequence(".", OneOrMore(NonTerminal("DIGIT")))),
    Optional(
        Sequence(
            "e",
            OneOrMore(NonTerminal("DIGIT")),
            Optional(Sequence(".", OneOrMore(NonTerminal("DIGIT")))),
        )
    ),
)

ORDINAL = OneOrMore(NonTerminal("DIGIT"))

CHARACTER = Choice(
    0,
    NonTerminal("DIGIT"),
    NonTerminal("UPPER_CASE_LETTER"),
    NonTerminal("LOWER_CASE_LETTER"),
)

AMINO_ACID = UPPER_CASE_LETTER

SIGN = Choice(0, "+", "-")

BraceEnclosedContent = Sequence(
    Terminal("["),
    OneOrMore(Choice(0, NonTerminal("CHARACTER"), NonTerminal("SYMBOL"))),
    Optional(
        Sequence(
            Terminal("["),
                OneOrMore(Choice(0, NonTerminal("CHARACTER"), NonTerminal("SYMBOL"), Terminal(" "))),
            Terminal("]"),
        )
    ),
    Terminal("]"),
)

IsAuxiliary = Group(Optional(Terminal("&")), "Is Auxiliary")

AnalyteIdentifier = Group(
    Sequence(NonTerminal("ORDINAL"), Terminal("@")), "Analyte Identifier"
)

PeptideIon = Group(
    Sequence(
        Choice(0, *list(map(Terminal, ("a", "b", "c", "x", "y", "z", "da", "db", "v", "wa", "wb")))),
        NonTerminal("ORDINAL"),
        Optional(
            Sequence(
                Terminal("{"),
                Group(OneOrMore(NonTerminal("ANY")), "ProForma 2.0 Sequence"),
                Terminal("}"),
            )
        ),
    ),
    "Peptide Ion",
)

ReferenceIon = Group(Sequence(Terminal("r"), BraceEnclosedContent), "Reference Ion")

InternalIon = Group(
    Sequence(
        Terminal("m"),
        NonTerminal("ORDINAL"),
        Terminal(":"),
        NonTerminal("ORDINAL"),
        Sequence(
            Terminal("{"),
            Group(NonTerminal("ANY"), "ProForma 2.0 Sequence"),
            Terminal("}"),
        ),
    ),
    "Internal Peptide Ion",
)

ImmoniumIon = Group(
    Sequence(Terminal("I"), NonTerminal("AMINO_ACID"), Optional(BraceEnclosedContent)),
    "Immonium Ion",
)

PrecursorIon = Group(Terminal("p"), "Precursor Ion")


ChemicalFormula = OneOrMore(Choice(0, NonTerminal("ATOM_COUNT"), NonTerminal("ISOTOPE_ATOM_COUNT")))


FormulaIon = Group(
    Sequence(Terminal("f"), Terminal("{"), ChemicalFormula, Terminal("}")),
    "Formula Ion",
)

NamedCompound = Group(
    Sequence(
        Terminal("_"),
        Terminal("{"),
        OneOrMore(NonTerminal("CHARACTER")),
        Terminal("}"),
    ),
    "Named Compound",
)

UnknownIon = Group(
    Sequence(Terminal("?"), Optional(OneOrMore(NonTerminal("DIGIT")))), "Unknown Ion"
)

SMILESIon = Group(
    Sequence(
        Terminal("s"), Terminal("{"), OneOrMore(Terminal("/[^}]/")), Terminal("}")
    ),
    "SMILES Ion",
)

IonType = Group(
    Choice(
        0,
        PeptideIon,
        InternalIon,
        ImmoniumIon,
        ReferenceIon,
        PrecursorIon,
        FormulaIon,
        NamedCompound,
        SMILESIon,
        UnknownIon,
    ),
    "Ion Type",
)

NeutralLoss = Group(
    Sequence(NonTerminal("SIGN"), ZeroOrMore('ORDINAL'), Choice(0, ChemicalFormula, BraceEnclosedContent)),
    "Neutral Loss(es)",
)


IsotopomerIdentity = Group(
    Sequence(OneOrMore(NonTerminal("ORDINAL")), NonTerminal("ELEMENT")),
    "Isotopomer Identity"
)


AverageIsotopologue = Group(
    Terminal("A"),
    "Average Isotopologue"
)


Isotope = ZeroOrMore(Group(
    Sequence(
        NonTerminal("SIGN"),
        ZeroOrMore(NonTerminal("ORDINAL")),
        Terminal("i"),
        Optional(Choice(0, IsotopomerIdentity, AverageIsotopologue)),
    ),
    "Isotope",
))

ChargeState = Group(Sequence("^", NonTerminal("ORDINAL")), "Charge State")

Adducts = Group(
    Sequence(
        "[",
        "M",
        OneOrMore(
            Sequence(
                NonTerminal("SIGN"),
                ChemicalFormula,
            )
        ),
        "]",
    ),
    "Adducts",
)

MassError = Group(Sequence("/", NonTerminal("NUMBER"), Optional("ppm")), "Mass Error")

ConfidenceEstimate = Group(Sequence("*", NonTerminal("NUMBER")), "Confidence Estimate")


Annotation = Stack(
    IsAuxiliary,
    Optional(AnalyteIdentifier),
    IonType,
    ZeroOrMore(NeutralLoss),
    Isotope,
    Optional(Adducts),
    Optional(ChargeState),
    Optional(MassError),
    Optional(ConfidenceEstimate),
)


def encode_svg(diagram):
    buffer = io.StringIO()
    diagram.writeStandalone(buffer.write)
    value: str = buffer.getvalue()
    return value


def render_group_to_file(fh, name):
    print("Writing", name)
    tokens = globals()[name]
    pathname = f"{image_dir}{name}.svg"
    with open(pathname, "wt") as img_fh:
        img_fh.write(encode_svg(Diagram(tokens)))
    fh.write(f"""## {name}\n<img src="{pathname}">\n\n""")


with open("grammar.md", "wt") as fh:
    fh.write("""# Peak Annotation Grammar\n\n""")
    render_group_to_file(fh, "DIGIT")
    render_group_to_file(fh, "LOWER_CASE_LETTER")
    render_group_to_file(fh, "UPPER_CASE_LETTER")
    render_group_to_file(fh, "SYMBOL")
    render_group_to_file(fh, "ORDINAL")
    render_group_to_file(fh, "NUMBER")
    render_group_to_file(fh, "CHARACTER")
    render_group_to_file(fh, "SIGN")
    render_group_to_file(fh, "ELEMENT")
    render_group_to_file(fh, "ATOM_COUNT")
    render_group_to_file(fh, "ISOTOPE_ATOM_COUNT")
    render_group_to_file(fh, "AMINO_ACID")
    render_group_to_file(fh, "Annotation")
    fh.write("\n")
