from PyQt6.QtWidgets import (
    QListWidget
)


class ToolBox(QListWidget):

    def __init__(self):

        super().__init__()

        self.addItems(
            [
                "Button",
                "Label",
                "Entry"
            ]
        )