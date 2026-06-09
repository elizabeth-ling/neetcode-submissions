# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
fast and slow ptr
when not fast or not fast.next, slow will be in middle
reverse slow
merge the two lists 
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse slow
        head2 = slow.next
        slow.next = None

        prev = None
        while head2:
            nxt = head2.next
            head2.next = prev
            prev = head2
            head2 = nxt

        # merge head and head2
        head2 = prev
        while head2:
            nxt1 = head.next
            nxt2 = head2.next

            head.next = head2
            head2.next = nxt1

            head = nxt1
            head2 = nxt2


        



        