# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function to validate the BST property recursively
        # Parameters:
        #   node: The current node being checked.
        #   left: The lower bound (exclusive) for the node's value. 
        #         All nodes in this subtree must be strictly greater than 'left'.
        #   right: The upper bound (exclusive) for the node's value.
        #          All nodes in this subtree must be strictly less than 'right'.
        def valid(node, left, right):
            # Base Case: An empty node (subtree) is a valid BST.
            if not node:
                return True
            
            # Check current node's value against the bounds inherited from ancestors.
            # The node's value must be strictly within the (left, right) range.
            if not (left < node.val < right): 
                return False # Violation of BST property found.

            # Recursively check the left and right subtrees.
            # Left subtree: 
            #   - Must still be greater than the original 'left' bound.
            #   - Must now be strictly less than the current 'node.val' (new upper bound).
            # Right subtree:
            #   - Must now be strictly greater than the current 'node.val' (new lower bound).
            #   - Must still be less than the original 'right' bound.
            # Both subtrees must be valid BSTs.
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        # Start the validation process from the root node.
        # Initialize the bounds as negative infinity and positive infinity,
        # as the root itself has no value restrictions initially.
        return valid(root, float("-inf"), float("inf"))