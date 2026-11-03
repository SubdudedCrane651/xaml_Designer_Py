from PyQt6.QtWidgets import (
    QListWidget,
    QListWidgetItem
)

from PyQt6.QtGui import (
    QColor
)


class ToolBox(QListWidget):

    def __init__(self):
        super().__init__()

        self.build_toolbox()

    def add_header(self, text):

        item = QListWidgetItem(text)

        item.setFlags(
            item.flags() &
            ~item.flags().ItemIsSelectable
        )

        item.setBackground(
            QColor("#D8D8D8")
        )

        self.addItem(item)

    def add_control(self, name):

        self.addItem(
            QListWidgetItem(name)
        )

    def build_toolbox(self):

        self.add_header(
            "=== Inputs ==="
        )

        self.add_control("Button")
        self.add_control("Label")
        self.add_control("Entry")
        self.add_control("CheckBox")
        self.add_control("Switch")
        self.add_control("Picker")
        self.add_control("DatePicker")
        self.add_control("Slider")
        self.add_control("ProgressBar")

        self.add_header(
            "=== Visuals ==="
        )

        self.add_control("Image")
        self.add_control("Icon")

        self.add_header(
            "=== Containers ==="
        )

        self.add_control("Frame")
        self.add_control("Border")
        self.add_control("ContentView")

        self.add_header(
            "=== Layouts ==="
        )

        self.add_control("Grid")
        self.add_control(
            "VerticalStackLayout"
        )
        self.add_control(
            "HorizontalStackLayout"
        )
        self.add_control(
            "ScrollView"
        )