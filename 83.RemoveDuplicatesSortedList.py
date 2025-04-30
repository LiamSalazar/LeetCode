class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        visited = []
        current = head
        while current is not None:
            if current.val not in visited:
                visited.append(current.val)
            current = current.next
        current = head
        for i in range(len(visited)):
            if i == len(visited) - 1:
                current.next = None
            current.val = visited[i]
            current = current.next
        return head

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sol = Solution()
r = sol.deleteDuplicates(node1)
print (r)