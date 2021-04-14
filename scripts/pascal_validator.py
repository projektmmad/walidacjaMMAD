from pascal_voc_structure import *
from pascal_validator_one_file import *
import argparse

def pascal_validator(path_to_VOC):
    if check_structure(path_to_VOC) is not False:
        VOC_trash(path_to_VOC)
        VOC_warning_dir(path_to_VOC)
        if trash_in_ann(path_to_VOC) is not False and trash_in_jpg(path_to_VOC) is not False:
            jpg_xml(path_to_VOC)
            dir_annotations = path_to_VOC + '/Annotations'
            list_file = os.listdir(dir_annotations)
            for file in list_file:
                pascal_validator_one_file(f'{dir_annotations}/{file}')

parser = argparse.ArgumentParser()
parser.add_argument('path', help='path to the file')
args = parser.parse_args()

pascal_validator(args.path)