class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        nums = []
        def transversalDFS(node):
            if not node:
                return
            transversalDFS(node.left)
            nums.append(node.val)
            transversalDFS(node.right)
        transversalDFS(root)
        return nums