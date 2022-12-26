# ID 72545231
from typing import List


def factorize(number: int) -> List[int]:
    i = 2
    factors = list()
    while i * i <= number:
        while number % i == 0:
            factors.append(int(i))
            number = int(number / i)
        i = i + 1
    if number > 1:
        factors.append(number)
    return factors


if __name__ == '__main__':
    result = factorize(int(input()))
    print(*result)
