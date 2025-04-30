class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left, right): 
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        c = head
        while c:
            print(c.val)
            c = c.next
        
        return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

left = 2
right = 4
sol = Solution()
r = sol.reverseBetween(node1, left, right)
print (r)