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
            getattr(control, "x", 100),
            getattr(control, "y", 100)
        )

        self.setFlags(
            self.GraphicsItemFlag.ItemIsMovable |
            self.GraphicsItemFlag.ItemIsSelectable
        )

    def boundingRect(self):

        return QRectF(
            0,
            0,
            getattr(
                self.control,
                "width",
                120
            ),
            getattr(
                self.control,
                "height",
                40
            )
        )

    def paint(
        self,
        painter,
        option,
        widget
    ):

        rect = self.boundingRect()

        #
        # Safe property retrieval
        #

        background_color = getattr(
            self.control,
            "background_color",
            "#E8E8E8"
        )

        foreground_color = getattr(
            self.control,
            "foreground_color",
            "#000000"
        )

        border_color = getattr(
            self.control,
            "border_color",
            "#808080"
        )

        border_width = getattr(
            self.control,
            "border_width",
            1
        )

        border_radius = getattr(
            self.control,
            "border_radius",
            5
        )

        shadow = getattr(
            self.control,
            "shadow",
            False
        )

        control_type = getattr(
            self.control,
            "control_type",
            "Button"
        )

        text = getattr(
            self.control,
            "text",
            control_type
        )

        #
        # Shadow
        #

        if shadow:

            painter.setPen(
                Qt.PenStyle.NoPen
            )

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
                border_radius,
                border_radius
            )

        #
        # Base appearance
        #

        painter.setPen(
            QPen(
                QColor(border_color),
                border_width
            )
        )

        painter.setBrush(
            QBrush(
                QColor(
                    background_color
                )
            )
        )

        #
        # Main shape
        #

        painter.drawRoundedRect(
            rect,
            border_radius,
            border_radius
        )

        #
        # Selection border
        #

        if self.isSelected():

            painter.setPen(
                QPen(
                    QColor("#2196F3"),
                    2
                )
            )

            painter.setBrush(
                Qt.BrushStyle.NoBrush
            )

            painter.drawRect(rect)

        #
        # Text
        #

        font = QFont()
        font.setPointSize(10)

        painter.setFont(font)

        painter.setPen(
            QColor(
                foreground_color
            )
        )

        #
        # Label
        #

        if control_type == "Label":

            painter.drawText(
                rect,
                Qt.AlignmentFlag.AlignLeft |
                Qt.AlignmentFlag.AlignVCenter,
                text
            )

        #
        # Button
        #

        elif control_type == "Button":

            painter.drawText(
                rect,
                Qt.AlignmentFlag.AlignCenter,
                text
            )

        #
        # Entry
        #

        elif control_type == "Entry":

            painter.drawText(
                rect.adjusted(
                    5,
                    0,
                    -5,
                    0
                ),
                Qt.AlignmentFlag.AlignLeft |
                Qt.AlignmentFlag.AlignVCenter,
                text
            )

        #
        # Frame
        #

        elif control_type == "Frame":

            painter.drawText(
                rect,
                Qt.AlignmentFlag.AlignCenter,
                "Frame"
            )

        #
        # Border
        #

        elif control_type == "Border":

            painter.drawText(
                rect,
                Qt.AlignmentFlag.AlignCenter,
                "Border"
            )

        #
        # Image
        #

        elif control_type == "Image":

            painter.drawText(
                rect,
                Qt.AlignmentFlag.AlignCenter,
                "Image"
            )

        #
        # CheckBox
        #

        elif control_type == "CheckBox":

            painter.drawRect(
                8,
                int(rect.height() / 2) - 8,
                16,
                16
            )

            painter.drawText(
                QRectF(
                    30,
                    0,
                    rect.width(),
                    rect.height()
                ),
                Qt.AlignmentFlag.AlignVCenter,
                text
            )

        #
        # Switch
        #

        elif control_type == "Switch":

            painter.drawRoundedRect(
                8,
                8,
                40,
                20,
                10,
                10
            )

            painter.drawEllipse(
                10,
                10,
                16,
                16
            )

            painter.drawText(
                QRectF(
                    60,
                    0,
                    rect.width(),
                    rect.height()
                ),
                Qt.AlignmentFlag.AlignVCenter,
                text
            )

        #
        # Default
        #

        else:

            painter.drawText(
                rect,
                Qt.AlignmentFlag.AlignCenter,
                control_type
            )

    def mouseReleaseEvent(
        self,
        event
    ):

        if hasattr(
            self.control,
            "x"
        ):
            self.control.x = self.pos().x()

        if hasattr(
            self.control,
            "y"
        ):
            self.control.y = self.pos().y()

        super().mouseReleaseEvent(
            event
        )

    def refresh(self):

        self.prepareGeometryChange()

        self.setPos(
            getattr(
                self.control,
                "x",
                100
            ),
            getattr(
                self.control,
                "y",
                100
            )
        )

        self.update()