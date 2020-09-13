# Runtime: 60 ms, faster than 75.62% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 13.8 MB, less than 73.94% of Python3 online submissions for ZigZag Conversion.


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = []
        for i in range(numRows):
            arr.append('')
        # N 자 방향으로 계속 지그재그로 글자를 나열함.
        # 아래로 내려가는 중인가?
        desc = True
        # 몇번째 인덱스에 넣을 것인가.
        index = 0
        for i in range(len(s)):
            arr[index] += s[i]
            # numRows 하나면 어레이를 왔다갔다 하는 일 자체가 없음
            if numRows == 1:
                continue
            if desc:
                # 어레이 아래로 내려가는 중인데 인덱스 초과한 경우 방향 튕겨낸다.
                if index + 1 == len(arr):
                    desc = False
            else:
                # 정반대도 반대쪽에서 동일
                if index == 0:
                    desc = True
            if desc:
                index += 1
            else:
                index -= 1

        answer = ''
        for i in arr:
            answer += i

        return answer
