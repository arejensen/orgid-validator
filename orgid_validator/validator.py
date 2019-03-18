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
WEIGHTS = [3, 2, 7, 6, 5, 4, 3, 2]

def validate_orgid(orgid):
    """
    Checks passed argument, orgid, against the algorithm used to create
    Norwegian Organizational IDs.

    Returns True if it validates, False otherwise.
    """
    # Convert the digits into a list of integers
    # (but first convert it to a string)
    digits = [int(id) for id in str(orgid)]

    # UPDATE: After contacting BRREG I was told that these orgids can only start with 8 or 9.
    # This is not specified in the algorithm document.
    if digits[0] not in [8, 9]:
        return False

    # Length requirement
    # "Organisasjonsnummeret består av 9 siffer"
    if len(digits) != 9:
        return False

    # "Organisasjonsnummeret består av 9 siffer hvor det siste sifferet er et
    # kontrollsiffer beregnet med standard vekter, modulus 11. Etter dette blir
    # vektene 3, 2, 7, 6, 5, 4, 3 og 2 regnet fra første siffer. Sifrene i
    # feltet multipliseres med vekttallene 2, 3, 4, 5, 6, 7, 2, 3 osv. regnet
    # fra høyre mot venstre."
    product_sum = 0
    for weight, digit in zip(WEIGHTS, digits):
        product_sum = product_sum + (weight * digit)

    # "Produktsummen divideres med 11."
    remainder = product_sum % 11

    # "Hvis kontrollsifferet blir 10 (rest = 1) må kontrollsifferet erstattes
    # med minus-tegn (-). Minus-tegn (-) er ikke lovlig kontrollsiffer for
    # organisasjonsnummer."
    if remainder == 1: # this is the most opaque part of the algorithm description
        return False   # not sure if this is correct still
    # "Hvis divisjonen går opp (rest = 0), blir kontrollsifferet 0"
    if remainder == 0:
        control = 0
        # "Resten etter divisjonen trekkes fra 11 og resultatet blir kontrollsifferet."
    else:
        control = 11 - remainder

    if control != digits[-1]: # This is the actual test
        return False

    # Counterfactual: The orgid must be correct
    return True
