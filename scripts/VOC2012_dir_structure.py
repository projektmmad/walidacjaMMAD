from methods import *

def check_folder_structure(path_to_VOC2012, dirname):
    if os.path.isdir(f'{path_to_VOC2012}/{dirname}') is False:
        print(f'Folder structure error: there is no {dirname} directory')


def VOC2012_structure(path_to_VOC2012):
    if os.path.isdir(path_to_VOC2012) is True:
        check_folder_structure(path_to_VOC2012, 'Annotations')
        check_folder_structure(path_to_VOC2012, 'ImageSets')
        check_folder_structure(path_to_VOC2012, 'JPEGImages')
        check_folder_structure(path_to_VOC2012, 'SegmentationClass')
        check_folder_structure(path_to_VOC2012, 'SegmentationObject')
    else:
        print('Wrong path to VOC2012 folder')
        return False
