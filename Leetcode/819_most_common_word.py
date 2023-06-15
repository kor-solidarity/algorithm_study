# https://leetcode.com/problems/most-common-word/
# Runtime: 44 ms, Beats 39.34%
# Memory: 14 MB, Beats 25.76%

import collections
from typing import List
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 먼저 paragraph 내 단어들을 추출 - 쉼표 마침표 등 다 제거
        # 동시에 banned 목록에 있는 단어와 중복되는 단어 다 제거.
        # re.sub - 정규식에 걸린 단어를 그다음 매개변수 값으로 바꾸는 역할을 함
        words = [word for word in re.sub(r'\W', ' ', paragraph).lower().split() if word not in banned]
        return collections.Counter(words).most_common(1)[0][0]
