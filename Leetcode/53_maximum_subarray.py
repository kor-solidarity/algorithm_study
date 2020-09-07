# Runtime: 64 ms, faster than 90.78% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.6 MB, less than 64.25% of Python3 online submissions for Maximum Subarray.
from typing import List


class Solution:
    # 최소 1개 숫자가 들어있는 어레이에서 섭어레이 값의 합 중에 나올 수 있는 최대값을 구하기.
    # 섭어레이란 인접어레이, contiguous array 로서
    # from [1, 2, 3, 4], The subarrays are (1), (2), (3), (4), (1,2), (2,3), (3,4), (1,2,3), (2,3,4) and (1,2,3,4)
    # 예: [-2,1,-3,4,-1,2,1,-5,4], 여기서 나올 수 있는 최대값은 [4,-1,2,1] 로 6임
    def maxSubArray(self, nums: List[int]) -> int:
        # 만일 하나짜리면 돌릴필요 없음
        if len(nums) == 1:
            return nums[0]
        # 원칙:
        # 1. 처음과 마지막 값이 마이너스가 아니어야 한다.
        # 2. 마이너스값이 나왔을 때 그 다음 값들이 또 마이너스가 나오기 전에 앞에 마이너스값들을 상쇄시킬 수 있는가.
        # 최종 결과값
        result = 0
        # 현재값
        cur_val = 0
        for i in range(len(nums)):
            cur_val += nums[i]
            # 인덱스 값을 넣은 결과가 마이너스면 거기까지는 다 걸러야 한다는 소리.
            # 0으로 초기화하고 이전인덱스 다 통과한다 친다.
            if cur_val < 0:
                cur_val = 0
                continue
            # 그리고 쭉 더하면서 가장 높은 값이 나오면 그걸로 교체하는 식으로 넘어간다.
            # 뒤를 계속 잇는게 값이 더 안나가면 결국 안쓰게 되는거.
            if result < cur_val:
                result = cur_val
        # 만일 0이 나온 경우 == 0 외에 연결된게 없던가 마이너스 뿐이거나.
        # 어레이 값들 중에 가장 높은 값으로 정한다.
        if result == 0:
            result = max(nums)
        return result
