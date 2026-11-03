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

from models.control import (
    Control
)

from ui.toolbox import (
    ToolBox
)

from ui.property_editor import (
    PropertyEditor
)

from services.serializer import (
    save_project,
    load_project
)

from services.xaml_generator import (
    generate_xaml
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "XAML Designer V2"
        )

        self.resize(
            1600,
            900
        )

        self.controls = []

        #
        # Scene
        #

        self.scene = DesignerScene()

        self.view = QGraphicsView(
            self.scene
        )

        self.setCentralWidget(
            self.view
        )

        #
        # Toolbox
        #

        self.toolbox = ToolBox()

        toolbox_dock = QDockWidget(
            "Toolbox"
        )

        toolbox_dock.setWidget(
            self.toolbox
        )

        self.addDockWidget(
            Qt.DockWidgetArea.LeftDockWidgetArea,
            toolbox_dock
        )

        #
        # Property Editor
        #

        self.property_editor = (
            PropertyEditor()
        )

        property_dock = QDockWidget(
            "Properties"
        )

        property_dock.setWidget(
            self.property_editor
        )

        self.addDockWidget(
            Qt.DockWidgetArea.RightDockWidgetArea,
            property_dock
        )

        #
        # XAML Preview
        #

        self.xaml_preview = QTextEdit()

        self.xaml_preview.setReadOnly(
            True
        )

        xaml_dock = QDockWidget(
            "XAML Preview"
        )

        xaml_dock.setWidget(
            self.xaml_preview
        )

        self.addDockWidget(
            Qt.DockWidgetArea.BottomDockWidgetArea,
            xaml_dock
        )

        #
        # Menu
        #

        self.create_menu()

        #
        # Wiring
        #

        self.toolbox.itemDoubleClicked.connect(
            self.add_control
        )

        self.scene.control_selected.connect(
            self.property_editor.load_control
        )

        self.property_editor.control_changed.connect(
            self.control_modified
        )

        self.scene.canvas_changed.connect(
            self.refresh_xaml
        )

        self.refresh_xaml()

    #
    # Menu
    #

    def create_menu(self):

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

    #
    # Add Control
    #

    def add_control(self, item):

        control_type = item.text()

        index = (
            len(self.controls) + 1
        )

        control = Control(
            control_type=control_type,
            name=f"{control_type}{index}",
            text=control_type,
            x=100,
            y=100
        )

        self.controls.append(
            control
        )

        self.scene.add_control(
            control
        )

        self.refresh_xaml()

    #
    # Property Changes
    #

    def control_modified(
        self,
        control
    ):

        self.scene.refresh_control(
            control
        )

        self.refresh_xaml()

    #
    # XAML
    #

    def refresh_xaml(self):

        self.xaml_preview.setPlainText(
            generate_xaml(
                self.controls
            )
        )

    #
    # New
    #

    def new_project(self):

        self.controls.clear()

        self.scene.clear_controls()

        self.refresh_xaml()

    #
    # Save
    #

    def save_project(self):

        filename, _ = (
            QFileDialog.getSaveFileName(
                self,
                "Save Project",
                "",
                "Designer (*.mauiwyg)"
            )
        )

        if not filename:
            return

        save_project(
            filename,
            self.controls
        )

    #
    # Open
    #

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

        self.scene.clear_controls()

        for control in self.controls:

            self.scene.add_control(
                control
            )

        self.refresh_xaml()