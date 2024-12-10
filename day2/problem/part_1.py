from enum import Enum
from typing import List


class ReportDir(Enum):
    INCR = "increasing"
    DECR = "decreasing"


def is_safe_report(report: List[int]) -> bool:
    if len(report) == 0:
        return False
    elif len(report) == 1:
        return True

    prev_dir = None
    prev_level = report[0]
    for i in range(1, len(report)):
        cur_level = report[i]
        diff = cur_level - prev_level
        if not (1 <= abs(diff) <= 3):
            return False

        cur_dir = ReportDir.INCR if diff > 0 else ReportDir.DECR
        if prev_dir is not None and prev_dir != cur_dir:
            return False

        prev_level = cur_level
        prev_dir = cur_dir
    return True


def get_safe_reports(reports: List[int]) -> List[List[int]]:
    return list(filter(is_safe_report, reports))


def get_safe_reports_count(reports: List[List[int]]) -> int:
    return len(get_safe_reports(reports))


def get_reports(filename="input.txt") -> List[List[int]]:
    with open(filename) as f:
        return [[int(n) for n in l.strip().split()] for l in f.readlines()]


def main():
    reports = get_reports()
    safe_reports_count = get_safe_reports_count(reports)
    answer = f"There are {safe_reports_count} safe reports"
    print(answer)


if __name__ == "__main__":
    main()
