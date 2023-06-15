# https://leetcode.com/problems/valid-palindrome/
# Runtime: 86 ms, faster than 23.92% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 20.2 MB, less than 5.11% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []

        # 글자별로 자른다.
        for c in s:
            # 해당 스트링이 문자·숫자인지 확인하는 내장함수
            if c.isalnum():
                # 해당되면 리스트에 추가.
                letters.append(c.lower())

        # 역순이랑 비교해서 똑같은지 확인만 하면 끝.
        return letters == letters[::-1]
