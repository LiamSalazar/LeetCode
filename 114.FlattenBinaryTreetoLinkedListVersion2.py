class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        prev  = [None]
        def f(root,prev):
            if (not root):
                return 
            f(root.right,prev)
            f(root.left,prev)
            root.right = prev[0]
            root.left = None
            prev[0] = root
        f(root,prev)
        return 
