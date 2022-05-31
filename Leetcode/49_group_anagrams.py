# https://leetcode.com/problems/group-anagrams/
# Runtime: 143 ms, faster than 48.77% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.1 MB, less than 96.57% of Python3 online submissions for Group Anagrams.
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 아나그램: 기존의 단어의 문자를 재배열해서 만드는 새로운 단어
        # 같은 글자들로 구성된 단어들의 묶음을 반환하기.
        anagrams = collections.defaultdict(list)

        for s in strs:
            # sorted() 를 쓰면 글자 하나하나 정렬됨
            # ''.join() 으로 쪼갠걸 하나로 합침. 키값으로 묶기 가능.
            anagrams[''.join(sorted(s))].append(s)
        return list(anagrams.values())
