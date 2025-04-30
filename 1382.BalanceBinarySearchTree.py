def inorder(root, nodes):
    if root:
        inorder(root.left, nodes)
        nodes.append(root)
        inorder(root.right, nodes)

def buildBalanced(nodes, l, r):
    if l > r:
        return None
    m = (l + r) // 2
    root = nodes[m]
    root.left = buildBalanced(nodes, l, m - 1)
    root.right = buildBalanced(nodes, m + 1, r)
    return root

class Solution(object):
    def balanceBST(self, root):
        nodes = []
        inorder(root, nodes)
        return buildBalanced(nodes, 0, len(nodes) - 1)
