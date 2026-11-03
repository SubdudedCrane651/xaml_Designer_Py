from dataclasses import dataclass, asdict


@dataclass
class Control:

    #
    # Identity
    #

    control_type: str = "Button"

    name: str = "Button1"

    text: str = "Button"

    #
    # Position
    #

    x: float = 100

    y: float = 100

    #
    # Size
    #

    width: float = 120

    height: float = 40

    #
    # Colors
    #

    background_color: str = "#E8E8E8"

    foreground_color: str = "#000000"

    border_color: str = "#808080"

    #
    # Border
    #

    border_width: int = 1

    border_radius: int = 5

    #
    # Effects
    #

    shadow: bool = False

    #
    # Image/Icon support
    #

    image_path: str = ""

    #
    # State
    #

    visible: bool = True

    enabled: bool = True

    #
    # Serialization
    #

    def to_dict(self):

        return asdict(self)

    @classmethod
    def from_dict(
        cls,
        data
    ):

        defaults = cls()

        for key, value in data.items():

            if hasattr(
                defaults,
                key
            ):
                setattr(
                    defaults,
                    key,
                    value
                )

        return defaults