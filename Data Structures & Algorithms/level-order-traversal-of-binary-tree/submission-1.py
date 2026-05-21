# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #entire algo is basically BFS level order traversal
        res = []
        # we use a queue to hold the nodes as we go through them and pop
        q = deque()
        #start w root
        q.append(root)
        while q:
            # we go through the length of q aka basically the # of nodes 
            qLen = len(q)
            level = []
            for i in range(qLen):
                #popleft most node and then if non null we add to our level 
                # and we add the left and right cjhild nodes it has 
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # once we are done the level, if its non empty, we add it to res
            if level:
                res.append(level)
        return res