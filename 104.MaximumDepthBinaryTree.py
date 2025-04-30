class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        RightDepth = self.maxDepth(root.right)
        return 1 + max(leftDepth, RightDepth)

node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(1)
node4 = TreeNode(5)
node5 = TreeNode(6)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

sol = Solution()
r = sol.maxDepth(node1)
print(r)