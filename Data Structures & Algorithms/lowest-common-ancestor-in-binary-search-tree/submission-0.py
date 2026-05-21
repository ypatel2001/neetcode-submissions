# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root 

        # keeps going until we find answer basically
        while cur:
            # check if both p and q fall in one half of tree
            # if they do keep going and reassign current to that split node
            if p.val > cur.val and q.val>cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val<cur.val:
                cur = cur.left
            # if we reach here then that means that p an q split here
            #in which case we immediately return as that is the LCA
            else:
                return cur
                    