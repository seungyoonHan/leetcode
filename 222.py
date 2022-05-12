# med
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        if l == r:
            return pow(2, l)+self.countNodes(root.right)
        else:
            return pow(2, r)+self.countNodes(root.left)

    def height(self, root):
        if not root:
            return 0
        return 1+self.height(root.left)
