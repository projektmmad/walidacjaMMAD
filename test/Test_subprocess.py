import pytest
import subprocess
import argparse

command_line= "python3 scripts/pascal_validator.py /home/tycha/Documents/VOCDevkit_test"
command_line2 = "python3 scripts/pascal_validator.py /home/tycha/Documents/VOCtrainval/VOCdevkit/VOC2012"
command_line3 = "python3 scripts/pascal_validator.py /home/tycha/PycharmProjects/walidacjaMMAD/data_examples/VOC2012"

'''
parser = argparse.ArgumentParser()
parser.add_argument('path', help='path to the file')
args = parser.parse_args()
'''

@pytest.mark.parametrize('path, expected', [(command_line, b''), (command_line2, b''), (command_line3, b'')])
def test_pascal_validator(path, expected):
    arg = path.split()
    proces = subprocess.Popen(arg, stdout = subprocess.PIPE)
    #subprocess.CompletedProcess(args=['python3', 'pascal_validator.py', "/home/tycha/Documents/VOCDevkit_test"], returncode=0, stdout=True)
    stdout, stderr = proces.communicate()
    assert stdout == expected


'''
@pytest.fixture()
def popen_pascal_validator(path):
    path = path.split()
    proces = subprocess.Popen(path, stdout=subprocess.PIPE)
    stdout, stderr = proces.communicate()
    return stdout

def test_pascal_validator(popen_pascal_validator, exp_print):
    assert popen_pascal_validator.path == exp_print
'''