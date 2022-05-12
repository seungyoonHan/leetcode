# med
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):  # sol1
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def backtrack(node):
            if not node:
                return False
            l = backtrack(node.left)
            r = backtrack(node.right)
            m = node == p or node == q
            if l+r+m >= 2:
                self.ans = node
                return True
            return m or l or r
        backtrack(root)
        return self.ans
