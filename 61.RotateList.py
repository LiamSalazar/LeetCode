class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1
        k = k % length
        if k == 0:
            return head
        new_end = head
        for _ in range(length - k - 1):
            new_end = new_end.next
        new_begin = new_end.next
        new_end.next = None
        last.next = head
        return new_begin

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sol = Solution()
r = sol.rotateRight(node1, 2)