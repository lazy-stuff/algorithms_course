# ID 72545840
from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    shorter = list(shorter)
    longer = list(longer)
    shorter_dict = dict()
    result = ''
    for value in shorter:
        if value not in shorter_dict:
            shorter_dict[value] = 0
        shorter_dict[value] += 1
    longer_dict = dict()
    for value in longer:
        if value not in longer_dict:
            longer_dict[value] = 0
        longer_dict[value] += 1
    for letter in longer_dict:
        if letter in shorter_dict:
            if shorter_dict[letter] < longer_dict[letter]:
                result = letter
        else:
            result = letter
    return result


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


if __name__ == '__main__':
    shorter, longer = read_input()
    print(get_excessive_letter(shorter, longer))
