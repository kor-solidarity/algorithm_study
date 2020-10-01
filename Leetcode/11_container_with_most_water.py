# Runtime: 116 ms, faster than 97.71% of Python3 online submissions for Container With Most Water.
# Memory Usage: 15.8 MB, less than 7.78% of Python3 online submissions for Container With Most Water.
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maximum = 0

        while start < end:
            length = end - start
            alt = min([height[start], height[end]])
            if maximum < alt * length:
                maximum = alt * length
            # 짧은 쪽을 계속 안쪽으로 보낸다.
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maximum
