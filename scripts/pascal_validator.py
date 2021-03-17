from validation_merge import *

path = '../data_examples/VOC2012/Annotations/2007_000027.xml'

def pascal_validator(path):
    dir_annotations = os.path.dirname(path)
    list_file = os.listdir(dir_annotations)
    for file in list_file:
        pascal_validator_one_file(f'{dir_annotations}/{file}')

pascal_validator(path)