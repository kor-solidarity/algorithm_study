# Runtime: 32 ms, faster than 73.48% of Python3 online submissions for Add Binary.
# Memory Usage: 14.3 MB, less than 17.47% of Python3 online submissions for Add Binary.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 2진수로 된 스트링 형태의 숫자 두개를 이진수로 합치는게 목적.

        # 10진수로 변환
        a_int = int(a, 2)
        b_int = int(b, 2)

        return bin(a_int + b_int)[2:]
