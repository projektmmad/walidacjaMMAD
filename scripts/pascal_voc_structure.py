from pascal_validator_one_file import *


def check_path(path_to_voc: str):
    if os.path.isdir(path_to_voc) is True:
        return True
    else:
        return False


def check_ann(path_to_voc: str):
    if os.path.isdir(os.path.join(path_to_voc, 'Annotations')) is True:
        return True
    else:
        return False


def check_jpg(path_to_voc: str):
    if os.path.isdir(os.path.join(path_to_voc, 'JPEGImages')) is True:
        return True
    else:
        return False


def check_folder_structure(path_to_voc: str):
    if check_path(path_to_voc) is True:
        if check_ann(path_to_voc) is False or check_jpg(path_to_voc) is False:
            print("Folder structure error: there is no \"Annotations\" or \"JPEGImages\" directory")
            return False
    else:
        print('Wrong path to VOC folder')
        return False


def voc_warning_add_dir(path_to_voc: str):
    dir_name = ['Annotations', 'ImageSets', 'JPEGImages', 'SegmentationClass', 'SegmentationObject', '.git']
    dir_voc = os.listdir(path_to_voc)
    for cat in dir_voc:
        if not cat in dir_name:
            print(f'Warning: additional directory or wrong dirname in VOC folder {cat}')


def voc_warning_miss_dir(path_to_voc: str):
    dir_name = ['ImageSets', 'SegmentationClass', 'SegmentationObject']
    dir_voc = os.listdir(path_to_voc)
    for cat in dir_name:
        if not cat in dir_voc:
            print(f'Warning: Missing folder: \"{cat}\" ')


def trash_in_ann(path_to_voc: str):
    for file_xml in os.listdir(os.path.join(path_to_voc, 'Annotations')):
        if file_xml.endswith('.xml') is False:
            print(f"Error: Invalid file '{file_xml}' in folder 'Annotations' - there should be only .xml files ")
            return False


def trash_in_jpg(path_to_voc: str):
    for file_jpg in os.listdir(os.path.join(path_to_voc, 'JPEGImages')):
        if file_jpg.endswith('.jpg') is False and file_jpg.endswith('.jpeg') is False:
            print(f"Error: Invalid file '{file_jpg} in folder 'JPEGImages' - there should be only .jp(e)g files ")
            return False


def jpg_xml(path_to_voc: str):
    """
    jpg_xml(path_to_VOC) - the function checks if the files are the same in two folders: '/Annotations' and /JPEGImages'
    """

    list_jpg = []
    list_xml = []
    for file_xml in os.listdir(os.path.join(path_to_voc, 'Annotations')):
        file_xml_split = file_xml.split(".")
        list_xml.append(file_xml_split[0])
    for file_jpg in os.listdir(os.path.join(path_to_voc, 'JPEGImages')):
        file_jpg_split = file_jpg.split(".")
        list_jpg.append(file_jpg_split[0])
    help_xml = []
    for a in list_xml:
        if a in list_jpg:
            list_jpg.remove(a)
        else:
            help_xml.append(a)
    if list_jpg != []:
        print(f"The following name-files: {list_jpg} in the folder 'JPEGImages' have no match in the folder '/Annotations' ")
    if help_xml != []:
        print(f"The following name-files: {help_xml} in the folder '/Annotations' have no match in the folder 'JPEGImages' ")


def trash_folders(path_to_voc: str):
    """
    VOC2012_trash(path_to_VOC) - the function checks if there are only xml files in the Annotation folder,
    jpg files in the JPEGImage and png files in SegmentationClass, SegmentationObject
    """

    for file_xml in os.listdir(os.path.join(path_to_voc, 'Annotations')):
        if file_xml.endswith('.xml') is not True:
            print(f"Invalid file '{file_xml}' in folder 'Annotations' ")
    for file_jpg in os.listdir(os.path.join(path_to_voc + 'JPEGImages')):
        if file_jpg.endswith('.jpg') is not True:
            print(f"Invalid file '{file_jpg}' in folder 'JPEGImages' ")
    for file_png in os.listdir(os.path.join(path_to_voc, 'SegmentationClass')):
        if file_png.endswith('.png') is not True:
            print(f"Invalid file '{file_png}' in folder 'SegmentationClass' ")
    for file_png in os.listdir(os.path.join(path_to_voc, 'SegmentationObject')):
        if file_png.endswith('.png') is not True:
            print(f"Invalid file '{file_png}' in folder 'SegmentationObject' ")
