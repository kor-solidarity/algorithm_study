# https://github.com/beginnerpy-com/challenges/blob/main/weekday/challenge_645.md

from __future__ import annotations
from beginnercodes.challenges import test


def difference_two(numbers: list[int]) -> list[list[int]]:
    # 정수 배열을 입력으로 받아 차이가 2인 모든 정수 쌍을 반환하는 함수를 작성하세요.
    # 결과 배열은 값의 오름차순으로 정렬되어야 합니다.
    numbers.sort()
    res = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[j] - numbers[i] == 2:
                res.append([numbers[i], numbers[j]])
    return res  # Put your code here!!!


test(645, difference_two)  # Tell it which challenge to test against
