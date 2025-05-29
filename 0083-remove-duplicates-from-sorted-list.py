# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        prev, act = head, head.next
        while True:
            if act == None:
                prev.next = act
                break
            while act.next != None and act.val == prev.val:
                act = act.next

            if act.val != prev.val:
                prev.next = act
                prev = prev.next
            act = act.next
        return head
