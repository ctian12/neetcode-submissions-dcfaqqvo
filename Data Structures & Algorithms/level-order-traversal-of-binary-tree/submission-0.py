# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        def dfs(node, level):
            if not node:
                return None
            if len(out) == level:
                out.append([])
            out[level].append(node.val)
            level += 1
            dfs(node.left, level)
            dfs(node.right, level)
        dfs(root, 0)
        return out