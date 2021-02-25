from lxml import etree
from methods import *
import xml.etree.ElementTree as ET

#path = input("Podaj ścieżkę: ")
path = '../data_examples/VOC2012/Annotations/2007_000027.xml'

''' 
syntax_validator(path) is a function to validate syntax error. It works how it goes: we open xml file as txt file,
then transform it from string to the tree. If there is something wrong with the syntax, we can't transform it. 
'''

def syntax_validator(path):
    with open(path, 'r') as file:
        txt_xml_file = file.read().replace('','')
    try:
        etree.fromstring(txt_xml_file)
    except BaseException as e:
        print(e)


'''
check_extension is a function to check if file extension in attribute 'filename' is correct
'''

def check_extension(path):
    str_jpg = root.find('filename').text
    if str_jpg.endswith('.jpg') != True:
        print('Invalid file extension')


'''
bnd_validator is a function to validate if bndbox  has a right values of coordinates xmax, xmin, ymax, ymin.  
'''

def bndbox_validator(path):
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

    if len(list_xmax) == len(list_xmin) and len(list_ymax) == len(list_ymin) and len(list_xmax) == len(list_ymax):
        if diff_if_negative(list_xmax, list_xmin) == True or diff_if_negative(list_ymax, list_ymin) == True:
            print('Difference between coordinates xmax and xmin or ymax and ymin is negative: '
                  'fragmentation beyond the graph')
        for (i, j, k, l) in zip(list_xmax, list_xmin, list_ymax, list_ymin):
            if i <= width and i > 0 and j < width and j >= 0 and k <= height and k > 0 and l < height and l >= 0:
                continue
            else:
                print('Coordinates xmax, xmin, ymax, ymin are wrong with height and width value:'
                      ' fragmentation beyond the graph ')
    else:
        print('Wrong amount of coordinates xmax, xmin, ymax, ymin')

'''
dtd_validator is a function to validate if 'depth', 'truncated' and 'difficult' values are right.  
'''

def dtd_validator(path):
    for n in root.iter('depth'):
        if int(n.text) != 3 and int(n.text) != 0:
            print(" invalid value of 'depth' ")

    for n in root.iter('truncated'):
        if int(n.text) != 1 and int(n.text) != 0:
            print(" invalid value of 'truncated' ")

    for n in root.iter('difficult'):
        if int(n.text) != 1 and int(n.text) != 0:
            print(" invalid value of 'difficult' ")



syntax_validator(path)
bndbox_validator(path)

