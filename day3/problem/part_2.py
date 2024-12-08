from typing import List

from problem.part_1 import get_all_valid_mul, get_memory_dump, get_muls_result_sum


def slice_str_on_enable_parts(s: str) -> List[str]:
    result = []
    parts = s.split("don't()")
    # Because all chars before "don't" enabled
    result.append(parts[0])

    for part in parts[1:]:
        first_do_index = part.find("do()")
        if first_do_index != -1:
            result.append(part[first_do_index:])
    return [p for p in result if p]


def main():
    memory_dump = get_memory_dump()
    muls = []
    for part in slice_str_on_enable_parts(memory_dump):
        muls += get_all_valid_mul(part)
    muls_result_sum = get_muls_result_sum(muls)
    print(f"All valid mul result sum is {muls_result_sum}")


if __name__ == "__main__":
    main()
