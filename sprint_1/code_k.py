# ID 72545569
from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    number = ''
    for i in number_list:
        number += str(i)
    return str(int(number) + k)


def read_input() -> Tuple[List[int], int, int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k, n


if __name__ == '__main__':
    number_list, k, n = read_input()
    result = get_sum(number_list, k)
    print(*result)
