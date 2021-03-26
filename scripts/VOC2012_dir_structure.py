from methods import *

def check_folder_structure(path_to_VOC2012, dirname):
    if os.path.isdir(f'{path_to_VOC2012}/{dirname}') is False:
        print(f'Folder structure error: there is no {dirname} directory')
    else:
        return True

def VOC2012_structure(path_to_VOC2012):
    dir_name = ['Annotations', 'ImageSets', 'JPEGImages', 'SegmentationClass', 'SegmentationObject']
    if os.path.isdir(path_to_VOC2012) is True:
        for name in dir_name:
            check_folder_structure(path_to_VOC2012, name)
    else:
        print('Wrong path to VOC2012 folder')
        return False


# VOC2012_trash(path_to_VOC) - the function checks if there are any unnecessary files in the VOC folder
def VOC2012_trash(path_to_VOC):
    dir_name = ['Annotations', 'ImageSets', 'JPEGImages', 'SegmentationClass', 'SegmentationObject', '.git']
    dir_VOC = os.listdir(path_to_VOC)
    for katalog in dir_VOC:
        if not katalog in dir_name:
            print(f'Warning: additional directory or wrong dirname in VOC folder {katalog}')


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


# jpg_xml(path_to_VOC) - the function checks if the files are the same in two folders: '/Annotations' and /JPEGImages'

def jpg_xml(path_to_VOC):
    lista_jpg = []
    lista_xml = []
    for file_xml in os.listdir(path_to_VOC + '/Annotations'):
        file_xml_split = file_xml.split(".")
        lista_xml.append(file_xml_split[0])
    print(lista_xml)
    for file_jpg in os.listdir(path_to_VOC + '/JPEGImages'):
        file_jpg_split = file_jpg.split(".")
        lista_jpg.append(file_jpg_split[0])
    print(lista_jpg)
    help_xml=[]
    for a in lista_xml:
        if a in lista_jpg:
            lista_jpg.remove(a)
        else:
            help_xml.append(a)
    if lista_jpg != []:
        print(f"The following name-files: {lista_jpg} in the folder 'JPEGImages' have no match in the folder '/Annotations' ")
    if help_xml != []:
        print(f"The following name-files: {help_xml} in the folder '/Annotations' have no match in the folder 'JPEGImages' ")


#path_to_VOC = '/home/sandra/walidacjaMMAD/data_examples/VOC2012'
#jpg_xml(path_to_VOC)


