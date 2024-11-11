import json
from importlib.resources import open_text

from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, ClassVar

PROTON = 1.00727646677


def _neutral_mass(mz, z, charge_carrier=PROTON):
    return (mz * abs(z)) - (z * charge_carrier)


def _mass_charge_ratio(neutral_mass, z, charge_carrier=PROTON):
    return (neutral_mass + (z * charge_carrier)) / abs(z)


@dataclass(frozen=True)
class ReferenceMolecule:
    name: str
    molecule_type: str
    cv_term: Optional[str] = field(default=None)
    label_type: Optional[str] = field(default=None)
    neutral_mass: float = field(default=None)
    ion_mz: float = field(default=None)
    chemical_formula: Optional[str] = field(default=None)
    ion_chemical_formula: Optional[str] = field(default=None)
    references: List[str] = field(default_factory=list)

    _registry: ClassVar[Dict[str, 'ReferenceMolecule']] = None

    def __post_init__(self):
        if self.neutral_mass is None:
            if self.ion_mz is not None:
                object.__setattr__(self, "neutral_mass",
                                   _neutral_mass(self.ion_mz, 1))
            else:
                raise ValueError("Must provide at least one of `neutral_mass` or `ion_mz`!")
        elif self.ion_mz is None:
            if self.neutral_mass is not None:
                object.__setattr__(self, 'neutral_mass',
                                   _mass_charge_ratio(self.neutral_mass, 1))
            else:
                raise ValueError("Must provide at least one of `neutral_mass` or `ion_mz`!")

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, state, **kwargs):
        return cls(**state)

    @classmethod
    def _load_registry(cls):
        with open_text("mzpaf.data", "reference_molecules.json") as stream:
            data = json.load(stream)
        cls._registry = {}
        for k, v in data.items():
            v['name'] = k
            cls._registry[k] = cls.from_dict(v)

    @classmethod
    def get(cls, name: str) -> 'ReferenceMolecule':
        if cls._registry is None:
            cls._load_registry()
        return cls._registry[name]

    @classmethod
    def is_reference(cls, name: str) -> bool:
        if cls._registry is None:
            cls._load_registry()
        return name in cls._registry


def load_json(stream) -> Dict[str, ReferenceMolecule]:
    if isinstance(stream, dict):
        payload = stream
    else:
        payload = json.load(stream)
    index = {}
    for name, state in payload.items():
        state['name'] = name
        index[name] = ReferenceMolecule.from_dict(state)
    return index
