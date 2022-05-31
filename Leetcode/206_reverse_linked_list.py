# https://leetcode.com/problems/reverse-linked-list/
# Runtime: 76 ms, faster than 5.31% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.5 MB, less than 74.17% of Python3 online submissions for Reverse Linked List.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # singly-linked list 를 역순으로 연결시켜 반환시키기

        # 간단요약: 넥스트 넘기면서 넥스트로 지정된 노드주소를 뒤집어준다.
        # 현위치 노드
        current = head
        # 이전 노드
        previous = None

        while current:
            # 다음 노드. 사전에 배정
            next_node = current.next
            # 현재 노드의 연결점을 이전껄로 전환
            current.next = previous
            # 전환 완료했으면 현 노드는 이전 노드가 변수로 재배정
            previous = current
            # 그리고 다음 노드에서 빼오기
            current = next_node
        # 최종적으로 현 노드가 previous 변수에 있기 때문에 previous 를 반환한다
        return previous
