# https://leetcode.com/problems/reorder-data-in-log-files/
# Runtime: 60 ms, faster than 29.24% of Python3 online submissions for Reorder Data in Log Files.
# Memory Usage: 14.1 MB, less than 7.50% of Python3 online submissions for Reorder Data in Log Files.

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 첫 단어는 식별자, 그 다음부터가 실제 정렬해야 하는 내용
        # 단어-숫자 순
        # 단어는 알파벳, 숫자는 원래 순서대로.

        letters, digits = [], []
        for i in logs:
            if i.split()[1].isdigit():
                digits.append(i)
            else:
                letters.append(i)

        # 단어 목록 정렬.
        # 두번째 단어부터를 기준으로 정렬, 거기서 동일하면 식별자 동원.
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

# logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
#
# solution = Solution()
#
# print(solution.reorderLogFiles(logs))
