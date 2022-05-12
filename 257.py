# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []

        def helper(node, prev):
            if not node:
                return
            if prev == "":
                prev = str(node.val)
            else:
                prev = prev+"->"+str(node.val)
            if not node.left and not node.right:
                ans.append(prev)
            helper(node.left, prev)
            helper(node.right, prev)

        helper(root, "")
        return ans
