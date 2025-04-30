class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sortedArrayToBST(self, nums):
        def addNode(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = addNode(left, mid - 1)
            node.right = addNode(mid+1, right)
            return node
        return addNode(0, len(nums)-1)