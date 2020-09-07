from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs):
            sample = strs[0]
        else:
            return ''
        prefix = ''
        cut = False
        for i in sample:
            prefix += i
            print(prefix)
            for s in strs:
                if s.find(prefix) != 0:
                    cut = True
                    break
            if cut:
                prefix = prefix[0:-1]
                break
        return prefix
