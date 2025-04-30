class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None
        slow, fast, prevSlow = head, head, None
        while fast and fast.next:
            prevSlow = slow
            fast, slow = fast.next.next, slow.next
        node = TreeNode(slow.val)
        if prevSlow:
            prevSlow.next = None
            node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node