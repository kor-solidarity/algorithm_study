class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(abs(x))
        answer_str = ''
        for i in x_str:
            answer_str = i + answer_str
        answer = int(answer_str)
        # 32비트 초과하는지 확인
        if x < 0:
            if answer >= (1 << 31):
                answer = 0
            else:
                answer *= -1
        elif answer > (1 << 31):
            answer = 0
        return answer

