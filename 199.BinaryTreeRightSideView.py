class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1
class Solution(object):
    def rightSideView(self, root):
        result = []
        if not root:
            return result
        queue = []
        queue.append(root)
        output = []
        while queue:
            temp = []
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(temp)
        for level in result:
            num = level.pop()
            output.append(num)
        return output

# Solution 2
class Solution(object):
    def rightSideView(self, root):
        output = []
        if not root:
            return output
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i == n - 1:
                    output.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return output