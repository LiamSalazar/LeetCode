class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    return 0 if root is None else 1 + max(height(root.left), height(root.right))

def balanceFactor(root):
    return (height(root.left) - height(root.right))

def turnRight(root):
    if root is None or root.left is None: return None
    temp = root.left
    newChild = temp.right
    return TreeNode(temp.val, temp.left, TreeNode(root.val, newChild, root.right))

def turnLeft(root):
    if root is None or root.right is None: return None
    temp = root.right
    newChild = temp.left
    return TreeNode(temp.val, TreeNode(root.val, root.left, newChild), temp.right)

class Solution(object):
    def balanceBST(self, root):
        if not root:
            return None
        left = self.balanceBST(root.left)
        right = self.balanceBST(root.right)
        new = TreeNode(root.val, left, right)
        bf = balanceFactor(new)
        if bf > 1:
            if balanceFactor(left) >= 0:
                return turnRight(new)
            else:
                left = turnLeft(left)
                new = TreeNode(root.val, left, right)
                return turnRight(new)
        elif bf < -1:
            if balanceFactor(right) <= 0:
                return turnLeft(new)
            else:
                right = turnRight(right)
                new = TreeNode(root.val, left, right)
                return turnLeft(new)
        return new
