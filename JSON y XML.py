import os
import xml.etree.ElementTree as xml
import json

data = {
    "name" : "Cristian Cordero",
    "age" : 25,
    "birth_date" : "14-01-2000",
    "programming_languages" : ["Python", "Java", "JavaScript"]
}

xml_file = "cristiandev.xml"


"""
Ejercicio
"""


# XML

def save_xml():

    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)
    
    tree = xml.ElementTree(root)
    tree.write(xml_file)

save_xml()

with open(xml_file) as xml_data:
    print(xml_data.read())

os.remove(xml_file)


