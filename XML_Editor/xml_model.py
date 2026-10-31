from xml.etree import ElementTree as ET


class XMLModel:

    def __init__(self):
        self.root = ET.Element("Root")

    def load_file(self, filename):
        tree = ET.parse(filename)
        self.root = tree.getroot()

    def save_file(self, filename):
        tree = ET.ElementTree(self.root)
        tree.write(
            filename,
            encoding="utf-8",
            xml_declaration=True
        )

    def to_string(self):
        return ET.tostring(
            self.root,
            encoding="unicode"
        )