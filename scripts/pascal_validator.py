from VOC2012_dir_structure import *

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


#path_to_VOC = '/home/annaw/VOCdevkit/VOC2012'
path_to_VOC = '/home/sandra/walidacjaMMAD/data_examples/VOC2012'
pascal_validator(path_to_VOC)