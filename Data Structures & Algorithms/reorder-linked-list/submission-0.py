# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            nxt = curr.next # save next node
            curr.next = prev # reverse pointer
            prev = curr # move prev forward
            curr = nxt # move curr forward 

        # merge head and prev
        while prev:
            nxt = head.next
            head.next = prev
            prev = prev.next
            head.next.next = nxt
            head = head.next.next

        