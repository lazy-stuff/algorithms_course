# ID 72544787
import re


def is_palindrome(line: str) -> bool:
    phrase = line.lower()
    phrase = ''.join(phrase.split(' '))
    phrase = re.sub(r'[.,"-?:!;]', '', phrase)
    if phrase[::-1] == phrase[::]:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_palindrome(input().strip()))
