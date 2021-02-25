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
    else:
        print('Amount of bndbox coordinate is wrong.')
    for var in list_with_diff:
        if var < 0:
            return True



