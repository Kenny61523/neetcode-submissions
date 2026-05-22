# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle node
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print("check1")
        # reverse the second half of the linked list
        cur = slow.next
        slow.next = None # missing 
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        print("check2")

        cur = head
        cur2 = prev
        while cur and cur2:
            tmp = cur.next
            tmp2 = cur2.next
            cur.next = cur2
            cur2.next = tmp
            cur = tmp
            cur2 = tmp2

        return
            
