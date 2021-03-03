from valid_functions_MT import *
import pytest

read_xml()

'''
def test_syntax_validator():
    #assert syntax_validator(path) == 1
    with pytest.raises(BaseException):
        syntax_validator(path)
'''

def test_check_extension():
    assert check_extension(str_jpg) is True

def test_bndbox_validator():
    assert bndbox_validator(size, width, height) is True

def test_values_validator():
    assert values_validator(root, 'depth', {0, 3}) is False
    assert values_validator(root, 'truncated', {0, 1}) is False
    assert values_validator(root, 'difficult', {0, 1}) is False