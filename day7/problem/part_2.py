from dataclasses import dataclass
from operator import add, mul
from typing import List

from problem.part_1 import Equation, get_all_operators_combs, read_eqs

operators_combs_cache = dict()


def calc_expr(a: int, b: int, operator: str):
    if operator == "+":
        return add(a, b)
    elif operator == "*":
        return mul(a, b)
    elif operator == "|":
        return int(str(a) + str(b))
    else:
        raise ValueError


def calc_eq(eq: Equation, operators: str):
    if len(eq.operands) - 1 != len(operators):
        raise ValueError

    operators = list(operators)
    result = eq.operands[0]
    for operand in eq.operands[1:]:
        result = calc_expr(result, operand, operators.pop())

    return result


def is_valid_eq(eq: Equation):
    operators_count = len(eq.operands) - 1
    combs = get_all_operators_combs(
        count=operators_count,
        operators=["+", "*", "|"],
        combs_cache=operators_combs_cache,
    )
    for c in combs:
        if calc_eq(eq, c) == eq.result:
            return True
    return False


def filter_valid_eqs(eqs: List[Equation]) -> List[Equation]:
    return list(filter(is_valid_eq, eqs))


def get_valid_eqs_sum(input_filename) -> int:
    input_eqs = read_eqs(input_filename)
    valid_eqs = filter_valid_eqs(input_eqs)
    return sum([eq.result for eq in valid_eqs])


def main():
    result = get_valid_eqs_sum("equations.txt")
    print(f"The sum of all valid equations is {result}")


if __name__ == "__main__":
    main()
