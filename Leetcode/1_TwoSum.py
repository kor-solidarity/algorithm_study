# https://leetcode.com/problems/two-sum
# Runtime: 3660 ms, faster than 17.10% of Python3 online submissions for Count and Say.
# Memory Usage: 14.8 MB, less than 92.97% of Python3 online submissions for Count and Say.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start_num = 0
        total = len(nums)
        for i in range(start_num, total):
            answer = []
            lost_pair = target - nums[i]
            for j in range(i + 1, total):
                if nums[j] == lost_pair:
                    answer = [i, j]
                    break
            if answer:
                break
        return answer
