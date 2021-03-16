from valid_functions import *
path = '../data_examples/VOC2012/Annotations/2007_000027.xml'


def pascal_validator_one_file(path):
    if syntax_validator(path) is not False:
        tree = ET.parse(path)
        root = tree.getroot()
        if empty_value(tree) is False:
            size = root.find("size")
            width = int(size.find("width").text)
            height = int(size.find("height").text)
            str_jpg = root.find('filename').text
            correct_tag(tree)
            root_tag(root)
            great_bnd_validator(root, width, height)
            check_extension(str_jpg)
            values_validator(root, 'depth', {'0', '3'})
            values_validator(root, 'truncated', {'0', '1'})
            values_validator(root, 'difficult', {'0', '1'})
            values_validator(root, 'pose', {'Unspecified', 'Rear', 'Frontal', 'Left', 'Right'})
        else:
            return True
    else:
        return True


if pascal_validator_one_file(path) is True:
    print(path)

