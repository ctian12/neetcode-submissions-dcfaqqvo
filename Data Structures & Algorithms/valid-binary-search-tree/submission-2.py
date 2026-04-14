# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        out = True
        def dfs(node, lower, upper):
            nonlocal out
            if not node:
                return
            if node.val >= upper or node.val <= lower:
                out = False
            dfs(node.left, lower, node.val)
            dfs(node.right, node.val, upper)
        dfs(root, -1 * sys.maxsize, sys.maxsize)
        return out