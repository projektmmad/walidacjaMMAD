from methods import *

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
        return False

'''
check_extension is a function to check if file extension in attribute 'filename' is correct
'''

def check_extension(str_jpg):
    if str_jpg.endswith('.jpg') != True:
        print('Invalid file extension')


'''
great_bnd_validator is a function to validate if bndbox  has a right values of coordinates xmax, xmin, ymax, ymin.  
'''

def great_bnd_validator(root, width, height):
    if empty_min_max(root) != False:
        list_xmax = []
        list_xmin = []
        list_ymax = []
        list_ymin = []

        for branch in root.iter('bndbox'):
            list_xmax += [int(leaf.text) for leaf in branch if leaf.tag == 'xmax']
            list_xmin += [int(leaf.text) for leaf in branch if leaf.tag == 'xmin']
            list_ymax += [int(leaf.text) for leaf in branch if leaf.tag == 'ymax']
            list_ymin += [int(leaf.text) for leaf in branch if leaf.tag == 'ymin']
        bnd_validator1(list_xmax, list_xmin, list_ymax, list_ymin)
        bnd_validator2(list_xmax, list_xmin, list_ymax, list_ymin)
        bnd_validator3(list_xmax, list_xmin, list_ymax, list_ymin, width, height)
    else:
        return None

def values_validator(root, checked_atribute, valid_values):
    for n in root.iter(checked_atribute):
        # print(n) Tylko w celu sprawdzenia, czy funkcja sprawdza poprawny atrybut
        if int(n.text) in valid_values:
            return True
        else:
            print("Invalid value of " + checked_atribute)
            return False
