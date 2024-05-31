import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """create the root element"""
    root = ET.Element('data')
    """for each key-value pair in dict, create a subelement"""
    for key, value in dictionary.items():
        child = ET.SubElement(root.key)
        child.text = str(value)
    """create ElementTreee and write to file"""
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """parse XML and get root element"""
    tree = ET.parse(filename)
    root = tree.getroot()
    """create dict from XML"""
    dictionary = {child.tag: child.text for child in root}
    return dictionary

if __name__ == "__main__":
    """Defines a dictionary
    then defines a filename
    serializes the dict to XML
    deserializes XML back to dict
    print the deserialized data
    """
    data = {'name': 'John', 'age': 25, 'is_student': True}
    filename = 'data.xml'
    serialize_to_xml(data, filename)
    deserialized_data = deserialize_from_xml(filename)
    print(deserialized_data)
