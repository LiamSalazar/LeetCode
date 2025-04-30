class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        def add(root, currentSum):
            if not root:
                return False
            currentSum += root.val
            if not (root.left or root.right):
                return currentSum == targetSum
            return add(root.left, currentSum) or add(root.right, currentSum)
        return add(root, 0)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
target = 1
sol = Solution()
r = sol.hasPathSum(node1, target)
print(r)