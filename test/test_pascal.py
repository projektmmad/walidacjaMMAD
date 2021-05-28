import pytest
import subprocess
import os

pascal_voc_2012 = "python3 scripts/pascal_validator.py /home/tycha/Documents/VOCtrainval/VOCdevkit/VOC2012"

invalid_depth = {'Invalid value of depth in 2007_000063.xml', 'Invalid value of depth in 2007_000061.xml'}

invalid_difficult = {'Invalid value of difficult in 2007_000121.xml', 'Invalid value of difficult in 2007_000123.xml', 'Invalid value of difficult in 2007_000129.xml'}

invalid_truncated = {'Invalid value of truncated in 2007_000187.xml', 'Invalid value of truncated in 2007_000170.xml', 'Invalid value of truncated in 2007_000175.xml'}

empty_depth = {'Empty value in depth in 2007_000584.xml', 'Empty value in depth in 2007_000629.xml'}

empty_difficult = {'Empty value in difficult in 2007_000636.xml', 'Empty value in difficult in 2007_000645.xml'}

empty_truncated = {'Empty value in truncated in 2007_000661.xml', 'Empty value in truncated in 2007_000648.xml'}

too_big_bndbox = {'Coordinates xmax, xmin, ymax, ymin are wrong with height and width value: fragmentation beyond the graph in 2007_000256.xml',
                'Coordinates xmax, xmin, ymax, ymin are wrong with height and width value: fragmentation beyond the graph in 2007_000250.xml',
                'Coordinates xmax, xmin, ymax, ymin are wrong with height and width value: fragmentation beyond the graph in 2007_000243.xml',
                'Coordinates xmax, xmin, ymax, ymin are wrong with height and width value: fragmentation beyond the graph in 2007_000272.xml',
                'Coordinates xmax, xmin, ymax, ymin are wrong with height and width value: fragmentation beyond the graph in 2007_000241.xml'}

empty_bndbox = {'Empty value in ymin in 2007_000333.xml', 'Empty value in xmax in 2007_000333.xml', 'Empty value in ymax in 2007_000333.xml',
                'Empty value in xmin in 2007_000333.xml', 'Empty value in ymin in 2007_000323.xml', 'Empty value in xmin in 2007_000332.xml'}

invalid_annotation = {'Incorrect name of filename: 2007_000823.jpg in 2007_000822.xml', 'Incorrect name of filename: 2007_0008368.jpg in 2007_000836.xml',
                      'Incorrect name of filename: 007_000847.jpg in 2007_000847.xml', 'Incorrect name of filename: 2007_00083.jpg in 2007_000830.xml',
                      'Incorrect name of filename: 2007_00083773.jpg in 2007_000837.xml'}

bracket_slash = {"expected '>', line 16, column 2 (<string>, line 16) in 2007_000464.xml",
                "Opening and ending tag mismatch: annotation line 2 and folder, line 3, column 25 (<string>, line 3) in 2007_000480.xml",
                "expected '>', line 28, column 1 (<string>, line 28) in 2007_000528.xml",
                "expected '>', line 24, column 4 (<string>, line 24) in 2007_000504.xml",
                "Opening and ending tag mismatch: database line 6 and source, line 9, column 11 (<string>, line 9) in 2007_000549.xml",
                "Opening and ending tag mismatch: ymin line 35 and bndbox, line 38, column 12 (<string>, line 38) in 2007_000559.xml",
                "error parsing attribute name, line 15, column 13 (<string>, line 15) in 2007_000515.xml",
                "expected '>', line 29, column 1 (<string>, line 29) in 2007_000491.xml",
                "Opening and ending tag mismatch: bndbox line 33 and xmax, line 36, column 19 (<string>, line 36) in 2007_000529.xml",
                "Opening and ending tag mismatch: bndbox line 38 and object, line 39, column 11 (<string>, line 39) in 2007_000572.xml"}

xminbiggerxmax = {'Difference between coordinates xmax and xmin or ymax and ymin is negative: fragmentation beyond the graph in 2007_000363.xml',
                 'Difference between coordinates xmax and xmin or ymax and ymin is negative: fragmentation beyond the graph in 2007_000346.xml',
                 'Difference between coordinates xmax and xmin or ymax and ymin is negative: fragmentation beyond the graph in 2007_000364.xml',
                 'Coordinates xmax, xmin, ymax, ymin are wrong with height and width value: fragmentation beyond the graph in 2007_000364.xml'}
yminbiggerymax = {'Difference between coordinates xmax and xmin or ymax and ymin is negative: fragmentation beyond the graph in 2007_000392.xml',
                 'Difference between coordinates xmax and xmin or ymax and ymin is negative: fragmentation beyond the graph in 2007_000452.xml',
                 'Difference between coordinates xmax and xmin or ymax and ymin is negative: fragmentation beyond the graph in 2007_000423.xml'}
invalid_extension = {'Invalid file extension: 2007_000032.pg in 2007_000032.xml',
                    'Invalid file extension: 2007_000042 in 2007_000042.xml',
                    'Invalid file extension: 2007_000033.jg in 2007_000033.xml',
                    'Invalid file extension: 2007_000027.jp in 2007_000027.xml',
                    'Invalid file extension: 2007_000039.gif in 2007_000039.xml'}


@pytest.mark.parametrize('path, expected', [("invalid_depth", invalid_depth), ("invalid_difficult", invalid_difficult), ("invalid_truncated", invalid_truncated),
                                            ("empty_depth", empty_depth), ("empty_difficult", empty_difficult), ("empty_truncated", empty_truncated),
                                            ("too_big_bndbox", too_big_bndbox), ("invalid_annotation", invalid_annotation), ("bracket_slash", bracket_slash),
                                            ("xminbiggerxmax", xminbiggerxmax), ("yminbiggerymax", yminbiggerymax), ("invalid_extension", invalid_extension),
                                            ("empty_bndbox", empty_bndbox), ("invalid_annotation", invalid_annotation)])

def test_pascal_invalid_values(path, expected):
    arg = "python3 scripts/pascal_validator.py /home/tycha/Documents/VOCtest_podzielone/" + path
    arg = arg.split()
    stdout = subprocess.check_output(arg, encoding="utf8")
    assert all(outputs in stdout for outputs in expected)