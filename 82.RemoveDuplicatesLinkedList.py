class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution():
    def deleteDuplicates(self, head):
        current = ListNode(0, head)
        aux = current  
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                aux.next = head.next
            else:
                aux = aux.next
            head = head.next
        
        return current.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

sol = Solution()
r = sol.deleteDuplicates(node1)
print(r)