# https://leetcode.com/problems/two-sum
# Runtime: 860 ms, faster than 33.48% of Python3 online submissions for Two Sum.
# Memory Usage: 14.8 MB, less than 95.11% of Python3 online submissions for Two Sum.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 두 값의 합이 target 값이 나오는 인덱스 값을 반환
        for i, n in enumerate(nums):
            complement = target - n
            # 남은 리스트에서 나머지 값이 있는지 확인 후 그 값의 인덱스를 반환
            if complement in nums[i + 1:]:
                # 뒤에 i+1 하는 이유: 리스트를 nums[i + 1] 로 가져왔으니 인덱스 수가 i+1만큼 밀림...
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

