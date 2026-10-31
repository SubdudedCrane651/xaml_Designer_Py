from PyQt6.QtWidgets import (
    QWidget,
    QFormLayout,
    QLineEdit
)


class PropertyEditor(QWidget):

    def __init__(self):

        super().__init__()

        self.control = None

        layout = QFormLayout()

        self.setLayout(layout)

        self.name_edit = QLineEdit()
        self.text_edit = QLineEdit()

        layout.addRow(
            "Name",
            self.name_edit
        )

        layout.addRow(
            "Text",
            self.text_edit
        )

    def set_control(
        self,
        control
    ):

        self.control = control

        self.name_edit.setText(
            control.name
        )

        self.text_edit.setText(
            control.text
        )

    def apply_changes(self):

        if not self.control:
            return

        self.control.name = (
            self.name_edit.text()
        )

        self.control.text = (
            self.text_edit.text()
        )