# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
min heap solution
- put heads of non-empty lists into a min heap
- pop smallest, and add to results list
"""

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        res = ListNode(0)
        curr = res

        while heap:
            val, i, head = heapq.heappop(heap)
            
            curr.next = head
            curr = curr.next

            if head.next:
                heapq.heappush(heap, (head.next.val, i, head.next))
        
        return res.next
