class Solution:
    def romanToInt(self, s: str) -> int:
        # 로마 숫자 읽는 방식:
        # 특정 수 앞에 그 수보다 적은 수가 있으면 그만큼 빼고 아니면 하나하나 다 더한다.
        roman_num = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        answer = 0
        # 뒤에서 앞으로 하나하나 더하고 중간에 수가 적은게 있으면 그만큼 빼면 그만인거임.
        last_val = 0
        for i in range(len(s)-1, -1, -1):
            curr_val = roman_num[s[i]]
            # 지금 숫자가 이전 수보다 적은 경우 뺀다.
            if curr_val < last_val:
                answer -= curr_val
            else:
                answer += curr_val
            last_val = curr_val
        return answer