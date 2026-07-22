import xml.etree.ElementTree as ET


class VASPRUNParser:
    """
    Parser for VASP vasprun.xml files.
    """

    def __init__(self):
        self.filename = None

    def read(self, filename):
        self.filename = filename
        return self

    def parse(self):

        tree = ET.parse(self.filename)
        root = tree.getroot()

        result = {}

        # Fermi energy
        for elem in root.iter("i"):
            if elem.attrib.get("name") == "efermi":
                result["efermi"] = float(elem.text)
                break

        return result
