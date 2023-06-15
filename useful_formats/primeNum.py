def is_prime(num: int) -> bool:
    if num <= 0:
        return False
    for i in range(2, (num // 2) + 1):
        if not num % i:
            return False
    return True
