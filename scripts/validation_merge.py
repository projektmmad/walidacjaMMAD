from valid_functions import *
path = '../data_examples/VOC2012/Annotations/2007_000027.xml'

def pascal_validator(path):
    if syntax_validator(path) is not False:
        tree = ET.parse(path)
        root = tree.getroot()
        size = root.find("size")
        width = int(size.find("width").text)
        height = int(size.find("height").text)
        str_jpg = root.find('filename').text
        great_bnd_validator(root, width, height)
        check_extension(str_jpg)
        values_validator(root, 'depth', {0, 3})
        values_validator(root, 'truncated', {0, 1})
        values_validator(root, 'difficult', {0, 1})
    else:
        return None
pascal_validator(path)
