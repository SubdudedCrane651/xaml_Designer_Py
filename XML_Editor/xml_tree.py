from PyQt6.QtWidgets import QTreeWidget
from PyQt6.QtWidgets import QTreeWidgetItem


class XMLTree(QTreeWidget):

    def __init__(self):
        super().__init__()

        self.setHeaderLabel("XML Nodes")

    def populate(self, root):

        self.clear()

        root_item = QTreeWidgetItem([root.tag])

        root_item.xml_node = root

        self.addTopLevelItem(root_item)

        self._add_children(root, root_item)

        self.expandAll()

    def _add_children(self, element, item):

        for child in element:

            child_item = QTreeWidgetItem([child.tag])

            child_item.xml_node = child

            item.addChild(child_item)

            self._add_children(child, child_item)