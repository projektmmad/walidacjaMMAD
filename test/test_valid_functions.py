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
    assert check_extension(path) == 0

def test_bndbox_validator():
    assert bndbox_validator(path) == 0

def test_dtd_validator():
    assert dtd_validator(path) == 0