from PyQt6.QtWidgets import (
    QGraphicsRectItem,
    QGraphicsTextItem
)

from PyQt6.QtGui import QBrush
from PyQt6.QtCore import Qt

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QGraphicsObject,
    QGraphicsSimpleTextItem
)


class DesignerItem(QGraphicsObject):

    selected_item = pyqtSignal(object)

    def __init__(self, control):
        super().__init__()

        self.control = control

class DesignerItem(QGraphicsRectItem):

    def __init__(self, model):

        super().__init__(
            0,
            0,
            model.width,
            model.height
        )

        self.model = model

        self.setPos(
            model.x,
            model.y
        )

        self.setBrush(
            QBrush(
                Qt.GlobalColor.lightGray
            )
        )

        self.setFlags(
            QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable
            |
            QGraphicsRectItem.GraphicsItemFlag.ItemIsSelectable
        )

        self.caption = QGraphicsTextItem(
            model.text,
            self
        )

        self.caption.setPos(
            5,
            5
        )

    def mouseReleaseEvent(
        self,
        event
    ):

        self.model.x = self.pos().x()

        self.model.y = self.pos().y()

        super().mouseReleaseEvent(
            event
        )