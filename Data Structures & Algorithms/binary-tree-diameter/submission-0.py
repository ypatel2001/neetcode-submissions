# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res # allows us to use the outside res 
            #instead one local to the dfs method we made
            if not root:
                return 0
            # get left and right subtree height
            left = dfs(root.left)
            right = dfs(root.right)
            #take the max of the current and left + right as we are adding the paths 
            #for the longest diameter
            res = max(res, left + right)

            return 1 + max(left, right)
        #kick off recursive call 
        dfs(root)
        return res