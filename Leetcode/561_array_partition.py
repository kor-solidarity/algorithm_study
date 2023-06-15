# https://leetcode.com/problems/array-partition/
# Runtime: 283 ms
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 2n 개의 숫자 리스트를 두개씩 묶은 후 그 짝들의 min() 값들이 나올 수 있는 합의 최대값을 구하기

        # 간단요약: 전부 정렬한 후 하나씩 건너뛴 값들만 더하면 그것이 최대값.
        return sum(sorted(nums)[::2])