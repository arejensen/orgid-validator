import pytest

from orgid_validator import validator

# These orgids were picked from BRREG itself and must therefore be valid
from .data import valid_orgids_int
from .data import valid_orgids_float
from .data import valid_orgids_str
from .data import valid_orgids_str_float


# Orgids in int form
@pytest.mark.parametrize('valid_orgid', valid_orgids_int)
def test_valid_int(valid_orgid):
    assert validator.validate_orgid(valid_orgid)


# Orgids as floating point values
@pytest.mark.parametrize('valid_orgid', valid_orgids_float)
def test_valid_float(valid_orgid):
    assert validator.validate_orgid(valid_orgid)


# # Orgids as strings
# @pytest.mark.parametrize('valid_orgid', valid_orgids_str)
# def test_valid_str(valid_orgid):
#     assert validator.validate_orgid(valid_orgid)


# # Orgids as strings, but floats in the numeric sense
# @pytest.mark.parametrize('valid_orgid', valid_orgids_str_float)
# def test_valid_str_float(valid_orgid):
#     assert validator.validate_orgid(valid_orgid)