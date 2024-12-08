from problem.part_2 import slice_str_on_enable_parts


def test_slice_str_on_enable_parts_empty_input():
    result = slice_str_on_enable_parts("")
    assert result == []


def test_slice_str_on_enable_parts_none_dont():
    s = "xmul(2,4)&mul[3,7]!_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    result = slice_str_on_enable_parts(s)

    correct_parts = [
        "xmul(2,4)&mul[3,7]!_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    ]
    assert result == correct_parts


def test_slice_str_on_enable_parts_single_dont():
    s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    result = slice_str_on_enable_parts(s)

    correct_parts = ["xmul(2,4)&mul[3,7]!^", "do()?mul(8,5))"]
    assert result == correct_parts


def test_slice_str_on_enable_parts_dont_at_start():
    s = "don't()xmul(2,4)do()&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    result = slice_str_on_enable_parts(s)
    correct_parts = ["do()&mul[3,7]!^", "do()?mul(8,5))"]
    assert result == correct_parts


def test_slice_str_on_enable_parts_dont_at_end():
    s = "mul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))don't()"
    result = slice_str_on_enable_parts(s)
    correct_parts = ["mul(2,4)&mul[3,7]!^", "do()?mul(8,5))"]
    assert result == correct_parts


def test_slice_str_on_enable_parts_glued_dont():
    s = "xmul(2,4)&mul[3,7]!^don't()don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    result = slice_str_on_enable_parts(s)

    correct_parts = ["xmul(2,4)&mul[3,7]!^", "do()?mul(8,5))"]
    assert result == correct_parts


def test_slice_str_on_enable_parts_none_do():
    s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)un?mul(8,5))"
    result = slice_str_on_enable_parts(s)

    correct_parts = ["xmul(2,4)&mul[3,7]!^"]
    assert result == correct_parts


def test_slice_str_on_enable_parts_single_do():
    s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)do()+mul(32,64](mul(11,8)un?mul(8,5))"
    result = slice_str_on_enable_parts(s)

    correct_parts = ["xmul(2,4)&mul[3,7]!^", "do()+mul(32,64](mul(11,8)un?mul(8,5))"]
    assert result == correct_parts


def test_slice_str_on_enable_parts_do_right_after_dont():
    s = "xmul(2,4)&mul[3,7]!^don't()do()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    result = slice_str_on_enable_parts(s)

    correct_parts = [
        "xmul(2,4)&mul[3,7]!^",
        "do()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
    ]
    assert result == correct_parts


def test_slice_str_on_enable_parts_do_at_end():
    s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))do()"
    result = slice_str_on_enable_parts(s)

    correct_parts = ["xmul(2,4)&mul[3,7]!^", "do()?mul(8,5))do()"]
    assert result == correct_parts


def test_slice_str_on_enable_parts_do_glued():
    s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()do()?mul(8,5))"
    result = slice_str_on_enable_parts(s)

    correct_parts = ["xmul(2,4)&mul[3,7]!^", "do()do()?mul(8,5))"]
    assert result == correct_parts


def test_slice_str_on_enable_parts_none_do_and_dont():
    s = "xmul(2,4)&mul[3,7]!_mul(5,5)+mul(32,64](mul(11,8)un?mul(8,5))"
    result = slice_str_on_enable_parts(s)

    correct_parts = ["xmul(2,4)&mul[3,7]!_mul(5,5)+mul(32,64](mul(11,8)un?mul(8,5))"]
    assert result == correct_parts
