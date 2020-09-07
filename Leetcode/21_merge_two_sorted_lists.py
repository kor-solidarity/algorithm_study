# Runtime: 20 ms, faster than 99.99% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.7 MB, less than 88.32% of Python3 online submissions for Merge Two Sorted Lists.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sorted_list = []
        obj1 = l1
        obj2 = l2
        while obj1:
            if obj1.val is not None:
                sorted_list.append(obj1.val)
            obj1 = obj1.next

        while obj2:
            if obj2.val is not None:
                sorted_list.append(obj2.val)
            obj2 = obj2.next
        sorted_list.sort()

        node = None
        for i in range(len(sorted_list) - 1, -1, -1):
            print(i)
            node = ListNode(sorted_list[i], node)

        return node