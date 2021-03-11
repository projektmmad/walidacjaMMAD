from lxml import etree
from methods import *
import xml.etree.ElementTree as ET
import glob

'''read_xml is a function to read a xml file'''

def xml_files(path):
    xmlfiles = []
    for file in glob.glob(path + '/' + '*.xml'):
        xmlfiles.append(file)
    print(xmlfiles)
    return xmlfiles


def read_xml(path):
    path = path
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

'''
bnd_validator is a function to validate if bndbox  has a right values of coordinates xmax, xmin, ymax, ymin.  
'''

'''
def empty_min_max(path):
    for k in ['xmax', 'xmin','ymax','ymin']:
        for m in root.iter(k):
            if m.text == None:
                print('Empty value in',k )

tree = ET.parse(path)
root = tree.getroot()
list_xmax = []
list_xmin = []
list_ymax = []
list_ymin = []

for branch in root.iter('bndbox'):
    list_xmax += [int(leaf.text) for leaf in branch if leaf.tag == 'xmax']
    list_xmin += [int(leaf.text) for leaf in branch if leaf.tag == 'xmin']
    list_ymax += [int(leaf.text) for leaf in branch if leaf.tag == 'ymax']
    list_ymin += [int(leaf.text) for leaf in branch if leaf.tag == 'ymin']


size = root.find("size")
width = int(size.find("width").text)
height = int(size.find("height").text)




def bnd_validator1(path):
    if len(list_xmax) != len(list_xmin) or len(list_ymax) != len(list_ymin) or len(list_xmax) != len(list_ymax):
        print('Wrong amount of coordinates xmax, xmin, ymax, ymin')

def bnd_validator2(path):
    if diff_if_negative(list_xmax, list_xmin) == True or diff_if_negative(list_ymax, list_ymin) == True:
        print('Difference between coordinates xmax and xmin or ymax and ymin is negative: '
              'fragmentation beyond the graph ndaisodja')
def bnd_validator3(path):
    for (i, j, k, l) in zip(list_xmax, list_xmin, list_ymax, list_ymin):
        if i <= width and i > 0 and j < width and j >= 0 and k <= height and k > 0 and l < height and l >= 0:
            continue
        else:
            print('Coordinates xmax, xmin, ymax, ymin are wrong with height and width value:'
                  ' fragmentation beyond the graph ')

'''

'''Values validator checks if a value of checked atribute is valid or not. It's a poprawioned version of dtd_validator'''

def values_validator(root, checked_atribute, valid_values):
    for n in root.iter(checked_atribute):
        #print(n) Tylko w celu sprawdzenia, czy funkcja sprawdza poprawny atrybut
        if int(n.text) in valid_values:
            return True
        else:
            print("Invalid value of " + checked_atribute)
            return False

lista = xml_files('../data_examples/VOC2012/Annotations')

def execute(path):
    read_xml(path)
    path, tree, root, str_jpg, database, d_annotation, size, width, height = read_xml(path)
    syntax_validator(path)
    #bndbox_validator(root, size, width, height)
    check_extension(str_jpg)
    check_database(database, d_annotation)
    values_validator(root, 'depth', {0, 3})
    values_validator(root, 'truncated', {0, 1})
    values_validator(root, 'difficult', {0, 1})

for i in range(len(lista)):
    execute(lista[i])