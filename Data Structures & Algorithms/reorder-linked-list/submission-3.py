# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Reverse LinkedList
        cur = slow.next # middle pointer
        slow.next = None # prevent circular separate the backward link
        prev = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        cur = head
        cur2 = prev 
        while cur2:
            tmp, tmp2 = cur.next, cur2.next
            cur.next = cur2
            cur2.next = tmp
            cur = tmp
            cur2 = tmp2
        
        return
