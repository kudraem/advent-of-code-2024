from dataclasses import dataclass
from operator import add, mul
from typing import Dict, List


@dataclass
class Equation:
    operands: List[int]
    result: int


operators_combs_cache = dict()


def calc_expr(a: int, b: int, operator: str):
    if operator == "+":
        return add(a, b)
    elif operator == "*":
        return mul(a, b)
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


def get_all_operators_combs(
    count: int, operators: List[str], combs_cache: Dict[str, List[str]] = {}
) -> List[List[str]]:
    if count <= 0:
        raise ValueError

    if count in combs_cache:
        return combs_cache[count]

    combs = [op for op in operators]
    for _ in range(1, count):
        combs = [c + op for c in combs for op in operators]
    combs_cache[count] = combs
    return combs


def is_valid_eq(eq: Equation):
    operators_count = len(eq.operands) - 1
    combs = get_all_operators_combs(
        count=operators_count, operators=["+", "*"], combs_cache=operators_combs_cache
    )
    for c in combs:
        if calc_eq(eq, c) == eq.result:
            return True
    return False


def filter_valid_eqs(eqs: List[Equation]) -> List[Equation]:
    return list(filter(is_valid_eq, eqs))


def parse_eq_str(s: str) -> Equation:
    res_str, ops_str = s.strip().split(":")
    if len(ops_str) == 0:
        raise ValueError

    return Equation(
        operands=[int(i) for i in ops_str.strip().split()], result=int(res_str)
    )


def read_eqs(filename) -> List[Equation]:
    with open(filename) as f:
        return [parse_eq_str(l) for l in f.readlines()]


def get_valid_eqs_sum(input_filename) -> int:
    input_eqs = read_eqs(input_filename)
    valid_eqs = filter_valid_eqs(input_eqs)
    return sum([eq.result for eq in valid_eqs])


def main():
    result = get_valid_eqs_sum("equations.txt")
    print(f"The sum of all valid equations is {result}")


if __name__ == "__main__":
    main()
