class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        current = head
        minValues = []
        maxValues = []
        while current is not None:
            if current.val < x:
                minValues.append(current.val)
            else:
                maxValues.append(current.val)
            current = current.next
        minValues=minValues + maxValues
        current = head
        i = 0
        while current is not None:
            current.val = minValues[i]
            i += 1
            current = current.next
        return head
node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

x = 3
sol = Solution()
r = sol.partition(node1, 3)
print(r)