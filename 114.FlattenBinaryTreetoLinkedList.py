class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        if root:
            values = []
            def DFS(node):
                if node is None:
                    return None
                values.append(node.val)
                DFS(node.left)
                DFS(node.right)
            DFS(root)
            root.left = None
            root.right = None
            values.pop(0)
            current = root
            while values:
                current.right = TreeNode(values.pop(0))
                current = current.right