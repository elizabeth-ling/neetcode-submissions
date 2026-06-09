# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
iterative solution/two ptrs:
- l = head, r is always n steps ahead
- when r.next is none, l.next = l.next.next
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        l, r = head, head

        # move r n steps head
        while n:
            r = r.next
            n -= 1
        
        if not r:
            return head.next
            
        while r.next:
            r = r.next
            l = l.next
        
        l.next = l.next.next

        return head