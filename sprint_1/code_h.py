# ID 72544975
from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    first_number = [*map(int, first_number)]
    second_number = [*map(int, second_number)]
    first_number = first_number[::-1]
    second_number = second_number[::-1]
    size = max(len(first_number), len(second_number))
    first_number += [0] * (size - len(first_number))
    second_number += [0] * (size - len(second_number))
    overflow = 0
    result = []
    for obj in zip(first_number, second_number):
        value = obj[0] + obj[1] + overflow
        overflow = value // 2
        result.append(value % 2)
    if overflow == 1:
        result.append(1)
    result = result[::-1]
    return ''.join(map(str, result))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


if __name__ == '__main__':
    first_number, second_number = read_input()
    print(get_sum(first_number, second_number))
