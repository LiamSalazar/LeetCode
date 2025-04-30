class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        list = []
        current = head
        while current:
            list.append(current.val)
            current = current.next
        list.sort()
        current = head
        i = 0
        while current:
            current.val = list[i]
            i += 1
            current = current.next
        return head