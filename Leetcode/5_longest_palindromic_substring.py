# https://leetcode.com/problems/longest-palindromic-substring
# Runtime: 100 ms, Beats 97.67%
# Memory: 13.9 MB, Beats 86.81%

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 가장 긴 대칭 섭스트링값 구하기

        # 포인터 확장 and 페일린드롬 판별
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 역순으로 슬라이싱하여 모두 동일한 경우 페일린드롬에 해당하니 그대로 반환
        if s == s[::-1]:
            return s
        result = ''
        for i in range(0, len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result
