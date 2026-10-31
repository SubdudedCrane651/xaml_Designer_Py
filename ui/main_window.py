from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QFileDialog,
    QDockWidget,
    QGraphicsView,
    QMainWindow,
    QTextEdit
)

from canvas.designer_scene import (
    DesignerScene
)

from models.control import Control

from services.serializer import (
    save_project,
    load_project
)

from services.xaml_generator import (
    generate_xaml
)

from ui.toolbox import ToolBox
from ui.property_editor import (
    PropertyEditor
)


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.controls = []

        self.setWindowTitle(
            "MAUI Designer"
        )

        self.resize(
            1400,
            900
        )

        self.scene = (
            DesignerScene()
        )

        self.view = (
            QGraphicsView(
                self.scene
            )
        )

        self.setCentralWidget(
            self.view
        )

        self.build_ui()

        self.refresh_xaml()

    def build_ui(self):

        self.toolbox = ToolBox()

        self.toolbox.itemDoubleClicked.connect(
            self.add_control
        )

        toolbox_dock = (
            QDockWidget(
                "Toolbox"
            )
        )

        toolbox_dock.setWidget(
            self.toolbox
        )

        self.addDockWidget(
            Qt.DockWidgetArea.LeftDockWidgetArea,
            toolbox_dock
        )

        self.property_editor = (
            PropertyEditor()
        )

        prop_dock = (
            QDockWidget(
                "Properties"
            )
        )

        prop_dock.setWidget(
            self.property_editor
        )

        self.addDockWidget(
            Qt.DockWidgetArea.RightDockWidgetArea,
            prop_dock
        )

        self.xaml_preview = (
            QTextEdit()
        )

        self.xaml_preview.setReadOnly(
            True
        )

        xaml_dock = QDockWidget(
            "XAML"
        )

        xaml_dock.setWidget(
            self.xaml_preview
        )

        self.addDockWidget(
            Qt.DockWidgetArea.BottomDockWidgetArea,
            xaml_dock
        )

        self.create_menu()

    def create_menu(self):

        file_menu = (
            self.menuBar().addMenu(
                "File"
            )
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
            self.new_project
        )

        open_action.triggered.connect(
            self.open_project
        )

        save_action.triggered.connect(
            self.save_project
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

    def add_control(self, item):

        control_type = item.text()

        count = len(
            self.controls
        ) + 1

        control = Control(
            control_type=control_type,
            name=f"{control_type}{count}",
            text=control_type,
            x=100,
            y=100
        )

        self.controls.append(
            control
        )

        self.scene.add_control(control)

        self.refresh_xaml()

    def refresh_xaml(self):

        self.xaml_preview.setPlainText(
            generate_xaml(
                self.controls
            )
        )

    def new_project(self):

        self.controls.clear()

        self.scene.clear()

        self.refresh_xaml()

    def save_project(self):

        filename, _ = (
            QFileDialog.getSaveFileName(
                self,
                "Save Project",
                "",
                "Designer (*.mauiwyg)"
            )
        )

        if filename:

            save_project(
                filename,
                self.controls
            )

    def open_project(self):

        filename, _ = (
            QFileDialog.getOpenFileName(
                self,
                "Open Project",
                "",
                "Designer (*.mauiwyg)"
            )
        )

        if not filename:
            return

        self.controls = (
            load_project(
                filename
            )
        )

        self.scene.clear()

        for control in self.controls:

            item = (
                self.scene.add_control(
                    control
                )
            )

            item.selected_item.connect(
                self.property_editor.set_control
            )

        self.refresh_xaml()