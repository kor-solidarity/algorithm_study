# https://leetcode.com/problems/product-of-array-except-self/
# Runtime: 242 ms
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 각 리스트 요소 list[i]가 나머지 요소들의 곱의 결과가 나오게끔 반환
        n = len(nums)
        left = [1] * n
        right = [1] * n
        # 리스트 인덱스 왼쪽의 모든 값들의 곱을 넣는다.
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        # 인덱스 오른쪽의 모든 값들의 곱을 넣는다.
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        # 양 리스트 나란히 곱한다.
        for i in range(n):
            left[i] = left[i] * right[i]

        return left
