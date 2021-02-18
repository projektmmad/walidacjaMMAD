from lxml import *
from lxml import etree


def syntax_validator(path):
    with open(path, 'r') as file:
        txt_xml_file=file.read().replace('','')
    try:
        etree.fromstring(txt_xml_file)
    except BaseException as e:
        print(e)


path = '/home/sandra/Pulpit/mmad/VOC2012/Annotations/2007_000027.xml'
syntax_validator(path)
