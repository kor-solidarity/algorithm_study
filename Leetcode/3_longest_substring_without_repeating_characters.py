class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 가장 긴 중복없이 이어지는 글자의 길이를 찾으라는 질문.
        # brute force
        for i in range(len(s)):
