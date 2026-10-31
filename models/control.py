from dataclasses import dataclass, asdict


@dataclass
class Control:
    control_type: str
    name: str
    text: str
    x: float = 50
    y: float = 50
    width: float = 120
    height: float = 40

    def to_dict(self):
        return asdict(self)