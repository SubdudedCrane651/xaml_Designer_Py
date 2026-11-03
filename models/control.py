from dataclasses import dataclass, asdict


@dataclass
class Control:

    control_type: str = "Button"

    name: str = "Control1"

    text: str = "Control"

    x: float = 100
    y: float = 100

    width: float = 120
    height: float = 40

    background_color: str = "#E8E8E8"

    foreground_color: str = "#000000"

    border_color: str = "#808080"

    border_width: int = 1

    border_radius: int = 5

    shadow: bool = False

    image_path: str = ""

    visible: bool = True

    enabled: bool = True

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data):
        return Control(**data)