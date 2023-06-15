# https://github.com/beginner-codes/challenges/blob/main/weekday/challenge_644.md

from __future__ import annotations
from beginnercodes.challenges import test


def prime_divisors(number: int) -> list[int]:
    # 매개 변수로 받은 수의 모든 약수를 구하고 이 중 소수를 반환
    p = 2
    res1 = []
    while number > 1 and number >= p:
        if number % p:
            p += 1
        else:
            res1.append(p)
            number = number / p
            p += 1
    res2 = []
    for i in res1:
        if is_prime(i):
            res2.append(i)
    return res2  # Put your code here!!!


def is_prime(num: int) -> bool:
    if num <= 0:
        return False
    for i in range(2, (num // 2) + 1):
        if not num % i:
            return False
    return True


test(644, prime_divisors)  # Tell it which challenge to test against
