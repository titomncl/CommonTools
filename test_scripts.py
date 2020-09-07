import pytest

from concat import concat
from check_nomenclature import check

# parameters = [("TEST_C_testing_jnt")]

# @pytest.mark.parametrize("text", parameters)
def test_check_nomenclature():
    sel = ["TEST_C_testing_jnt", "TEST_L_testing_jntEnd", "TEST_R_testing_ikhl",
           "TEST_SKL_grp", "effector1"]

    check(sel)
