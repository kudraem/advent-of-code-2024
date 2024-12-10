import os

import pytest
from problem.part_1 import (
    Equation,
    calc_eq,
    calc_expr,
    get_all_operators_combs,
    get_valid_eqs_sum,
    parse_eq_str,
)


def test_get_valid_eqs_sum_sample_input():
    filename = os.path.join("tests", "input", "sample_input.txt")
    assert get_valid_eqs_sum(filename) == 3749


def test_parse_eq_str_valid_input():
    s = "1000: 89 3 19"
    eq = parse_eq_str(s)
    assert eq.result == 1000
    assert eq.operands == [89, 3, 19]


def test_parse_eq_str_valid_input_one_operand():
    s = "1000: 10"
    eq = parse_eq_str(s)
    assert eq.result == 1000
    assert eq.operands == [10]


def test_parse_eq_str_invalid_input_invalid_sep():
    s = "1000=89 3 19"
    with pytest.raises(ValueError):
        parse_eq_str(s)


def test_parse_eq_str_invalid_input_invalid_empty_result():
    s = ": 89 3 19"
    with pytest.raises(ValueError):
        parse_eq_str(s)


def test_parse_eq_str_invalid_input_invalid_empty_operands():
    s = "1000:"
    with pytest.raises(ValueError):
        parse_eq_str(s)


def test_get_all_operators_combs_count_1():
    cache = {}
    combs = get_all_operators_combs(count=1, operators=["*", "+"], combs_cache=cache)
    assert sorted(combs) == sorted(["*", "+"])


def test_get_all_operators_combs_count_2():
    cache = {}
    combs = get_all_operators_combs(count=2, operators=["*", "+"], combs_cache=cache)
    assert sorted(combs) == sorted(["**", "*+", "+*", "++"])


def test_get_all_operators_combs_count_3():
    cache = {}
    combs = get_all_operators_combs(count=3, operators=["*", "+"], combs_cache=cache)
    assert sorted(combs) == sorted(
        ["***", "*+*", "+**", "++*", "**+", "*++", "+*+", "+++"]
    )


def test_get_all_operators_combs_single_operator():
    cache = {}
    combs = get_all_operators_combs(count=2, operators=["*"], combs_cache=cache)
    assert sorted(combs) == sorted(["**"])


def test_get_all_operators_combs_count_0():
    cache = {}
    with pytest.raises(ValueError):
        get_all_operators_combs(count=0, operators=["*", "+"], combs_cache=cache)


def test_get_all_operators_combs_empty_operators():
    cache = {}

    assert len(get_all_operators_combs(count=2, operators=[], combs_cache=cache)) == 0


def test_get_all_operators_combs_get_from_cache():
    cache = {1: ["*", "+"], 1000: ["+++", "***"]}
    combs = get_all_operators_combs(count=1000, operators=["*", "+"], combs_cache=cache)
    assert sorted(combs) == sorted(["+++", "***"])


def test_calc_expr_add():
    assert calc_expr(2, 8, "+") == 10


def test_calc_expr_mul():
    assert calc_expr(2, 8, "*") == 16


def test_calc_expr_invalid_operator():
    with pytest.raises(ValueError):
        calc_expr(2, 2, "/")


def test_calc_eq():
    assert calc_eq(Equation(result=25, operands=[5, 5]), "*") == 25


def test_calc_eq_single_operand():
    assert calc_eq(Equation(result=25, operands=[5]), "") == 5


def test_calc_eq_operators_operands_count_mismatch():
    with pytest.raises(ValueError):
        calc_eq(Equation(result=25, operands=[5]), "+")
        calc_eq(Equation(result=25, operands=[]), "")
        calc_eq(Equation(result=25, operands=[]), "+")
