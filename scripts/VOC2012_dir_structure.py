from validation_merge import *

def check_path(path_to_VOC):
    if os.path.isdir(path_to_VOC) is True:
        return True
    else:
        return False

def check_ann(path_to_VOC):
    if os.path.isdir(path_to_VOC + '/Annotations') is True:
        return True
    else:
        return False

def check_jpg(path_to_VOC):
    if os.path.isdir(path_to_VOC + '/JPEGImages') is True:
        return True
    else:
        return False

def check_structure(path_to_VOC):
    if check_path(path_to_VOC) is True:
        if check_ann(path_to_VOC) is False or check_jpg(path_to_VOC) is False:
            print("Folder structure error: there is no \"Annotations\" or \"JPEGImages\" directory")
            return False
    else:
        print('Wrong path to VOC folder')
        return False

def VOC_trash(path_to_VOC):
    dir_name = ['Annotations', 'ImageSets', 'JPEGImages', 'SegmentationClass', 'SegmentationObject', '.git']
    dir_VOC = os.listdir(path_to_VOC)
    for katalog in dir_VOC:
        if not katalog in dir_name:
            print(f'Warning: additional directory or wrong dirname in VOC folder {katalog}')

def VOC_warning_dir(path_to_VOC):
    dir_name = ['ImageSets', 'SegmentationClass', 'SegmentationObject']
    dir_VOC = os.listdir(path_to_VOC)
    for katalog in dir_name:
        if not katalog in dir_VOC:
            print(f'Warning: Missing folder: \"{katalog}\" ')

def trash_in_ann(path_to_VOC):
    for file_xml in os.listdir(path_to_VOC + '/Annotations'):
        if file_xml.endswith('.xml') is False:
            print(f"Error: Invalid file(s) in folder 'Annotations' - there should be only .xml files ")
            return False

def trash_in_jpg(path_to_VOC):
    for file_jpg in os.listdir(path_to_VOC + '/JPEGImages'):
        if file_jpg.endswith('.jpg') is False and file_jpg.endswith('.jpeg') is False:
            print(f"Error: Invalid file in folder 'JPEGImages' - there should be only .jp(e)g files ")
            return False

# jpg_xml(path_to_VOC) - the function checks if the files are the same in two folders: '/Annotations' and /JPEGImages'
def jpg_xml(path_to_VOC):
    lista_jpg = []
    lista_xml = []
    for file_xml in os.listdir(path_to_VOC + '/Annotations'):
        file_xml_split = file_xml.split(".")
        lista_xml.append(file_xml_split[0])
    for file_jpg in os.listdir(path_to_VOC + '/JPEGImages'):
        file_jpg_split = file_jpg.split(".")
        lista_jpg.append(file_jpg_split[0])
    help_xml = []
    for a in lista_xml:
        if a in lista_jpg:
            lista_jpg.remove(a)
        else:
            help_xml.append(a)
    if lista_jpg != []:
        print(f"The following name-files: {lista_jpg} in the folder 'JPEGImages' have no match in the folder '/Annotations' ")
    if help_xml != []:
        print(f"The following name-files: {help_xml} in the folder '/Annotations' have no match in the folder 'JPEGImages' ")


# VOC2012_trash(path_to_VOC) - the function checks if there are only xml files in the Annotation folder,
# jpg files in the JPEGImage and png files in SegmentationClass, SegmentationObject
def trash_folders(path_to_VOC):
    for file_xml in os.listdir(path_to_VOC + '/Annotations'):
        if file_xml.endswith('.xml') is not True:
            print(f"Invalid file '{file_xml}' in folder 'Annotations' ")
    for file_jpg in os.listdir(path_to_VOC + '/JPEGImages'):
        if file_jpg.endswith('.jpg') is not True:
            print(f"Invalid file '{file_jpg}' in folder 'JPEGImages' ")
    for file_png in os.listdir(path_to_VOC + '/SegmentationClass'):
        if file_png.endswith('.png') is not True:
            print(f"Invalid file '{file_png}' in folder 'SegmentationClass' ")
    for file_png in os.listdir(path_to_VOC + '/SegmentationObject'):
        if file_png.endswith('.png') is not True:
            print(f"Invalid file '{file_png}' in folder 'SegmentationObject' ")
