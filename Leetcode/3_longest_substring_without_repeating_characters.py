# Runtime: 84 ms, faster than 46.49% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13.8 MB, less than 90.49% of Python3 online submissions for
#  Longest Substring Without Repeating Characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 가장 긴 중복없이 이어지는 글자의 길이를 찾으라는 질문. 릿코드 53번과 매우 흡사.
        # "abcabcbb" 인 경우 abc 가 중복없이 가장 많이 이어질 수 있으므로 그 길이는 3

        # 접근법:
        # 시작 포인터와 종료 포인터를 하나씩 집는다. >> i, j
        # i 번째 글자를 잡고 j 번째를 하나하나 늘리면서 인덱스 i, j 사이의 글자에 중복되는 글자가 있는지 확인한다.

        # 길이가 하나짜리면 어차피 하나니 1 반환
        if len(s) == 1:
            return 1

        # 정답이 될 수를 넣을 변수, 그리고 넘길 인덱스번호
        num, i, j = 0, 0, 1
        # 조건문: i나 j 가 인덱스를 넘어가지만 않으면 된다.
        while i < len(s) and j <= len(s):
            # 중복여부
            overlap = False
            # 중복여부를 확인할 스트링
            target = s[i:j]
            for k in target:
                # 만약 글자가 하나라도 중복되는게 있으면 i 인덱스를 넘긴다.
                if target.count(k) > 1:
                    i = i + 1
                    overlap = True
                    break
            # 중복이 안된 상황이면 target 길이가 num 보다 큰지 확인한다.
            if not overlap and len(target) > num:
                num = len(target)
            # 우선 j 인덱스 넘기기
            j += 1
        return num
