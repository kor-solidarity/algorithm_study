from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        current_num = None
        for i in nums:
            if i != current_num:
                nums[length] = i
                length += 1
                current_num = i
        return length

Solution().removeDuplicates([1,1,2])
