from PyQt6.QtCore import (
    QRectF,
    Qt
)
from PyQt6.QtGui import (
    QColor,
    QBrush,
    QPen,
    QPainter,
    QFont
)
from PyQt6.QtWidgets import (
    QGraphicsObject
)


class DesignerItem(QGraphicsObject):

    def __init__(self, control):
        super().__init__()

        self.control = control

        self.setPos(
            control.x,
            control.y
        )

        self.setFlags(
            self.GraphicsItemFlag.ItemIsMovable |
            self.GraphicsItemFlag.ItemIsSelectable
        )

    def boundingRect(self):

        return QRectF(
            0,
            0,
            self.control.width,
            self.control.height
        )

    def paint(
        self,
        painter: QPainter,
        option,
        widget
    ):

        rect = self.boundingRect()

        #
        # Shadow
        #
        if getattr(self.control, "shadow", False):

            painter.setPen(QPen(Qt.PenStyle.NoPen))

            painter.setBrush(
                QColor(
                    0,
                    0,
                    0,
                    40
                )
            )

            painter.drawRoundedRect(
                rect.adjusted(
                    4,
                    4,
                    4,
                    4
                ),
                self.control.border_radius,
                self.control.border_radius
            )

        #
        # Main body
        #

        painter.setPen(
            QPen(
                QColor(
                    self.control.border_color
                ),
                self.control.border_width
            )
        )

        painter.setBrush(
            QBrush(
                QColor(
                    self.control.background_color
                )
            )
        )

        #
        # Frame/Border/Button/etc
        #

        painter.drawRoundedRect(
            rect,
            self.control.border_radius,
            self.control.border_radius
        )

        #
        # Selection glow
        #

        if self.isSelected():

            painter.setPen(
                QPen(
                    QColor(
                        "#2196F3"
                    ),
                    2
                )
            )

            painter.setBrush(
                Qt.BrushStyle.NoBrush
            )

            painter.drawRect(
                rect
            )

        #
        # Render control content
        #

        font = QFont()

        font.setPointSize(10)

        painter.setFont(font)

        painter.setPen(
            QColor(
                self.control.foreground_color
            )
        )

        control_type = (
            self.control.control_type
        )

        #
        # LABEL
        #

        if control_type == "Label":

            painter.drawText(
                rect,
                int(
                    Qt.AlignmentFlag.AlignLeft |
                    Qt.AlignmentFlag.AlignVCenter
                ),
                self.control.text
            )

        #
        # BUTTON
        #

        elif control_type == "Button":

            painter.drawText(
                rect,
                int(
                    Qt.AlignmentFlag.AlignCenter
                ),
                self.control.text
            )

        #
        # ENTRY
        #

        elif control_type == "Entry":

            inset = rect.adjusted(
                4,
                4,
                -4,
                -4
            )

            painter.drawText(
                inset,
                int(
                    Qt.AlignmentFlag.AlignLeft |
                    Qt.AlignmentFlag.AlignVCenter
                ),
                self.control.text
            )

        #
        # FRAME
        #

        elif control_type == "Frame":

            painter.drawText(
                rect,
                int(
                    Qt.AlignmentFlag.AlignCenter
                ),
                "Frame"
            )

        #
        # BORDER
        #

        elif control_type == "Border":

            painter.drawText(
                rect,
                int(
                    Qt.AlignmentFlag.AlignCenter
                ),
                "Border"
            )

        #
        # IMAGE
        #

        elif control_type == "Image":

            painter.drawText(
                rect,
                int(
                    Qt.AlignmentFlag.AlignCenter
                ),
                "Image"
            )

        #
        # CHECKBOX
        #

        elif control_type == "CheckBox":

            box = QRectF(
                5,
                (rect.height() / 2) - 8,
                16,
                16
            )

            painter.drawRect(box)

            painter.drawText(
                QRectF(
                    26,
                    0,
                    rect.width(),
                    rect.height()
                ),
                int(
                    Qt.AlignmentFlag.AlignVCenter
                ),
                self.control.text
            )

        #
        # SWITCH
        #

        elif control_type == "Switch":

            painter.drawRoundedRect(
                5,
                8,
                40,
                20,
                10,
                10
            )

            painter.drawEllipse(
                7,
                10,
                16,
                16
            )

            painter.drawText(
                QRectF(
                    50,
                    0,
                    rect.width(),
                    rect.height()
                ),
                int(
                    Qt.AlignmentFlag.AlignVCenter
                ),
                self.control.text
            )

        #
        # DEFAULT
        #

        else:

            painter.drawText(
                rect,
                int(
                    Qt.AlignmentFlag.AlignCenter
                ),
                control_type
            )

    def mouseReleaseEvent(
        self,
        event
    ):

        self.control.x = self.pos().x()

        self.control.y = self.pos().y()

        super().mouseReleaseEvent(
            event
        )

    def refresh(self):

        self.prepareGeometryChange()

        self.setPos(
            self.control.x,
            self.control.y
        )

        self.update()