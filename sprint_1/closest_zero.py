# ID 72542631
from typing import List, Tuple


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    street_map = list(map(int, input().strip().split()))
    return street_map, n


def get_map(street_map: List[int]) -> List[int]:
    empty_spots = list()
    count = 0
    for i, val in enumerate(street_map):
        if val == 0:
            count = 0
            empty_spots.append(i)
        else:
            count += 1
            street_map[i] = count

    for i in range(len(street_map) - 1, -1, -1):
        if street_map[i] == 0:
            empty_spot_index = i
        if street_map[i] != 0:
            if i < empty_spots[0]:
                street_map[i] = empty_spots[0] - i
            if i > empty_spots[0] and i < empty_spots[-1]:
                distance_count = empty_spot_index - i
                if street_map[i] > distance_count:
                    street_map[i] = distance_count
    return street_map


if __name__ == '__main__':
    street_map, n = read_input()
    result = get_map(street_map)
    print(*result)
