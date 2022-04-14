import math
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class ProgressBar:

    def __init__(self, max_count: int, print_info_above: str):
        self._max_count = max_count
        self._print_info_above = print_info_above
        self._old_percent = 0

    def print_progress(self, count: int):
        percent = math.floor((count / self._max_count) * 100)
        if self._old_percent != percent:
            print(f"{self._print_info_above} {percent:3}% [{'=' * (percent // 2)}{' ' * (50 - percent // 2)}]",
                  end="\r")
        self._old_percent = percent
