# https://leetcode.com/problems/power-of-two/
# Runtime: 0 ms, Beats 100.00% 🤔
# Memory Usage: 12.30 MB, Beats 98.81%


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        숫자 n이 2의 거듭제곱인지 확인하는 함수. 맞으면 참, 아니면 거짓 반환.

        :type n: int
        :rtype: bool
        """
        # 0 보다 작거나 같으면 무조건 거짓
        if n <= 0:
            return False

        while n > 1:
            # 2로 나누어 떨어지지 않으면 거짓
            if n % 2 != 0:
                return False
            n //= 2

        return True
