from copy import copy
from dataclasses import dataclass
from enum import Enum
from typing import Any, List


@dataclass
class CharPos:
    row: int
    col: int

    def __hash__(self):
        return hash((self.row, self.col))


class Direction(Enum):
    TOP = (-1, 0)
    TOP_RIGHT = (-1, 1)
    RIGHT = (0, 1)
    BOTTOM_RIGHT = (1, 1)
    BOTTOM = (1, 0)
    BOTTOM_LEFT = (1, -1)
    LEFT = (0, -1)
    TOP_LEFT = (-1, -1)


def get_value_by_char_pos(pos: CharPos, source: List[List[Any]]):
    if pos.row < 0 or pos.col < 0:
        raise IndexError()
    return source[pos.row][pos.col]


def find_word_from_pos_in_dir(
    source: List[List[str]], target: str, start_pos: CharPos, direction: Direction
) -> List[List[CharPos]]:
    result = []
    cur_pos = copy(start_pos)

    for target_char in target:
        try:
            cur_value = get_value_by_char_pos(cur_pos, source)
        except IndexError:
            return []

        if cur_value == target_char:
            result.append(copy(cur_pos))
        else:
            return []

        cur_pos.row += direction.value[0]
        cur_pos.col += direction.value[1]

    return result


def find_word_from_pos(
    source: List[List[str]], target: str, start_pos: CharPos
) -> List[List[CharPos]]:
    result = []
    for direction in Direction:
        r = find_word_from_pos_in_dir(source, target, start_pos, direction)
        if len(r):
            result.append(r)
    return result


def find_char(source: List[List[str]], target: str) -> List[CharPos]:
    return [
        CharPos(r, c)
        for r, row in enumerate(source)
        for c, col in enumerate(row)
        if col == target
    ]


def find_word(source: List[List[str]], target: str) -> List[List[CharPos]]:
    result = []

    first_char_pos = find_char(source, target[0])
    for pos in first_char_pos:
        r = find_word_from_pos(source, target, pos)

        if len(r):
            result += r
    return result


def count_word(source: List[List[str]], target: str) -> int:
    return len(find_word(source, target))


def get_word_search(filename) -> List[List[str]]:
    with open(filename) as f:
        return [list(l.strip()) for l in f.readlines()]


def main():
    word_search = get_word_search("puzzle_input.txt")

    target_word = "XMAS"
    target_word_count = count_word(word_search, target_word)
    print(f"There are {target_word_count} '{target_word}' in word search")


if __name__ == "__main__":
    main()
