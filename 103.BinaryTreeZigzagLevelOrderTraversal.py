class Solution(object):
    def zigzagLevelOrder(self, root):
        result = []
        if not root:
            return result
        queue = [root]
        left = True  
        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left:
                temp.reverse()

            result.append(temp)
            left = not left  
        return result