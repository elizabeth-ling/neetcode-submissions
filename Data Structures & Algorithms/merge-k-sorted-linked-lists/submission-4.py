# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
write function to merge two lists
repeat for all items in lists
"""

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = None
        for lst in lists:
            merged = self.mergeTwoLists(merged, lst)
        
        return merged

    def mergeTwoLists(self, L1: Optional[ListNode], L2: Optional[ListNode]):
        res = ListNode()
        curr = res

        while L1 and L2:
            if L1.val > L2.val:
                curr.next = L2
                L2 = L2.next
            else:
                curr.next = L1
                L1 = L1.next
            curr = curr.next

        if L1:
            curr.next = L1
        else:
            curr.next = L2

        return res.next


