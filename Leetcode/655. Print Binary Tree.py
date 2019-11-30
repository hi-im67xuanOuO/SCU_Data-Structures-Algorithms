# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root: return [""]
        def getDepth(root):
            if not root:
                return 0
            return 1 + max(getDepth(root.left), getDepth(root.right))
        d = getDepth(root)
        cols = 2 ** d - 1
        self.res = [["" for i in range(cols)] for j in range(d)]
        def helper(root, d, pos):
            self.res[-d - 1][pos] = str(root.val)
            if root.left: helper(root.left, d - 1, pos - 2 ** (d - 1))
            if root.right: helper(root.right, d - 1, pos + 2 ** (d - 1))
        helper(root, d - 1, 2 ** (d - 1) - 1)
        return self.res
