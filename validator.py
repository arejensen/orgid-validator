#!/usr/bin/env python

# Norwegian organization id (organisasjonsnummer) validator.
# Copyright (C) 1985-1989, 1993-1995, 1997-2019 Free Software Foundation, Inc.
# This file is part of orgid_validator.
# orgid_validator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
# orgid_validator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with orgid_validator.  If not, see <https://www.gnu.org/licenses/>.

# NOTE: The code below is not exactly idiomatic Python, and arguable
#       over-commented. This is intentional as to match very closely to how the
#       algorithm is described by BRREG so that colleagues and neophytes can more
#       easily match the Python code with the BRREG description. The description can
#       be found in the README that should be included with this source code, or on
#       https://www.brreg.no/om-oss/oppgavene-vare/alle-registrene-vare/om-enhetsregisteret/organisasjonsnummeret/
#       as of 2019-02-01.

# These weights are provided by BRREG
weights = [3, 2, 7, 6, 5, 4, 3, 2]

def validate_orgid(orgid):

    # Convert the digits into a list of integers
    # (but first convert it to a string)
    digits = [int(id) for id in str(orgid)]

    # Length requirement
    if len(digits) != 9:
        return False
    sum = 0

    # Create control digit (last digit)
    for weight, digit in zip(weights, digits):
       sum = sum + (weight * digit)
    control = 11 - (sum % 11)

    # Conditions of failure (two conditions)
    # Condition 1:
    if control == 10: # this is the most opaque part of the algorithm description
        return False  # left seperate for illustration
    # Condition 2:
    elif control != digits[-1]: # This is the actual test
        return False

    # Counterfactual: The orgid must be correct
    else:
        return True
