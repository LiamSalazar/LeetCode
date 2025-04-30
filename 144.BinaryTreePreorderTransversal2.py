class Treeroot(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        values = []
        def DFS(node):
            if node is None:
                return None
            values.append(node.val)
            DFS(node.left)
            DFS(node.right)
        DFS(root)
        return values