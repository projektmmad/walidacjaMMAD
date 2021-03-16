from lxml import etree
import xml.etree.ElementTree as ET

'''
diff_if_negative is a method that count a difference between two lists, element by element, like a vector difference,
coordinate by coordinate, then check if every difference is negative, if it is so - diff_if_negative returns True.
We need it for bndbox_validator function.
'''

def diff_if_negative(list1, list2):
    list_with_diff = []
    if len(list1) == len(list2):
        for i in range(0, len(list1)):
            list_with_diff.append(list1[i] - list2[i])
    for var in list_with_diff:
        if var < 0:
            return True


def bnd_validator1(xmax, xmin, ymax, ymin):
    if len(xmax) != len(xmin) or len(ymax) != len(ymin) or len(xmax) != len(ymax):
        print('Wrong amount of coordinates xmax, xmin, ymax, ymin')
def bnd_validator2(xmax, xmin, ymax, ymin):
    if diff_if_negative(xmax, xmin) == True or diff_if_negative(ymax, ymin) == True:
        print('Difference between coordinates xmax and xmin or ymax and ymin is negative: '
              'fragmentation beyond the graph')
def bnd_validator3(xmax, xmin, ymax, ymin, width, height):
    for (i, j, k, l) in zip(xmax, xmin, ymax, ymin):
        if i <= width and i > 0 and j < width and j >= 0 and k <= height and k > 0 and l < height and l >= 0:
            continue
        else:
            print('Coordinates xmax, xmin, ymax, ymin are wrong with height and width value:'
                  ' fragmentation beyond the graph ')


