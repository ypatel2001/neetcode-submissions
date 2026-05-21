# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function using Depth First Search (DFS)
        # Returns a list: [isSubtreeBalanced, heightOfSubtree]
        def dfs(root):
            # Base Case: An empty tree (None node) is considered balanced and has a height of 0.
            if not root:
                return [True, 0]

            # Recursively call dfs on left and right children.
            # left will be [isLeftBalanced, leftHeight]
            # right will be [isRightBalanced, rightHeight]
            left, right = dfs(root.left), dfs(root.right)
            
            # Determine if the current subtree (rooted at 'root') is balanced.
            # Conditions:
            # 1. The left subtree must be balanced (left[0]).
            # 2. The right subtree must be balanced (right[0]).
            # 3. The absolute difference in heights between left and right subtrees <= 1.
            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)
            
            # Calculate the height of the current subtree.
            # Height = 1 (for the current node) + maximum height of its children.
            height = 1 + max(left[1], right[1])
            
            # Return the balance status and height for the current subtree.
            return [balanced, height]

        # Start the DFS from the actual root of the tree.
        # The result of dfs(root) is [isWholeTreeBalanced, heightOfWholeTree].
        # We only need the boolean balance status, which is the first element ([0]).
        return dfs(root)[0]