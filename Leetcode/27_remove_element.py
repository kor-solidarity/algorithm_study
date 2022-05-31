from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # val 값이 리스트에 있는 수를 구하고 목록에서 그 값을 제외한 후
        # 그 수만큼까지의 리스트 인덱스를 반환한다(반환은 자동)
        # count = 0
        counter = 0
        list_copy = nums.copy()
        for i in list_copy:
            print(i)
            if i == val:
                nums.remove(i)
                # count += 1
            counter += 1
        return counter
