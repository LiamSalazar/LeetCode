class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        def dfs(root, sum):
            if not root:
                return 0
            sum = sum * 10 + root.val
            if not root.left and not root.right:
                return sum
            return dfs(root.left, sum) + dfs(root.right, sum)
        return dfs(root, 0)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

sol = Solution()
output = sol.sumNumbers(root)

print(output) 