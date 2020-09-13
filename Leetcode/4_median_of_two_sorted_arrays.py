# Runtime: 92 ms, faster than 87.72% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 13.9 MB, less than 86.83% of Python3 online submissions for Median of Two Sorted Arrays.
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 받은 어레이를 정렬한 후 가운데 인덱스에 있는 값을 구한다.
        # 만일 짝수라 가운데가 안 걸리면 가운데 두 숫자의 평균값을 구한다.

        the_list = []
        the_list.extend(nums1)
        the_list.extend(nums2)

        the_list.sort()

        # 리스트의 길이가 홀수면 가운데 인덱스 그대로 뽑고 짝수면 가운데 두 수의 평균을 구한다.
        # 기본값은 홀수일 때 인덱스값
        index = len(the_list) // 2
        if len(the_list) % 2 == 1:
            return float(the_list[index])
        # 짝수인 경우 위 인덱스값과 그 이전 인덱스값의 평균값을 구해야 한다.
        else:
            return (the_list[index] + the_list[index-1]) / 2
