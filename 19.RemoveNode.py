
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        current = head
        reference = []
        while current is not None:
            reference.append(current)
            current = current.next
        count = len(reference) - n
        if count == 0:
            return head.next
        current = reference[count - 1] 

        if current.next is not None:
            current.next = current.next.next  

        return head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

n = 2

sol = Solution()
r = sol.removeNthFromEnd(node1, n)
print(r)