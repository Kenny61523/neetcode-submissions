# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        #edge len = 0
        if curr is None or curr.next is None:
            return 
        

        # reverse linked ist.
        # find the length. 
        index = 0
        while curr:
            curr = curr.next
            index += 1
        
        print(index)
        print("a")

        index -= n
        print(index)

        curr = head
        if (index == 0):
            curr = curr.next
            return curr

        while True:                
            if (index <= 1):
                curr.next = curr.next.next
                break
            else: 
                curr = curr.next
                print(index)
            index -= 1
        
        return head