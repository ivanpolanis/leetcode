# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, height) -> int:
            if not root:
                return height
            return max(dfs(root.left, height + 1), dfs(root.right, height + 1))

        if not root:
            return 0

        return max(dfs(root.left, 1), dfs(root.right, 1))
