# Runtime: 692 ms, faster than 86.17% of Python3 online submissions for 3Sum.
# Memory Usage: 17.6 MB, less than 29.46% of Python3 online submissions for 3Sum.
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 제공된 숫자가 있는 목록에서 값 셋을 골라서 0이 될 수 있는 조합의 목록을 반환하기.

        # 우선 크기별로 정렬한다
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 2):
            # 첫번째 수가 0보다 크면 그다음은 볼필요도 없다.
            if nums[i] > 0:
                break
            # 이전 숫자값이 지금꺼랑 중복이 안되게끔 조치
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 확인할 인덱스. 하나는 중간, 하나는 마지막
            j, k = i + 1, n - 1
            while j < k:
                the_sum = nums[i] + nums[j] + nums[k]
                # 썸값이 너무 낮으면 중간 인덱스를 올린다.
                if the_sum < 0:
                    j += 1
                # 너무 높으면 마지막 인덱스를 줄인다.
                elif the_sum > 0:
                    k -= 1
                # 엘스는 무조건 정답
                else:
                    output = [nums[i], nums[j], nums[k]]
                    # 다음으로 넘어갈 숫자가 혹시 중복되는지 확인해본다.
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    result.append(output)
                    j += 1
                    k -= 1
        return result
