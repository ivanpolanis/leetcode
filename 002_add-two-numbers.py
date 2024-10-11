# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n = 0
        i = 1

        while True:
            n = n + i * l1.val
            if l1.next == None:
                break
            i = i * 10
            l1 = l1.next

        i = 1
        while True:
            n = n + i * l2.val
            if l2.next == None:
                break
            i = i * 10
            l2 = l2.next

        head = ListNode(n % 10, None)
        n = n // 10
        prev = head
        act = head
        while n > 0:
            act = ListNode(n % 10, None)
            prev.next = act
            prev = act
            n = n // 10

        return head
