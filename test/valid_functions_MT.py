from lxml import etree
from methods import *
import xml.etree.ElementTree as ET

'''read_xml is a function to read a xml file'''

def read_xml():
    #path = input("Podaj ścieżkę: ")
    path = '../data_examples/VOC2012/Annotations/2007_000027.xml'
    tree = ET.parse(path)
    root = tree.getroot()
    str_jpg = root.find('filename').text
    source = root.find('source')
    database = source.find('database').text
    d_annotation = source.find('annotation').text
    size = root.find("size")
    width = int(size.find("width").text)
    height = int(size.find("height").text)
    return path, tree, root, str_jpg, database, d_annotation, size, width, height


''' 
syntax_validator(path) is a function to validate syntax error. It works how it goes: we open xml file as txt file,
then transform it from string to the tree. If there is something wrong with the syntax, we can't transform it. 
'''

def syntax_validator(path):
    with open(path, 'r') as file:
        txt_file = file.read().replace('','')
    try:
        etree.fromstring(txt_file)
    except BaseException as e:
        print(e)


'''check_database is a function to check if a file is from Pascal The VOC2007 database'''

def check_database(database, annotation):
    if database == "The VOC2007 Database" and annotation == "PASCAL VOC2007":
        return True
    else:
        print("File is not from Pascal The VOC2007 Database")
        return False


'''
check_extension is a function to check if file extension in attribute 'filename' is correct
'''

def check_extension(extension):
    if extension.endswith('.jpg') != True:
        print('Invalid file extension')
        return False
    return True


'''
bnd_validator is a function to validate if bndbox  has a right values of coordinates xmax, xmin, ymax, ymin.  
'''

def bndbox_validator(size, width, length):
    list_xmax = []
    list_xmin = []
    list_ymax = []
    list_ymin = []

    for branch in root.iter('bndbox'):
        list_xmax += [int(leaf.text) for leaf in branch if leaf.tag == 'xmax']
        list_xmin += [int(leaf.text) for leaf in branch if leaf.tag == 'xmin']
        list_ymax += [int(leaf.text) for leaf in branch if leaf.tag == 'ymax']
        list_ymin += [int(leaf.text) for leaf in branch if leaf.tag == 'ymin']

    if len(list_xmax) == len(list_xmin) and len(list_ymax) == len(list_ymin) and len(list_xmax) == len(list_ymax):
        if diff_if_negative(list_xmax, list_xmin) == True or diff_if_negative(list_ymax, list_ymin) == True:
            print('Difference between coordinates xmax and xmin or ymax and ymin is negative: '
                  'fragmentation beyond the graph')
            return False
        for (i, j, k, l) in zip(list_xmax, list_xmin, list_ymax, list_ymin):
            if 0 < i <= width and 0 <= j < width and 0 < k <= height and 0 <= l < height:
                continue
            else:
                print('Coordinates xmax, xmin, ymax, ymin are wrong with height and width value:'
                      ' fragmentation beyond the graph ')
                return False
    else:
        print('Wrong amount of coordinates xmax, xmin, ymax, ymin')
        return False
    return True


'''Values validator checks if a value of checked atribute is valid or not. It's a poprawioned version of dtd_validator'''

def values_validator(root, checked_atribute, valid_values):
    for n in root.iter(checked_atribute):
        #print(n) Tylko w celu sprawdzenia, czy funkcja sprawdza poprawny atrybut
        if int(n.text) in valid_values:
            return True
        else:
            print("Invalid value of " + checked_atribute)
            return False

def execute():
    path, tree, root, str_jpg, database, d_annotation, size, width, height = read_xml()
    syntax_validator(path)
    bndbox_validator(size, width, height)
    check_extension(str_jpg)
    check_database(database, d_annotation)
    values_validator(root, 'depth', {0, 3})
    values_validator(root, 'truncated', {0, 1})
    values_validator(root, 'difficult', {0, 1})

execute()