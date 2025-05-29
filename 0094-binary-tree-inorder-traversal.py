# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, root, res):
        if root == None:
            return
        if root.left:
            self.traverse(root.left, res)

        res.append(root.val)

        if root.right:
            self.traverse(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traverse(root, res)
        return res
