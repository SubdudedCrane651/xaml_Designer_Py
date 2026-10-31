import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QTextEdit,
    QSplitter,
    QMessageBox
)

from PyQt6.QtGui import QAction

from PyQt6.QtCore import Qt

from xml_model import XMLModel
from xml_tree import XMLTree
from property_editor import PropertyEditor
from designer import Designer


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.model = XMLModel()

        self.setWindowTitle(
            "XML Creator Professional"
        )

        self.resize(1600, 900)

        self.tree = XMLTree()

        self.properties = PropertyEditor()

        self.designer = Designer()

        self.xml_preview = QTextEdit()

        self.xml_preview.setReadOnly(True)

        splitter = QSplitter(
            Qt.Orientation.Horizontal
        )

        splitter.addWidget(self.tree)
        splitter.addWidget(self.designer)
        splitter.addWidget(self.properties)
        splitter.addWidget(self.xml_preview)

        splitter.setSizes(
            [300, 500, 300, 500]
        )

        self.setCentralWidget(
            splitter
        )

        self.build_menu()

        self.tree.itemClicked.connect(
            self.node_selected
        )

        self.properties.tag_edit.editingFinished.connect(
            self.properties_changed
        )

        self.properties.text_edit.editingFinished.connect(
            self.properties_changed
        )

        self.create_demo()

    def build_menu(self):

        file_menu = self.menuBar().addMenu(
            "File"
        )

        new_action = QAction(
            "New",
            self
        )

        open_action = QAction(
            "Open",
            self
        )

        save_action = QAction(
            "Save",
            self
        )

        new_action.triggered.connect(
            self.create_demo
        )

        open_action.triggered.connect(
            self.open_xml
        )

        save_action.triggered.connect(
            self.save_xml
        )

        file_menu.addAction(
            new_action
        )

        file_menu.addAction(
            open_action
        )

        file_menu.addAction(
            save_action
        )

    def create_demo(self):

        from xml.etree import ElementTree as ET

        root = ET.Element("Customer")

        name = ET.SubElement(
            root,
            "Name"
        )

        email = ET.SubElement(
            root,
            "Email"
        )

        phone = ET.SubElement(
            root,
            "Phone"
        )

        name.text = "John"

        email.text = "john@example.com"

        phone.text = "555-1234"

        self.model.root = root

        self.refresh()

    def refresh(self):

        self.tree.populate(
            self.model.root
        )

        self.xml_preview.setText(
            self.model.to_string()
        )

    def node_selected(
        self,
        item
    ):

        node = item.xml_node

        self.properties.set_node(
            node
        )

        self.designer.build_form(
            node
        )

    def properties_changed(self):

        self.properties.update_node()

        self.refresh()

    def open_xml(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open XML",
            "",
            "*.xml"
        )

        if not filename:
            return

        try:

            self.model.load_file(
                filename
            )

            self.refresh()

        except Exception as ex:

            QMessageBox.critical(
                self,
                "Error",
                str(ex)
            )

    def save_xml(self):

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save XML",
            "",
            "*.xml"
        )

        if not filename:
            return

        self.model.save_file(
            filename
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())