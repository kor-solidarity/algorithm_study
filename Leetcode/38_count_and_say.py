# Runtime: 32 ms, faster than 88.33% of Python3 online submissions for Count and Say.
# Memory Usage: 13.6 MB, less than 97.87% of Python3 online submissions for Count and Say.


class Solution:
    # 작동방식: 1로 시작,
    # 그 다음은 1이 하나니 one one = 11,
    # 11은 1이 둘이니 two one = 21
    # 21은 2가 둘 1이 하나니 one two one one = 1211
    # 111221 >> 312211 and so on...

    def countAndSay(self, n: int) -> str:
        # 최초값이자 최종적으로 뽑혀야 하는 결과물. 1부터 시작.
        start = '1'
        for i in range(n):
            # 어차피 첫시작이 1이라 굳이 아래 돌 이유가 없음.
            if n == 1:
                return '1'
            # 첫번째껀 건너뛴다.
            elif i == 1:
                continue
            # 당장 세고있는 숫자. start 최초값의 첫숫자로 시작한다.
            pointer = start[0]
            # n값 하나씩 넘길때마다 매번 새로 갱신될 값
            temp = ''
            # 위 포인터가 몇번 중복됬는지 확인
            counter = 0
            for j in start:
                # 포인터의 값과 같으면 카운터를 올린다.
                if pointer == j:
                    counter += 1
                # 카운터와 포인터값 뽑아내고 교체.
                else:
                    temp += str(counter) + pointer
                    pointer = j
                    # 위에 포인터 교체한것도 센다
                    counter = 1
            # 맨 마지막에 카운터가 0 보다 많으면 추가.
            if counter > 0:
                temp += str(counter) + pointer
            start = temp
        return start
