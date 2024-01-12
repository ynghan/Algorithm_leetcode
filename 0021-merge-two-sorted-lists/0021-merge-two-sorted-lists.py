class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        # 더미 노드를 사용하여 결과 리스트의 헤드를 초기화하여야 한다.
        current = result
        while list1 and list2:
            if list1.val <= list2.val:
                a = list1
                current.next = list1
                list1 = list1.next
                current = current.next
                
            else:
                a = list2
                current.next = list2
                list2 = list2.next
                current = current.next
            

        # list1 또는 list2 중 하나가 더 이상 없을 때 나머지 리스트를 연결한다.
        current.next = list1 if list1 else list2

        return result.next