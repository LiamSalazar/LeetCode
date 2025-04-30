class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        nums = []
        def postDFS(node):
            if not node:
                return
            if node.left is not None:
                postDFS(node.left)
            if node.right is not None:
                postDFS(node.right)
            nums.append(node.value)
        postDFS(root)
        return nums