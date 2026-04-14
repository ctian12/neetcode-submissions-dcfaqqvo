# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curmax):
            if not node:
                return 0
            if node.val >= curmax:
                count = 1
                curmax = node.val
            else:
                count = 0
            count += dfs(node.left, curmax)
            count += dfs(node.right, curmax)
            return count
        return dfs(root, root.val)