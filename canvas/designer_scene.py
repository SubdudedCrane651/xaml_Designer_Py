from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QGraphicsScene
)

from canvas.designer_item import (
    DesignerItem
)


class DesignerScene(QGraphicsScene):

    #
    # Fires when a control gets selected
    #
    control_selected = pyqtSignal(object)

    #
    # Fires whenever controls move
    #
    canvas_changed = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.control_items = {}

        self.setSceneRect(
            0,
            0,
            5000,
            5000
        )

        self.selectionChanged.connect(
            self._on_selection_changed
        )

    def add_control(
        self,
        control
    ):

        item = DesignerItem(control)

        self.addItem(item)

        self.control_items[
            control.name
        ] = item

        return item

    def remove_control(
        self,
        control
    ):

        item = self.control_items.get(
            control.name
        )

        if item:

            self.removeItem(item)

            del self.control_items[
                control.name
            ]

            self.canvas_changed.emit()

    def get_item(
        self,
        control
    ):

        return self.control_items.get(
            control.name
        )

    def refresh_control(
        self,
        control
    ):

        item = self.get_item(
            control
        )

        if item:

            item.refresh()

            self.canvas_changed.emit()

    def clear_controls(self):

        self.clear()

        self.control_items.clear()

        self.canvas_changed.emit()

    def selected_control(self):

        items = self.selectedItems()

        if not items:
            return None

        item = items[0]

        if hasattr(item, "control"):
            return item.control

        return None

    def _on_selection_changed(self):

        control = self.selected_control()

        if control is not None:

            self.control_selected.emit(
                control
            )

    def mouseReleaseEvent(
        self,
        event
    ):

        super().mouseReleaseEvent(
            event
        )

        #
        # Update XAML after move
        #

        self.canvas_changed.emit()

    def refresh_all(self):

        for item in self.control_items.values():

            item.refresh()

        self.update()

        self.canvas_changed.emit()