# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """

        self.parsum = []
        self.targetSum = targetSum
        if root == None:
            return []
        path = []
        self.helper(root, 0, path)
        return self.parsum

    def helper(self, root, psum, path):
        if root == None:
            return
        # print(root.val,psum,path)
        psum += root.val
        # path.append(root.val)
        if root.left == None and root.right == None:
            if psum == self.targetSum:
                path.append(root.val)
                self.parsum.append(path)
                return
        self.helper(root.left, psum, path+[root.val])
        self.helper(root.right, psum, path+[root.val])
