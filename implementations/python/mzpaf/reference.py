
import json

from dataclasses import dataclass, field, asdict
from typing import Any, List, Optional, Pattern, Dict, Tuple, Type, Union

PROTON = 1.00727646677

def _neutral_mass(mz, z, charge_carrier=PROTON):
    return (mz * abs(z)) - (z * charge_carrier)


def _mass_charge_ratio(neutral_mass, z, charge_carrier=PROTON):
    return (neutral_mass + (z * charge_carrier)) / abs(z)


@dataclass
class ReferenceMolecule:
    name: str
    molecule_type: str
    label_type: str = field(default=None)
    neutral_mass: float = field(default=None)
    ion_mz: float = field(default=None)
    chemical_formula: str = field(default=None)
    ion_chemical_formula: str = field(default=None)
    references: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.neutral_mass is None:
            if self.ion_mz is not None:
                self.neutral_mass = _neutral_mass(self.ion_mz, 1)
            else:
                raise ValueError("Must provide at least one of `neutral_mass` or `ion_mz`!")
        elif self.ion_mz is None:
            if self.neutral_mass is not None:
                self.ion_mz = _mass_charge_ratio(self.neutral_mass, 1)
            else:
                raise ValueError("Must provide at least one of `neutral_mass` or `ion_mz`!")

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, state, **kwargs):
        return cls(**state)


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
