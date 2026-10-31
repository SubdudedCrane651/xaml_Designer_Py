from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QFormLayout
from PyQt6.QtWidgets import QLineEdit


class PropertyEditor(QWidget):

    def __init__(self):

        super().__init__()

        self.current_node = None

        self.layout = QFormLayout()

        self.setLayout(self.layout)

        self.tag_edit = QLineEdit()
        self.text_edit = QLineEdit()

        self.layout.addRow(
            "Tag",
            self.tag_edit
        )

        self.layout.addRow(
            "Value",
            self.text_edit
        )

    def set_node(self, node):

        self.current_node = node

        self.tag_edit.setText(node.tag)

        self.text_edit.setText(node.text or "")

    def update_node(self):

        if not self.current_node:
            return

        self.current_node.tag = self.tag_edit.text()

        self.current_node.text = self.text_edit.text()