# test_chemistry_2.py
# Automated test script for the chemistry molar mass calculator.
# Ensures correctness of key functions using pytest.

import pytest
from chemistry import make_periodic_table, compute_molar_mass
from formula import parse_formula

def test_make_periodic_table():
    table = make_periodic_table()
    assert isinstance(table, dict)
    assert "H" in table
    assert table["H"][0] == "Hydrogen"
    assert pytest.approx(table["O"][1], 0.001) == 15.9994

def test_parse_formula():
    parsed = parse_formula("C6H6")
    assert parsed == [["C", 6], ["H", 6]]

def test_compute_molar_mass():
    table = make_periodic_table()
    parsed = parse_formula("C6H6")
    molar_mass = compute_molar_mass(parsed, table)
    assert pytest.approx(molar_mass, 0.001) == 78.11184
