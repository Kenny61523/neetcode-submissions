# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False














# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         prev = {}
#         curr = head
#         while curr:
#             prev[curr.val] = prev.get(curr.val, 0) + 1
#             if prev[curr.val] > 1:
#                 return True
#             curr = curr.next
#         return False
        