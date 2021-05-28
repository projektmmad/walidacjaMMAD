from pascal_voc_structure import *
from pascal_validator_one_file import *
import argparse
from argparse import RawTextHelpFormatter

def pascal_validator(path_to_voc: str):
   if check_folder_structure(path_to_voc) is not False:
        voc_warning_add_dir(path_to_voc)
        voc_warning_miss_dir(path_to_voc)
        if trash_in_ann_jpg(path_to_voc) is True:
            jpg_xml(path_to_voc)
            dir_annotations = os.path.join(path_to_voc, 'Annotations')
            list_file = os.listdir(dir_annotations)
            for file in list_file:
                pascal_validator_one_file(os.path.join(dir_annotations, file))


def pascal_validator_only_xml(path_to_voc: str):
    dir_annotations = os.path.join(path_to_voc, 'Annotations')
    list_file = os.listdir(dir_annotations)
    for file in list_file:
        pascal_validator_one_file(os.path.join(dir_annotations, file))


def pascal_validator_only_syntax(path_to_voc: str):
    dir_annotations = os.path.join(path_to_voc, 'Annotations')
    list_file = os.listdir(dir_annotations)
    for file in list_file:
        pascal_validator_one_file_syntax(os.path.join(dir_annotations, file))


def argparse_pascal_validator(path_to_voc: str, choose: str):
    if choose == 'all':
        pascal_validator(path_to_voc)
    if choose == 'only_xml':
        pascal_validator_only_xml(path_to_voc)
    if choose == 'only_syntax':
        pascal_validator_only_syntax(path_to_voc)


parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
parser.add_argument('path', help="Path to the VOC folder. Even if you want to check only xml or only syntax \n"
                                 "you have to insert 'Annotation' folder into VOC folder.")
parser.add_argument('-c', '--choose', default='all', help="Useful to choose validation type. \n"
                                                          "Default is 'all' - check all VOC folder, even structure. \n"
                                                          "If you want to check only xml use 'only_xml'. \n"
                                                          "For checking only xml syntax use 'only_syntax'.")
args = parser.parse_args()
argparse_pascal_validator(args.path, args.choose)
