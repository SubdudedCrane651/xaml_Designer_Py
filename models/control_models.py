from dataclasses import dataclass


@dataclass
class ControlModel:

    control_type: str

    name: str

    text: str

    x: float

    y: float

    width: float = 120

    height: float = 40