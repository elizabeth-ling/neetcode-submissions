# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
we can flatten to an array, and then get the kth index
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def flatten(node):
            if not node:
                return
            
            flatten(node.left)
            arr.append(node.val)
            flatten(node.right)
        
        flatten(root)
        return arr[k-1]
