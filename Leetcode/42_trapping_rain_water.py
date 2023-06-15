# https://leetcode.com/problems/trapping-rain-water/
# Runtime: 141 ms, Beats 49.37%
# Memory 15.9 MB, Beats 95.97%
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산

        # 빈 리스트인 경우 계산없이 0
        if not height:
            return 0

        volume = 0
        # 포인터 지정 - height index
        left, right = 0, len(height) - 1
        # 양 끝부터의 기둥 최대 높이 - height val.
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            # 더 높은 쪽으로 포인터 이동
            if left_max <= right_max:
                # right 부분은 아예 여기서 신경쓸 필요가 없다. 아래 else 문에서 반대 left도 마찬가지
                # left max 가 최대 높이이니 height[left] 를 뺀 만큼 물이 고인다.
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
