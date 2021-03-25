from methods import *

def check_folder_structure(path_to_VOC2012, dirname):
    if os.path.isdir(f'{path_to_VOC2012}/{dirname}') is False:
        print(f'Folder structure error: there is no {dirname} directory')
    else:
        return True

def VOC2012_trash(path_to_VOC):
    dir_name = ['Annotations', 'ImageSets', 'JPEGImages', 'SegmentationClass', 'SegmentationObject', '.git']
    dir_VOC = os.listdir(path_to_VOC)
    for katalog in dir_VOC:
        if not katalog in dir_name:
            print(f'Warning: additional directory or wrong dirname in VOC folder {katalog}')


def VOC2012_structure(path_to_VOC2012):
    VOC2012_trash(path_to_VOC2012)
    dir_name = ['Annotations', 'ImageSets', 'JPEGImages', 'SegmentationClass', 'SegmentationObject']
    if os.path.isdir(path_to_VOC2012) is True:
        for name in dir_name:
            check_folder_structure(path_to_VOC2012, name)
    else:
        print('Wrong path to VOC2012 folder')
        return False

