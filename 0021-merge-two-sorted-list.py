# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2

        if list2 == None:
            return list1

        head = None
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        act = head
               
        while list1 and list2:
            if list1.val >= list2.val:
                act.next = list2
                act = act.next
                list2 = list2.next
            else:
                act.next = list1
                act = act.next
                list1 = list1.next

        if list1:
            act.next = list1
        else:
            act.next = list2
        
        return head
        
