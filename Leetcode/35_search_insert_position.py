from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # nums 안에 target 이 몇번째 인덱스에 있는지 확인. 없으면 있다고 가정할 경우 어디에 있을지를 확인
        for i in range(0, len(nums)):
            # 찾았거나 초과.
            if target <= nums[i]:
                return i
        # 여기까지 왔으면 초과한게 전혀 없단 소리. 그럼 바로 그다음꺼임.
        return i + 1
