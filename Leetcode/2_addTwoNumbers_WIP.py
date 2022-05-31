# https://leetcode.com/problems/add-two-numbers
# Definition for singly-linked list.
# this is wrong.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        obj1 = l1
        obj2 = l2
        while obj1:
            num1 = str(obj1.val) + num1
            obj1 = obj1.next
        while obj2:
            num2 = str(obj2.val) + num2
            obj2 = obj2.next
        result = str(int(num1) + int(num2))

        node = None
        for i in range(0, len(result)):
            print(i, result[i])
            node = ListNode(result[i], node)

        return node
