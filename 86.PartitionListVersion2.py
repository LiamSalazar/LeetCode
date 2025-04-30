class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        current = head
        min_head = ListNode(0)
        max_head = ListNode(0)
        min = min_head
        max = max_head
        while current:
            if current.val < x:
                min.next = current
                min = min.next
            else:
                max.next = current
                max = max.next
            current = current.next
        max.next = None
        min.next = max_head.next
        
        return min_head.next
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
result = sol.partition(node1, 3)
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


print("Resultado después de la partición:")
print_linked_list(result)