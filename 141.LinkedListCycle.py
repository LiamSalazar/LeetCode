class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False