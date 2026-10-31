from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit
)


class Designer(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.setLayout(self.layout)

    def clear_layout(self):

        while self.layout.count():

            child = self.layout.takeAt(0)

            if child.widget():
                child.widget().deleteLater()

    def build_form(self, node):

        self.clear_layout()

        title = QLabel(
            f"Visual Editor : {node.tag}"
        )

        self.layout.addWidget(title)

        for child in node:

            self.layout.addWidget(
                QLabel(child.tag)
            )

            edit = QLineEdit()

            edit.setText(
                child.text or ""
            )

            def updater(
                value,
                element=child
            ):
                element.text = value

            edit.textChanged.connect(
                updater
            )

            self.layout.addWidget(edit)
