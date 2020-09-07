# Runtime: 36 ms, faster than 66.30% of Python3 online submissions for Plus One.
# Memory Usage: 14 MB, less than 19.61% of Python3 online submissions for Plus One.

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        numbers = 0
        digit = 1
        for i in range(len(digits) - 1, -1, -1):
            numbers += digits[i] * digit
            print(i)
            digit *= 10

        output = []
        for i in str(numbers):
            output.append(i)

        return output
