# Runtime: 32 ms, faster than 57.66% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.5 MB, less than 7.38% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        # 홀수면 애초부터 짝이 안맞으니 통과
        if len(s) % 2 != 0:
            return False
        # 여는 괄호
        layer1 = ['(', '[', '{']
        # 닫는 괄호. 위에 맞는 종류의 괄호와 인덱스 맞춰둔다.
        layer2 = [')', ']', '}']
        # 괄호를 확인할 스택
        stack = []

        for i in s:
            # 여는 괄호면 스택에 추가
            if i in layer1:
                stack.append(i)
            elif i in layer2:
                # 닫는 괄호인 경우 우선 어떤 괄호인지 확인한다(match 는 인덱스값).
                match = layer2.index(i)
                # 만일 현재 스택에 쌓인 괄호가 없거나
                # 스택의 마지막 인덱스의 괄호가 같은 종류인지 확인. 불일치하면 거짓 반환.
                if not len(stack) or stack.pop() != layer1[match]:
                    return False
        # 스택이 다 비워졌으면 참. 아니면 거짓.
        return bool(len(stack) == 0)
