import pytest
from problem.part_1 import (
    CharPos,
    Direction,
    count_word,
    find_char,
    find_word_from_pos_in_dir,
    get_value_by_char_pos,
)


def test_find_char_single_occurrence():
    source = [["a", "b"], ["c", "d"]]
    target = "a"
    expected = [CharPos(0, 0)]
    assert set(find_char(source, target)) == set(expected)


def test_find_char_multiple_occurrences_different_rows():
    source = [["a", "b"], ["a", "d"]]
    target = "a"
    expected = [CharPos(0, 0), CharPos(1, 0)]
    assert set(find_char(source, target)) == set(expected)


def test_find_char_multiple_occurrences_same_row():
    source = [["a", "a"], ["c", "d"]]
    target = "a"
    expected = [CharPos(0, 0), CharPos(0, 1)]
    assert set(find_char(source, target)) == set(expected)


def test_find_char_multiple_rows_and_columns():
    source = [["a", "b"], ["b", "a"]]
    target = "b"
    expected = [CharPos(0, 1), CharPos(1, 0)]
    assert set(find_char(source, target)) == set(expected)


def test_find_char_target_not_found():
    source = [["a", "b"], ["c", "d"]]
    target = "x"
    expected = []
    assert set(find_char(source, target)) == set(expected)


def test_find_char_empty_source():
    source = []
    target = "a"
    expected = []
    assert set(find_char(source, target)) == set(expected)


def test_find_char_empty_rows():
    source = [[], []]
    target = "a"
    expected = []
    assert set(find_char(source, target)) == set(expected)


def test_find_char_varying_row_lengths():
    source = [["a", "b", "c"], ["d", "a"]]
    target = "a"
    expected = [CharPos(0, 0), CharPos(1, 1)]
    assert set(find_char(source, target)) == set(expected)


def test_find_char_special_characters():
    source = [["!", "@"], ["#", "!"]]
    target = "!"
    expected = [CharPos(0, 0), CharPos(1, 1)]
    assert set(find_char(source, target)) == set(expected)


def test_find_char_on_the_edges():
    source = [["a", "b", "b", "a"]]
    target = "a"
    expected = [CharPos(0, 3), CharPos(0, 0)]
    assert set(find_char(source, target)) == set(expected)


@pytest.fixture
def get_value_by_char_source():
    return [
        ["a", "b"],
        ["c", "d"],
    ]


def test_get_value_by_char_pos_valid(get_value_by_char_source):
    pos = CharPos(1, 1)
    assert get_value_by_char_pos(pos, get_value_by_char_source) == "d"


def test_get_value_by_char_pos_row_out_of_bounds(get_value_by_char_source):
    pos = CharPos(2, 0)
    with pytest.raises(IndexError):
        get_value_by_char_pos(pos, get_value_by_char_source)


def test_get_value_by_char_pos_col_out_of_bounds(get_value_by_char_source):
    pos = CharPos(0, 2)
    with pytest.raises(IndexError):
        get_value_by_char_pos(pos, get_value_by_char_source)


def test_get_value_by_char_pos_negative_row_index(get_value_by_char_source):
    pos = CharPos(-1, 0)
    with pytest.raises(IndexError):
        get_value_by_char_pos(pos, get_value_by_char_source)


def test_get_value_by_char_pos_negative_col_index(get_value_by_char_source):
    pos = CharPos(0, -1)
    with pytest.raises(IndexError):
        get_value_by_char_pos(pos, get_value_by_char_source)


@pytest.fixture
def find_word_from_pos_in_dir_source():
    return [
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
    ]


def test_find_word_from_pos_in_dir_valid_right(find_word_from_pos_in_dir_source):
    target = "abc"
    start_pos = CharPos(0, 0)
    direction = Direction.RIGHT
    expected = [CharPos(0, 0), CharPos(0, 1), CharPos(0, 2)]

    assert set(
        find_word_from_pos_in_dir(
            find_word_from_pos_in_dir_source, target, start_pos, direction
        )
    ) == set(expected)


def test_find_word_from_pos_in_dir_valid_bottom(find_word_from_pos_in_dir_source):
    target = "adg"
    start_pos = CharPos(0, 0)
    direction = Direction.BOTTOM
    expected = [CharPos(0, 0), CharPos(1, 0), CharPos(2, 0)]
    assert set(
        find_word_from_pos_in_dir(
            find_word_from_pos_in_dir_source, target, start_pos, direction
        )
    ) == set(expected)


def test_find_word_from_pos_in_dir_invalid_character(find_word_from_pos_in_dir_source):
    target = "abx"
    start_pos = CharPos(0, 0)
    direction = Direction.RIGHT
    assert (
        len(
            find_word_from_pos_in_dir(
                find_word_from_pos_in_dir_source, target, start_pos, direction
            )
        )
        == 0
    )


def test_find_word_from_pos_in_dir_out_of_bounds(find_word_from_pos_in_dir_source):
    target = "abcdef"
    start_pos = CharPos(0, 0)
    direction = Direction.BOTTOM_RIGHT
    assert (
        len(
            find_word_from_pos_in_dir(
                find_word_from_pos_in_dir_source, target, start_pos, direction
            )
        )
        == 0
    )


def test_find_word_from_pos_in_dir_empty_target(find_word_from_pos_in_dir_source):
    target = ""
    start_pos = CharPos(0, 0)
    direction = Direction.RIGHT
    assert (
        len(
            find_word_from_pos_in_dir(
                find_word_from_pos_in_dir_source, target, start_pos, direction
            )
        )
        == 0
    )


def test_find_word_from_pos_in_dir_empty_source():
    source = []
    target = "abc"
    start_pos = CharPos(0, 0)
    direction = Direction.RIGHT
    assert len(find_word_from_pos_in_dir(source, target, start_pos, direction)) == 0


def test_find_count_word():
    source = [
        list("MMMSXXMASM"),
        list("MSAMXMSMSA"),
        list("AMXSXMAAMM"),
        list("MSAMASMSMX"),
        list("XMASAMXAMM"),
        list("XXAMMXXAMA"),
        list("SMSMSASXSS"),
        list("SAXAMASAAA"),
        list("MAMMMXMMMM"),
        list("MXMXAXMASX"),
    ]
    target = "XMAS"
    assert count_word(source, target) == 18
