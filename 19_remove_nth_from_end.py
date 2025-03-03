# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        lenght = 0
        while(node != None):
            lenght += 1
            node = node.next

        pos = lenght - n

        if pos == 0:
            return head.next

        node = head
        while (pos > 1):
            pos-=1;
            node = node.next

        if pos == lenght - 1:
            node.next = None
        else:
            node.next = node.next.next

        return head
