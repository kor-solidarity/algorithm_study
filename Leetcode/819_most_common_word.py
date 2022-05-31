# https://leetcode.com/problems/most-common-word/
# Runtime: 48 ms, faster than 55.66% of Python3 online submissions for Most Common Word.
# Memory Usage: 13.9 MB, less than 81.66% of Python3 online submissions for Most Common Word.

import collections
from typing import List
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # banned 를 제외한 paragraph 내 가장 많은 단어 반환

        # re.sub - 정규식에 걸린 단어를 그다음 매개변수 값으로 바꾸는 역할을 함
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        return collections.Counter(words).most_common(1)[0][0]
