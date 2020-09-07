# fyi Palindrome Number = 대칭수
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 문제 조건상 마이너스는 무조건 해당안됨.
        if x < 0:
            return False
        # 한자리수는 무조건 성립
        elif x < 10:
            return True
        # 0으로 끝나는건 단위하나가 날아가는거니 역시 통과
        elif x % 10 == 0:
            return False
        digits = len(str(x))
        for i in range(digits):
            if not str(x)[i] == str(x)[digits - 1 - i]:
                return False
        return True
