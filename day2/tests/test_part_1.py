import os

from problem.part_1 import get_reports, is_safe_report


def test_get_reports_sample_input_reports():
    filename = os.path.join("tests", "input", "multi_reports_input.txt")
    reports = get_reports(filename)

    correct_reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]

    assert isinstance(reports, list)
    assert len(reports) == len(correct_reports)
    for i in range(len(reports)):
        assert reports[i] == correct_reports[i]


def test_get_reports_one_report():
    filename = os.path.join("tests", "input", "one_report_input.txt")
    reports = get_reports(filename)

    correct_reports = [[1, 3, 2, 4, 5]]

    assert isinstance(reports, list)
    assert len(reports) == len(correct_reports)
    for i in range(len(reports)):
        assert reports[i] == correct_reports[i]


def test_get_reports_one_level():
    filename = os.path.join("tests", "input", "one_level_input.txt")
    reports = get_reports(filename)

    correct_reports = [[6], [2], [4], [5], [8]]

    assert isinstance(reports, list)
    assert len(reports) == len(correct_reports)
    for i in range(len(reports)):
        assert reports[i] == correct_reports[i]


def test_get_reports_empty():
    filename = os.path.join("tests", "input", "empty_input.txt")
    reports = get_reports(filename)
    assert isinstance(reports, list)
    assert len(reports) == 0


def test_get_reports_trailing_spaces():
    filename = os.path.join("tests", "input", "trailing_spaces_input.txt")
    reports = get_reports(filename)

    correct_reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]

    assert isinstance(reports, list)
    assert len(reports) == len(correct_reports)
    for i in range(len(reports)):
        assert reports[i] == correct_reports[i]


def test_is_safe_report_sample_reports_input():
    assert is_safe_report([7, 6, 4, 2, 1]) == True
    assert is_safe_report([1, 2, 7, 8, 9]) == False
    assert is_safe_report([9, 7, 6, 2, 1]) == False
    assert is_safe_report([1, 3, 2, 4, 5]) == False
    assert is_safe_report([8, 6, 4, 4, 1]) == False
    assert is_safe_report([1, 3, 6, 7, 9]) == True


def test_is_safe_report_all_increasing_and_correct_diff():
    assert is_safe_report([10, 11, 12, 13, 14, 15]) == True


def test_is_safe_report_all_decreasing_and_correct_diff():
    assert is_safe_report([15, 14, 13, 12, 11, 10]) == True


def test_is_safe_report_all_increasing_but_diff_greater_3():
    assert is_safe_report([10, 11, 12, 16, 17, 20]) == False


def test_is_safe_report_all_increasing_but_diff_smaller_1():
    assert is_safe_report([10, 11, 12, 13, 14, 14]) == False


def test_is_safe_report_all_decreasing_but_diff_greater_3():
    assert is_safe_report([15, 14, 13, 12, 11, 7]) == False


def test_is_safe_report_all_decreasing_but_diff_smaller_1():
    assert is_safe_report([15, 15, 13, 12, 11, 10]) == False


def test_is_safe_report_mix_decreasing_and_increasing():
    assert is_safe_report([15, 14, 13, 14, 15, 14]) == False


def test_is_safe_report_second_level_error():
    assert is_safe_report([15, 20, 13, 14, 15, 14]) == False


def test_is_safe_report_last_level_error():
    assert is_safe_report([15, 16, 17, 19, 21, 8]) == False


def test_is_safe_report_one_level_report():
    assert is_safe_report([5]) == True


def test_is_safe_report_empty_report():
    assert is_safe_report([]) == False
