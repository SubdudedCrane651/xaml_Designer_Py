from PyQt6.QtCore import pyqtSignal

from PyQt6.QtWidgets import (
    QWidget,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QCheckBox,
    QPushButton,
    QColorDialog
)


class PropertyEditor(QWidget):

    control_changed = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.control = None

        layout = QFormLayout()

        self.setLayout(layout)

        #
        # Name
        #

        self.name_edit = QLineEdit()

        layout.addRow(
            "Name",
            self.name_edit
        )

        #
        # Text
        #

        self.text_edit = QLineEdit()

        layout.addRow(
            "Text",
            self.text_edit
        )

        #
        # Position
        #

        self.x_spin = QSpinBox()
        self.x_spin.setRange(-10000, 10000)

        self.y_spin = QSpinBox()
        self.y_spin.setRange(-10000, 10000)

        layout.addRow(
            "X",
            self.x_spin
        )

        layout.addRow(
            "Y",
            self.y_spin
        )

        #
        # Size
        #

        self.width_spin = QSpinBox()
        self.width_spin.setRange(10, 5000)

        self.height_spin = QSpinBox()
        self.height_spin.setRange(10, 5000)

        layout.addRow(
            "Width",
            self.width_spin
        )

        layout.addRow(
            "Height",
            self.height_spin
        )

        #
        # Border Width
        #

        self.border_width_spin = QSpinBox()
        self.border_width_spin.setRange(0, 50)

        layout.addRow(
            "Border Width",
            self.border_width_spin
        )

        #
        # Border Radius
        #

        self.border_radius_spin = QSpinBox()
        self.border_radius_spin.setRange(0, 100)

        layout.addRow(
            "Border Radius",
            self.border_radius_spin
        )

        #
        # Shadow
        #

        self.shadow_check = QCheckBox()

        layout.addRow(
            "Shadow",
            self.shadow_check
        )

        #
        # Color Buttons
        #

        self.background_button = QPushButton(
            "Background Color"
        )

        self.foreground_button = QPushButton(
            "Text Color"
        )

        self.border_button = QPushButton(
            "Border Color"
        )

        layout.addRow(
            self.background_button
        )

        layout.addRow(
            self.foreground_button
        )

        layout.addRow(
            self.border_button
        )

        #
        # Apply
        #

        self.apply_button = QPushButton(
            "Apply Changes"
        )

        layout.addRow(
            self.apply_button
        )

        #
        # Events
        #

        self.apply_button.clicked.connect(
            self.apply_changes
        )

        self.background_button.clicked.connect(
            self.choose_background
        )

        self.foreground_button.clicked.connect(
            self.choose_foreground
        )

        self.border_button.clicked.connect(
            self.choose_border
        )

    def control_modified(self, control):

        print(
            control.name,
            control.text
        )

        self.scene.refresh_control(control)

        self.refresh_xaml()        

    def load_control(
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

        self.x_spin.setValue(
            int(control.x)
        )

        self.y_spin.setValue(
            int(control.y)
        )

        self.width_spin.setValue(
            int(control.width)
        )

        self.height_spin.setValue(
            int(control.height)
        )

        self.border_width_spin.setValue(
            control.border_width
        )

        self.border_radius_spin.setValue(
            control.border_radius
        )

        self.shadow_check.setChecked(
            control.shadow
        )

    def choose_background(self):

        if not self.control:
            return

        color = QColorDialog.getColor()

        if color.isValid():

            self.control.background_color = (
                color.name()
            )

    def choose_foreground(self):

        if not self.control:
            return

        color = QColorDialog.getColor()

        if color.isValid():

            self.control.foreground_color = (
                color.name()
            )

    def choose_border(self):

        if not self.control:
            return

        color = QColorDialog.getColor()

        if color.isValid():

            self.control.border_color = (
                color.name()
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

        self.control.x = (
            self.x_spin.value()
        )

        self.control.y = (
            self.y_spin.value()
        )

        self.control.width = (
            self.width_spin.value()
        )

        self.control.height = (
            self.height_spin.value()
        )

        self.control.border_width = (
            self.border_width_spin.value()
        )

        self.control.border_radius = (
            self.border_radius_spin.value()
        )

        self.control.shadow = (
            self.shadow_check.isChecked()
        )

        self.control_changed.emit(
            self.control
        )