class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        referencia = []
        values = []
        current = head
        while current is not None:
            referencia.append(current.val)  
            current = current.next
        for i in range(0, len(referencia), k):
            grupo = referencia[i:i+k]  
            if len(grupo) == k:  
                values.extend(grupo[::-1])  
            else:
                values.extend(grupo)
        current = head
        count = 0
        while current is not None:
            current.val = values[count]
            current = current.next
            count += 1
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

k = 2
sol = Solution()
r = sol.reverseKGroup(node1, k)