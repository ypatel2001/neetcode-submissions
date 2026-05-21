# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            # we need to get the max of each of the 
            #2 subtrees so we don't double count

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))