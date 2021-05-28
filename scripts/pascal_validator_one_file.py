from pascal_valid_functions import *
import xml.etree.ElementTree as ET
import os


def pascal_validator_one_file(path: str):
    filname = os.path.basename(path)
    if syntax_validator(path, filname) is not False:
        tree = ET.parse(path)
        root = tree.getroot()
        if check_if_empty_value(tree, filname) is False:
            if correct_tag(tree, filname) is not False:
                size = root.find("size")
                width = float(size.find("width").text)
                height = float(size.find("height").text)
                str_jpg = root.find('filename').text
                check_extension(str_jpg, root, filname)
                correct_filename(root, filname)
                root_tag(root, filname)
                great_bnd_validator(root, width, height, filname)
                values_validator(root, 'depth', {'0', '3'}, filname)
                values_validator(root, 'truncated', {'0', '1'}, filname)
                values_validator(root, 'difficult', {'0', '1'}, filname)
                values_validator(root, 'pose', {'Unspecified', 'Rear', 'Frontal', 'Left', 'Right'}, filname)

def pascal_validator_one_file_syntax(path: str):
    filname = os.path.basename(path)
    syntax_validator(path, filname)