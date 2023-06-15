# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Runtime: 1082 ms
from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 리스트 최고가와 최저가를 찾고 그 차를 구하기.
        # 최대이익
        profit = 0
        # 최저가. 아래에서 최저가를 구할 때 어떤 수가 나오던 반영이 될 수 있게끔 초기값을 이리 둔다.
        minimum = sys.maxsize

        for p in prices:
            # 최저가 구하기
            minimum = min(minimum, p)
            # 최대이익 구하기
            profit = max(profit, p - minimum)

        return profit
