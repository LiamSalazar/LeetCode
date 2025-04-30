class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        if not head or not head.next:
            return head  
        current = head.next  
        head.next = None  
        while current:
            next_node = current.next  
            eval = head  
            if current.val < head.val:
                current.next = head
                head = current
            else:
                while eval.next and eval.next.val < current.val:
                    eval = eval.next
                current.next = eval.next
                eval.next = current
            current = next_node
        return head  
