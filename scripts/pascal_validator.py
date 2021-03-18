from validation_merge import *
from VOC2012_dir_structure import VOC2012_structure

path_to_VOC = '/home/annaw/VOCdevkit/VOC2012'

def pascal_validator(path_to_VOC):
    if VOC2012_structure(path_to_VOC) is not False:
        dir_annotations = path_to_VOC+'/Annotations'
        list_file = os.listdir(dir_annotations)
        for file in list_file:
            pascal_validator_one_file(f'{dir_annotations}/{file}')

pascal_validator(path_to_VOC)