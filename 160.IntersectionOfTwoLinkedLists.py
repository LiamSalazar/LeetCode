class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        currentA = headA
        currentB = headB
        while currentA != currentB:
            currentA = currentA.next if currentA else headB
            currentB = currentB.next if currentB else headA
        return currentA
    
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        currentA = headA
        currentB = headB
        visited = set()
        while currentA:
            visited.add(currentA)
            currentA = currentA.next
        while currentB:
            if currentB in visited:
                return currentB
            currentB = currentB.next
        return None
    