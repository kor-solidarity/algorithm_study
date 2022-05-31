# https://leetcode.com/problems/climbing-stairs/
# Runtime: 32 ms, faster than 59.37% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 14.3 MB, less than 11.00% of Python3 online submissions for Climbing Stairs.

class Solution:
    def climbStairs(self, n: int) -> int:
        # n 값만큼의 숫자(계단 수)가 제공되는데,
        #  한계단 또는 두계단으로 올라간다고 할 때 올라갈 수 있는 조합의 수를 구하기.
        # 예: 3 인 경우
        # 1 + 1 + 1, 1 + 2, 2 + 1 이렇게 세가지 방법이 있다. 고로 답은 3

        # 마지막 두 계단에서 경우의 수.
        n1, n2 = 1, 1

        # 역순으로 더해간다.
        for i in range(n - 1):
            temp1 = n1
            n1 = n1 + n2
            n2 = temp1

        return n1
