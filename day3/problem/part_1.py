import re
from dataclasses import dataclass, field
from typing import List


@dataclass
class Mul:
    op1: int
    op2: int
    res: int = field(init=False)

    def __post_init__(self):
        self.res = self.op1 * self.op2

    def __hash__(self):
        return hash((self.op1, self.op2))


def get_all_valid_mul(s: str) -> List[Mul]:
    r = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    return [Mul(op1=int(op[0]), op2=int(op[1])) for op in r.findall(s)]


def get_muls_result_sum(muls: List[Mul]) -> int:
    return sum(mul.res for mul in muls)


def get_memory_dump(filename="memory_dump.txt") -> str:
    with open(filename) as f:
        return f.read()


def main():
    memory_dump = get_memory_dump()
    muls = get_all_valid_mul(memory_dump)
    muls_result_sum = get_muls_result_sum(muls)
    print(f"All valid mul result sum is {muls_result_sum}")


if __name__ == "__main__":
    main()
