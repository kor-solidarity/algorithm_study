# https://github.com/beginner-codes/challenges/blob/main/weekday/challenge_646.md

from __future__ import annotations
from beginnercodes.challenges import test


def pairs(numbers: list[int]) -> list[list[int]]:
    # 주어진 배열에서 첫 번째 숫자와 마지막 숫자를 짝짓고, 두 번째 숫자는 뒤에서 두 번째 숫자와 짝짓고, 등등
    # 이와 같은 방식으로 배열에서 모든 숫자 쌍을 짝지어 반환하는 함수를 작성
    p1, p2 = 0, len(numbers) - 1
    res = []
    while p1 <= p2:
        res.append([numbers[p1], numbers[p2]])
        p1 += 1
        p2 -= 1

    return res  # Put your code here!!!


test(646, pairs)  # Tell it which challenge to test against
