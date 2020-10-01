# Runtime: 52 ms, faster than 71.38% of Python3 online submissions for Regular Expression Matching.
# Memory Usage: 14.2 MB, less than 9.21% of Python3 online submissions for Regular Expression Matching.
import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        regex = re.compile(p)
        a = regex.fullmatch(s)
        if a:
            return True
        return False
