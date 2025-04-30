class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        result = []
        if not root:
            return result
        queue = []
        queue.append(root)
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result[::-1]