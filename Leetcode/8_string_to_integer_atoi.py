# Runtime: 28 ms, faster than 93.90% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 14.1 MB, less than 5.19% of Python3 online submissions for String to Integer (atoi).


class Solution:
    def myAtoi(self, str: str) -> int:
        # 스페이스 다 빼고 첫칸만 필요하다.
        string = str.split()
        if len(string) == 0:
            return 0
        else:
            string = string[0]

        # 현재 계산중인 단위의 수
        digit = 0
        minus = False
        first = True

        res = 0

        for i in string:
            if first and i == '-':
                minus = True
            elif first and i == '+':
                pass
            elif '0' <= i <= '9':
                if digit != 0:
                    res *= 10
                res += int(i)
                digit += 1
            else:
                break
            if first:
                first = False

        # 계산 다 끝나면 32비트제한 넘겼는지 확인
        if minus:
            res *= -1

        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        elif -2 ** 31 > res:
            res = -2 ** 31

        return res
