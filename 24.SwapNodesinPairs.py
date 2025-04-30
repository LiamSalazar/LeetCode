class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        current = head
        while current:
            if current.next is not None:
                nextNode = current.next 
                current.val, nextNode.val = nextNode.val, current.val
                current = current.next.next 
            else: break 
        return head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

sol = Solution()
r = sol.swapPairs(node1)