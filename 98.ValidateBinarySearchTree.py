class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        def go(root, minValue, maxValue):
            if not root:
                return True
            if root.val <= minValue or root.val >= maxValue:
                return False
            return go(root.right, root.val, maxValue) and go(root.left, minValue, root.val)

        return go(root.right, root.val, float('inf')) and go(root.left, float('-inf'), root.val)


node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(1)
node1.left = node2
node1.right = node3
sol = Solution()
print(sol.isValidBST(node1)) # True