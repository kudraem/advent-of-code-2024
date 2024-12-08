from problem.part_1 import Mul, get_all_valid_mul, get_muls_result_sum


def test_get_all_valid_mul_samples():
    s = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    res = get_all_valid_mul(s)
    correct_muls = [Mul(2, 4), Mul(5, 5), Mul(11, 8), Mul(8, 5)]
    assert set(res) == set(correct_muls)


def test_get_all_valid_mul_empty_input():
    s = ""
    res = get_all_valid_mul(s)
    assert len(res) == 0


def test_get_all_valid_mul_none_valid_mul():
    s = "%&mul[3,7]!@F^do_not_MU?23as?^$#m[_]1"
    res = get_all_valid_mul(s)
    assert len(res) == 0


def test_get_all_valid_mul_one_valid_mul():
    s = "%&mul[3,7]!@F^do_mul(10,20)not_MU?23as?^$#m[_]1"
    res = get_all_valid_mul(s)
    correct_muls = [Mul(10, 20)]
    assert set(res) == set(correct_muls)


def test_get_all_valid_mul_valid_mul_on_the_edges():
    s = "mul(50,8)%&mul[3,7]!@^do_not_+mul(32!,64]the(mul(1,23)"
    res = get_all_valid_mul(s)
    correct_muls = [Mul(50, 8), Mul(1, 23)]
    assert set(res) == set(correct_muls)


def test_get_all_valid_mul_glued_valid_muls():
    s = "testmul(11,8)mul(8,5)!"
    res = get_all_valid_mul(s)
    correct_muls = [Mul(11, 8), Mul(8, 5)]
    assert set(res) == set(correct_muls)


def test_get_all_valid_mul_invalid_separator():
    s = "$addmul(11|8)foo"
    res = get_all_valid_mul(s)
    assert len(res) == 0


def test_get_all_valid_mul_extra_spaces():
    s = "mul(8,8 )mul(50, 8)%&mul (3,7)]!@^do_notmul(3, 7)_+mul(32!,64]the(mul( 1,23)"
    res = get_all_valid_mul(s)
    assert len(res) == 0


def test_get_all_valid_mul_invalid_operand_type():
    s = "$addmul(eleven,10)foo"
    res = get_all_valid_mul(s)
    assert len(res) == 0

    s = "$addmul(23,ten)foo"
    res = get_all_valid_mul(s)
    assert len(res) == 0

    s = "$addmul(eleven,!)foo"
    res = get_all_valid_mul(s)
    assert len(res) == 0


def test_get_all_valid_mul_invalid_digits_count():
    s = "$addmul(1000,10)foo"
    res = get_all_valid_mul(s)
    assert len(res) == 0

    s = "$addmul(10,1000)foo"
    res = get_all_valid_mul(s)
    assert len(res) == 0

    s = "$addmul(1000,1000)foo"
    res = get_all_valid_mul(s)
    assert len(res) == 0


def test_get_all_valid_mul_upper_case():
    s = "%&mul[3,7]!@F^do_MUL(10, 20)not_MU?23as?^$#m[_]1"
    res = get_all_valid_mul(s)
    assert len(res) == 0


def test_get_all_valid_mul_brackets_and_braces():
    s = "xmul[2,4)%&mul[3,7]!@^do_not_mul{5,5}+mul(32,64]then(mul(11,8}mul(8,5])"
    res = get_all_valid_mul(s)
    assert len(res) == 0


def test_get_muls_result_sum_sample():
    muls = [Mul(2, 4), Mul(5, 5), Mul(11, 8), Mul(8, 5)]
    assert get_muls_result_sum(muls) == 161


def test_get_muls_result_sum_empty_mul_list():
    muls = []
    assert get_muls_result_sum(muls) == 0


def test_get_muls_result_sum_single_mul():
    muls = [Mul(2, 4)]
    assert get_muls_result_sum(muls) == 8
