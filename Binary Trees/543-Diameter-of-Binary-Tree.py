# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # took inspiration from 124. Binary Tree Maximum Path Sum
        self.ans = 1
        def dfs(node):
            if not node:
                return 0
            
            leftlen = dfs(node.left)
            rightlen = dfs(node.right)

            self.ans = max(self.ans, 1+leftlen+rightlen)

            # when returning it we only return the max of left or the right subtree
            # because the root of subtree must be used only once
            return 1+max(leftlen,rightlen)
        
        dfs(root)
        return self.ans - 1
