# https://leetcode.com/problems/3sum/
# Runtime: 1466 ms, Beats 53.94%
# Memory : 18.3 MB, Beats 57.99%
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 제공된 숫자가 있는 목록에서 값 셋을 골라서 0이 될 수 있는 조합의 목록을 반환하기. 투 포인터 사용

        # 우선 크기별로 정렬한다
        nums.sort()
        # 첫번째 수가 0보다 크면 어차피 합이 0이 나올 가능성 0이니 끝.
        if nums[0] > 0:
            return []

        n = len(nums)
        result = []
        # n-2를 하는 이유: 안에서 포인터를 두개 더 돌릴텐데 그 때 뒤에 두 수를 더 쓸테니 첫 포문에서 굳이 더 빼올 필요가 없음.
        for i in range(n - 2):
            # 첫 숫자가 중복이 안되게끔 통과
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 확인할 인덱스 포인터. 하나는 왼쪽, 하나는 오른쪽
            l, r = i + 1, n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    out = [nums[i], nums[l], nums[r]]
                    # 다음으로 넘어갈 숫자가 혹시 중복되는지 확인해본다. 다음에 또 걸릴 수도 있기 때문.
                    # 중복되면 포인터 민다.
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    result.append(out)
                    # 다 추가한 후 다음으로 넘기기 위한 절차
                    l += 1
                    r -= 1
        return result
