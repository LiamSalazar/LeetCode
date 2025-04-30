class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and 
                    isMirror(t1.left, t2.right) and 
                    isMirror(t1.right, t2.left))
        return isMirror(root.left, root.right)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(3)
node1.left = node2
node1.right = node3
node2.left = node4
node3.right = node5

sol = Solution()
r = sol.isSymmetric(node1)
print(r)