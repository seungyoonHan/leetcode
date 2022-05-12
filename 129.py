# med
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.leaves = 0
        self.helper(root, 0)
        return self.leaves

    def helper(self, root, v):
        if not root:
            return 0
        v = v*10+root.val
        if not root.left and not root.right:
            self.leaves += v

        self.helper(root.left, v)
        self.helper(root.right, v)
