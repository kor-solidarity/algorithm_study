# https://github.com/beginner-codes/challenges/blob/main/weekday/challenge_643.md
from __future__ import annotations
from beginnercodes.challenges import test
import time


def hours_passed(start: str, end: str) -> str:
    # 몇시간 지났는지 쓰기
    t1 = time.strptime(start, '%I:%M %p')
    t2 = time.strptime(end, '%I:%M %p')

    hours = t2[3] - t1[3]
    if hours == 0:
        return 'no time passed'
    return str(hours) + " hours"  # Put your code here!!!


test(643, hours_passed)  # Tell it which challenge to test against
