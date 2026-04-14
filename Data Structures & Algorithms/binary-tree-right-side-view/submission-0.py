# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        maxLevel = 0
        currLevel = 1
        def dfs(node, level):
            nonlocal maxLevel
            if not node:
                return
            if level > maxLevel:
                out.append(node.val)
                maxLevel = level
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, currLevel)
        return out
