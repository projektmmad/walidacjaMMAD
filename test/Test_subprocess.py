import pytest
import subprocess
import os

pascal_voc_2012 = "python3 scripts/pascal_validator.py /home/tycha/Documents/VOCtrainval/VOCdevkit/VOC2012"


@pytest.mark.parametrize('path, expected', [(pascal_voc_2012, b'')])
@pytest.mark.skip(reason="No reason to testing this")
def test_pascal_voc_2012(path, expected):
    arg = path.split()
    proces = subprocess.Popen(arg, stdout = subprocess.PIPE)
    #subprocess.CompletedProcess(args=['python3', 'pascal_validator.py', "/home/tycha/Documents/VOCDevkit_test"], returncode=0, stdout=True)
    stdout, stderr = proces.communicate()
    assert stdout == expected

#@pytest.mark.parametrize('path, expected', [(pascal_voc_2012, b'')])
@pytest.mark.skip(reason="No reason to testing this")
def test_pascal_bracket_slash():
    arg = "python3 scripts/pascal_validator.py /home/tycha/Documents/VOCtest_podzielone/bracket_slash"
    arg = arg.split()
    proces = subprocess.Popen(arg, stdout=subprocess.PIPE)
    stdout, stderr = proces.communicate()
    with open("test/expected_outputs/bracket_slash.txt") as f:
        lines = f.readlines()
        #lines = [l for l in lines]
    print(lines)
    assert stdout in lines

invalid_depth = b'\nInvalid value of depth in 2007_000063.xml\nInvalid value of depth in 2007_000061.xml\n'
invalid_difficult = b'\nInvalid value of difficult in 2007_000121.xml\nInvalid value of difficult in 2007_000123.xml\nInvalid value of difficult in 2007_000129.xml'
invalid_truncated = b'\nInvalid value of truncated in 2007_000187.xml\nInvalid value of truncated in 2007_000170.xml\nInvalid value of truncated in 2007_000175.xml'
empty_depth = b'\nEmpty value in depth in 2007_000584.xml\nEmpty value in depth in 2007_000629.xml'
empty_difficult = b'\nEmpty value in difficult in 2007_000636.xml\nEmpty value in difficult in 2007_000645.xml'
empty_truncated = b'\nEmpty value in truncated in 2007_000661.xml\nEmpty value in truncated in 2007_000648.xml'
too_big_bndbox = b'Coordinates xmax, xmin, ymax, ymin are wrong with height and width value: fragmentation beyond the graph in 2007_000256.xml\n' \
                 b'Coordinates xmax, xmin, ymax, ymin are wrong with height and width value: fragmentation beyond the graph in 2007_000250.xml\n' \
                 b'Coordinates xmax, xmin, ymax, ymin are wrong with height and width value: fragmentation beyond the graph in 2007_000243.xml\n' \
                 b'Coordinates xmax, xmin, ymax, ymin are wrong with height and width value: fragmentation beyond the graph in 2007_000272.xml\n' \
                 b'Coordinates xmax, xmin, ymax, ymin are wrong with height and width value: fragmentation beyond the graph in 2007_000241.xml\n'
empty_bndbox = b'Empty value in ymin in 2007_000333.xml\n' \
               b'Empty value in xmax in 2007_000333.xml\n' \
               b'Empty value in ymax in 2007_000333.xml\n' \
               b'Empty value in xmin in 2007_000333.xml\n' \
               b'Empty value in xmin in 2007_000332.xml\n' \
               b'Empty value in ymin in 2007_000323.xml\n'
invalid_annotation = b'Incorrect name of filename: 2007_000823.jpg in 2007_000822.xml\n' \
                     b'Incorrect name of filename: 2007_0008368.jpg in 2007_000836.xml\n' \
                     b'Incorrect name of filename: 007_000847.jpg in 2007_000847.xml\n' \
                     b'Incorrect name of filename: 2007_00083.jpg in 2007_000830.xml\n' \
                     b'Incorrect name of filename: 2007_00083773.jpg in 2007_000837.xml'



@pytest.mark.parametrize('path, expected', [("invalid_depth", invalid_depth), ("invalid_difficult", invalid_difficult), ("invalid_truncated", invalid_truncated),
                                            ("empty_depth", empty_depth), ("empty_difficult", empty_difficult), ("empty_truncated", empty_truncated),
                                            ("too_big_bndbox", too_big_bndbox), ("invalid_annotation", invalid_annotation), ("empty_bndbox", empty_bndbox)])
def test_pascal_invalid_values(path, expected):
    arg = "python3 scripts/pascal_validator.py /home/tycha/Documents/VOCtest_podzielone/" + path
    arg = arg.split()
    proces = subprocess.Popen(arg, stdout=subprocess.PIPE)
    stdout, stderr = proces.communicate()
    assert expected in stdout