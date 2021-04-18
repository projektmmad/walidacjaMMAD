import sys
import os
import pytest
import warnings

sys.path.append('/.../walidacjaMMAD/scripts')

import scripts
import scripts.pascal_validator as pv


def test_pascal_validator_onefile():
    with pytest.warns(UserWarning, match="Check_extension_warning"):
        pv.pascal_validator_one_file('../data_examples/VOC2012/Annotations/2007_000027.xml')
    with pytest.warns(UserWarning, match="Value_validator_warning"):
        pv.pascal_validator_one_file('../data_examples/VOC2012/Annotations/2007_000027.xml')


test_pascal_validator_onefile()
