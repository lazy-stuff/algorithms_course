# ID 72544651
from typing import List, Tuple


def get_weather_randomness(temperatures: List[int]) -> int:
    randomness_count = 0
    for i in range(0, len(temperatures)):
        if len(temperatures) == 1:
            randomness_count += 1
        else:
            if i == 0:
                if temperatures[i] > temperatures[i+1]:
                    randomness_count += 1
            elif i == int(len(temperatures)-1):
                if temperatures[i] > temperatures[i-1]:
                    randomness_count += 1
            else:
                if (temperatures[i] > temperatures[i-1]
                   and temperatures[i] > temperatures[i+1]):
                    randomness_count += 1
    return randomness_count


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures, n


if __name__ == '__main__':
    temperatures, n = read_input()
    print(get_weather_randomness(temperatures))
