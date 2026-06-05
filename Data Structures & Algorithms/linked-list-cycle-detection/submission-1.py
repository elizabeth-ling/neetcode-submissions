# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
hash set stores seen node ref
time: O(n)
space: O(n)
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_set = set()

        while head and head.next:
            if head in hash_set:
                return True
            hash_set.add(head)
            head = head.next

        return False