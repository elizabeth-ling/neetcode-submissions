# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
base case: if head is None of head is the last one in the list
else: 
    reverse remaining list
    set head.next to point to head
    set head to point to none
    return reversed list
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case, if head is None or head is the last one in the list
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next) # reverse remaining list
        head.next.next = head
        head.next = None
        return new_head

