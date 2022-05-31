# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Runtime: 32 ms, faster than 98.94% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 14.4 MB, less than 25.31% of Python3 online submissions for Remove Duplicates from Sorted List.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 다른 변수에 같은 오브젝트 할당
        cur = head
        while cur:
            # 다음 값이 존재하고 중복인 경우 링크를 그 다음으로 건너뛴다.
            while cur.next and cur.next.val == cur.val:
                # 이걸로 cur 위치 자체가 변경됨
                cur.next = cur.next.next
            cur = cur.next
        return head
