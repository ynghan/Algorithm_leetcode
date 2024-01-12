# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            # 다음 반복문에서 다음 노드를 사용할 수 있도록 하기 위함
            next_temp = current.next # 2
            # 노드를 거꾸로 만들기 위한 작업 시작
            # 현재 노드가 이전 노드를 가리키기 위함
            current.next = prev # 1 -> None
            # 다음 반복문을 위해 현재 노드가 이전 노드가 되어야 함
            prev = current 
            # 다음 반복문을 위해 다음 노드가 현재 노드가 되어야 함
            current = next_temp
        return prev