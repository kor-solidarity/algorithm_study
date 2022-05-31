# https://leetcode.com/problems/linked-list-cycle/
# Runtime: 52 ms, faster than 77.87% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 18.2 MB, less than 7.08% of Python3 online submissions for Linked List Cycle.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 단순 연결 리스트(singly-linked list) 가 순환되는 리스트인지 아닌지 확인하기.
        # 셋을 사용할 예정
        node_set = set()
        # 노드의 다음 연결고리가 없어질때까지 쭉 와일문.
        # 없어지면 순환이 안된다는 말이니 끝.
        while head and head.next is not None:
            # 다음 연결된 노드 객체가 셋 안에 존재하면 순환이 이루어졌다는 것이니 바로 참 반환 후 종료
            if head.next in node_set:
                return True
            # 위 해당사항 없으면 셋에 다음 객체 추가하고 넘긴다.
            node_set.add(head.next)
            head = head.next
        return False
