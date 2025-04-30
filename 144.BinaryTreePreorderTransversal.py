class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        values = []
        def goLeft(node):
            if node is None:
                return None
            values.append(node.val)
            goLeft(node.left)
            goRight(node.right)
        def goRight(node):
            if node is None:
                return None
            values.append(node.val)
            goLeft(node.left)
            goRight(node.right)
        goLeft(root)
        return values