# Runtime: 36 ms, faster than 98.55% of Python3 online submissions for Integer to Roman.
# Memory Usage: 14.2 MB, less than 5.10% of Python3 online submissions for Integer to Roman.


class Solution:
    def intToRoman(self, num: int) -> str:
        # 숫자를 로마숫자로 바꾸기.

        digit = 3
        answer = ''
        # 천단위부터 시작해서 5씩 쪼개본다.
        roman_num = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

        # 맨 앞자리 부터 차례로 뽑는다. 단, 5단위인지 확인해야함.
        while digit >= 0:
            # 단위 확인
            number = int(num / 10 ** digit)
            # 해당 단위가 있으면 진행
            if number > 0:
                # 숫자가 9/5/4인가?
                # 9면 현 단위 + 현 단위 위 단위 하나씩 넣어야함.
                # 5면 현 단위의 5단위
                # 4면 현 단위 + 현 단위의 5단위
                # 단, 천단위면 제외
                if digit == 3:
                    answer += roman_num[10 ** digit] * number
                elif number == 9:
                    answer += roman_num[10 ** digit] + roman_num[10 ** (digit + 1)]
                elif number == 5:
                    answer += roman_num[10 ** digit * 5]
                elif number == 4:
                    answer += roman_num[10 ** digit] + roman_num[10 ** digit * 5]
                # 그 외는 그냥 5 고려하면서 기존값 곱한다.
                else:
                    if number - 5 > 0:
                        answer += roman_num[10 ** digit * 5]
                    answer += roman_num[10 ** digit] * (number % 5)
                # 다 끝나면 해당 단위 값을 없앤다.
                num -= number * 10 ** digit
            digit -= 1

        return answer


print(Solution().intToRoman(58))
