from lxml import etree


def diff_if_negative(list1: list, list2: list):
    """
    diff_if_negative is a method that count a difference between two lists, element by element, like a vector difference,
    coordinate by coordinate, then check if every difference is negative, if it is so - diff_if_negative returns True.
    We need it for bndbox_validator function.
    """

    list_with_diff = []
    if len(list1) == len(list2):
        for i in range(0, len(list1)):
            list_with_diff.append(list1[i] - list2[i])
    for var in list_with_diff:
        if var < 0:
            return True


def bnd_validator_amount_cor(xmax: list, xmin: list, ymax: list, ymin: list, filename: str):
    if len(xmax) != len(xmin) or len(ymax) != len(ymin) or len(xmax) != len(ymax):
        print(f'Wrong amount of coordinates xmax, xmin, ymax, ymin in {filename}')


def bnd_validator_diff_cor(xmax: list, xmin: list, ymax: list, ymin: list, filename: str):
    if diff_if_negative(xmax, xmin) is True or diff_if_negative(ymax, ymin) is True:
        print(f'Difference between coordinates xmax and xmin or ymax and ymin is negative: '
              f'fragmentation beyond the graph in {filename}')


def bnd_validator_compare_size(xmax: list, xmin: list, ymax: list, ymin: list, width: float, height: float, filename: str):
    for (i, j, k, l) in zip(xmax, xmin, ymax, ymin):
        if 0 < i <= width and 0 < j < width and 0 < k <= height and 0 <= l < height:
            continue
        else:
            print(f'Coordinates xmax, xmin, ymax, ymin are wrong with height and width value:'
                  f' fragmentation beyond the graph in {filename}')


def syntax_validator(path: str, filename: str):
    """
    syntax_validator(path) is a function to validate syntax error. It works how it goes: we open xml file as txt file,
    then transform it from string to the tree. If there is something wrong with the syntax, we can't transform it.
    """

    with open(path, 'r') as file:
        txt_xml_file = file.read().replace('','')
    try:
        etree.fromstring(txt_xml_file)
    except BaseException as e:
        print(f'{str(e)} in {str(filename)}')
        return False


def check_if_empty_value(tree, filename: str):
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


def check_extension(str_jpg: str, root, filename: str):
    """
    check_extension is a function to check if file extension in attribute 'filename' is correct
    """
    for i in root.iter('filename'):
        if str_jpg.endswith('.jpg') is not True:
            print(f'Invalid file extension: {i.text} in {filename}')


def great_bnd_validator(root, width: float, height: float, filename: str):
    """
    great_bnd_validator is a function to validate if bndbox  has a right values of coordinates xmax, xmin, ymax, ymin.
    """

    list_xmax = []
    list_xmin = []
    list_ymax = []
    list_ymin = []
    for branch in root.iter('bndbox'):
        list_xmax += [float(leaf.text) for leaf in branch if leaf.tag == 'xmax']
        list_xmin += [float(leaf.text) for leaf in branch if leaf.tag == 'xmin']
        list_ymax += [float(leaf.text) for leaf in branch if leaf.tag == 'ymax']
        list_ymin += [float(leaf.text) for leaf in branch if leaf.tag == 'ymin']
    bnd_validator_amount_cor(list_xmax, list_xmin, list_ymax, list_ymin, filename)
    bnd_validator_diff_cor(list_xmax, list_xmin, list_ymax, list_ymin, filename)
    bnd_validator_compare_size(list_xmax, list_xmin, list_ymax, list_ymin, width, height, filename)


def values_validator(root, checked_atribute, valid_values, filename: str):
    for n in root.iter(checked_atribute):
        if n.text in valid_values:
            return True
        else:
            print(f"Invalid value of {checked_atribute} in {filename}")
            return False


def correct_tag(tree, filename: str):
    name_tags = ['folder', 'filename', 'source', 'database', 'annotation', 'image', 'size',
                 'width', 'height', 'depth']
    tags = [e.tag for e in tree.findall('.//')]

    for element in name_tags:
        if element not in tags:
            print(f"Missing tag '{element}' in {filename}.  ")
            return False


def root_tag(root, filename: str):
    if root.tag != 'annotation':
        print(f'Incorrect name of root: {root.tag} in {filename}')


def correct_filename(root, filename: str):
    for i in root.iter('filename'):
        name_file = i.text
        name_file_split = name_file.split(".")
        f_split = filename.split(".")
        if name_file_split[0] != f_split[0]:
            print(f"Incorrect name of filename: {i.text} in {filename}")
