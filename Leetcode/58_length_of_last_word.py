# Runtime: 20 ms, faster than 98.92% of Python3 online submissions for Length of Last Word.
# Memory Usage: 13.7 MB, less than 94.86% of Python3 online submissions for Length of Last Word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s.split():
            return 0
        return len(s.split()[-1])
