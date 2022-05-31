# https://leetcode.com/problems/longest-palindromic-substring
# Runtime: 944 ms, faster than 82.88% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 13.8 MB, less than 66.19% of Python3 online submissions for Longest Palindromic Substring.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 가장 긴 대칭 섭스트링값 구하기

        # 길이가 1 이하면 계산할 필요가 없다.
        if len(s) <= 1:
            return s

        answer = ''
        # 포문으로 기준점 하나씩 돌려가면서 퍼뜨린다.
        for i in range(len(s)):
            # 홀수 그리고 짝수일 경우 하나씩 돌아가면서 확인한다.
            res = self.palindrome(s, i, i)
            # 짝수
            res_even = self.palindrome(s, i, i + 1)
            # 짝수결과의 길이가 홀수보다 큰 경우 덮어씌운다.
            if len(res) < len(res_even):
                res = res_even
            if len(answer) < len(res):
                answer = res

        return answer

    def palindrome(self, s, start, end) -> str:
        # start 와 end 는 각각 벌려질 기준 인덱스다.

        # 서로 안맞을때까지 인덱스 끝까지 돌리는거
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start + 1:end]
