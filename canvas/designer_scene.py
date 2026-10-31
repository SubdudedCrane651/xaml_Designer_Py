from PyQt6.QtWidgets import (
    QGraphicsScene
)

from canvas.designer_item import (
    DesignerItem
)


class DesignerScene(QGraphicsScene):

    def __init__(self):

        super().__init__()

        self.setSceneRect(
            0,
            0,
            3000,
            3000
        )

    def add_control(
        self,
        model
    ):

        item = DesignerItem(
            model
        )

        self.addItem(item)

        return item