# ID 72500107
from typing import Tuple


def read_input() -> Tuple[str, int]:
    n = int(input())
    game_str = ''.join([input() for i in range(4)])
    return game_str, n


def get_score(game_str: str, n: int) -> int:
    n = n * 2
    count = 0
    game_dict = dict()
    for value in game_str:
        if value != '.':
            game_dict[value] = game_dict.get(value, 0) + 1

    for key in game_dict:
        if game_dict[key] <= n:
            count += 1
    return count


if __name__ == '__main__':
    game_str, n = read_input()
    print(get_score(game_str, n))
