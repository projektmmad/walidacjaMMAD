from pascal_voc_structure import *
from pascal_validator_one_file import *
import argparse


def pascal_validator(path_to_voc: str):
   if check_folder_structure(path_to_voc) is not False:
        voc_warning_add_dir(path_to_voc)
        voc_warning_miss_dir(path_to_voc)
        if trash_in_ann(path_to_voc) is not False or trash_in_jpg(path_to_voc) is not False:
            jpg_xml(path_to_voc)
            dir_annotations = os.path.join(path_to_voc, 'Annotations')
            list_file = os.listdir(dir_annotations)
            for file in list_file:
                pascal_validator_one_file(os.path.join(dir_annotations, file))


parser = argparse.ArgumentParser()
parser.add_argument('path', help='path to the file')
args = parser.parse_args()
pascal_validator(args.path)
