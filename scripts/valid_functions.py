from methods import *

#path = input("Podaj ścieżkę: ")
path = '../data_examples/VOC2012/Annotations/2007_000027.xml'

''' 
syntax_validator(path) is a function to validate syntax error. It works how it goes: we open xml file as txt file,
then transform it from string to the tree. If there is something wrong with the syntax, we can't transform it. 
'''

def syntax_validator(path, filename):
    with open(path, 'r') as file:
        txt_xml_file = file.read().replace('','')
    try:
        etree.fromstring(txt_xml_file)
    except BaseException as e:
        print(f'{str(e)} in {str(filename)}')
        return False


def empty_value(tree, filename):
    empty_list = []
    compare_list =[]
    root = tree.getroot()
    tags = [e.tag for e in tree.findall('.//')]
    for k in set(tags):
        for m in root.iter(k):
            if m.text is None:
                empty_list.append(k)
    if empty_list!=compare_list:
        for j in empty_list:
            print(f"Empty value in {j} in {filename}")
    else:
        return False

'''
check_extension is a function to check if file extension in attribute 'filename' is correct
'''

def check_extension(str_jpg, filename):
    if str_jpg.endswith('.jpg') is not True:
        print(f'Invalid file extension in {filename}')



'''
great_bnd_validator is a function to validate if bndbox  has a right values of coordinates xmax, xmin, ymax, ymin.  
'''

def great_bnd_validator(root, width, height, filename):
    list_xmax = []
    list_xmin = []
    list_ymax = []
    list_ymin = []
    for branch in root.iter('bndbox'):
        list_xmax += [int(leaf.text) for leaf in branch if leaf.tag == 'xmax']
        list_xmin += [int(leaf.text) for leaf in branch if leaf.tag == 'xmin']
        list_ymax += [int(leaf.text) for leaf in branch if leaf.tag == 'ymax']
        list_ymin += [int(leaf.text) for leaf in branch if leaf.tag == 'ymin']
    bnd_validator1(list_xmax, list_xmin, list_ymax, list_ymin, filename)
    bnd_validator2(list_xmax, list_xmin, list_ymax, list_ymin, filename)
    bnd_validator3(list_xmax, list_xmin, list_ymax, list_ymin, width, height, filename)

def values_validator(root, checked_atribute, valid_values, filename):
    for n in root.iter(checked_atribute):
        if n.text in valid_values:
            return True
        else:
            print(f"Invalid value of {checked_atribute} in {filename}")
            return False


def correct_tag(tree, filename):
    name_tags = ['folder', 'filename', 'source', 'database', 'annotation', 'image', 'size',
            'width', 'height', 'depth','segmented', 'object', 'name', 'pose', 'truncated',
            'difficult', 'bndbox', 'xmin', 'ymin', 'xmax', 'ymax', 'part']
    tags = [e.tag for e in tree.findall('.//')]

    for element in tags:
        if element not in name_tags:
            print(f"Incorrect name of tag: there is tag named '{element}' in {filename}.  ")

def root_tag(root,filename):
    if root.tag != 'annotation':
        print(f'Incorrect name of root: {root.tag} in {filename}')



