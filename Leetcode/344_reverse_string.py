# https://leetcode.com/problems/reverse-string/
# Runtime: 256 ms, faster than 49.67% of Python3 online submissions for Reverse String.
# Memory Usage: 18.5 MB, less than 18.58% of Python3 online submissions for Reverse String.

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 그냥 이 방법도 있고...
        # s.reverse()

        # 리스트 양 끝에 포인터를 만든 후 한칸씩 바꾸기
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


s = ["h", "e", "l", "l", "o"]
Solution().reverseString(s)
