import pytest
from .data import invalid_orgids_non_type_error
from .data import invalid_orgids_type_error
from orgid_validator import validator


# These orgids were checked on BRREG's lookup and were identified by their service as invalid
@pytest.mark.parametrize("invalid_orgid", invalid_orgids_non_type_error)
def test_invalid_non_type_error(invalid_orgid):
    assert validator.validate_orgid(invalid_orgid) == False


# These orgids are obvious junk
@pytest.mark.parametrize("invalid_orgid", invalid_orgids_type_error)
def test_invalid_type_error(invalid_orgid):
    assert validator.validate_orgid(invalid_orgid) == False


# These orgids are obvious junk
# @pytest.mark.parametrize("invalid_orgid", invalid_orgids_type_error)
# def test_invalid_type_error(invalid_orgid):
#     with pytest.raises((TypeError, ValueError)):
#         assert validator.validate_orgid(invalid_orgid)
