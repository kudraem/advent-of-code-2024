import os

import pytest
from problem.part_2 import calc_expr, get_valid_eqs_sum


def test_get_valid_eqs_sum_sample_input():
    filename = os.path.join("tests", "input", "sample_input.txt")
    assert get_valid_eqs_sum(filename) == 11387


def test_calc_expr_add():
    assert calc_expr(2, 8, "+") == 10


def test_calc_expr_mul():
    assert calc_expr(2, 8, "*") == 16


def test_calc_expr_concat():
    assert calc_expr(2, 8, "|") == 28


def test_calc_expr_invalid_operator():
    with pytest.raises(ValueError):
        calc_expr(2, 2, "/")
