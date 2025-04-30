class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        arrayl1 = []
        arrayl2 = []
        while l1:
            arrayl1.append(l1.val)
            l1 = l1.next
        while l2:
            arrayl2.append(l2.val)
            l2 = l2.next
        lenmax = max(len(arrayl1), len(arrayl2))
        result = []
        guardado = 0
        for i in range(lenmax):
            val1 = arrayl1[i] if i < len(arrayl1) else 0
            val2 = arrayl2[i] if i < len(arrayl2) else 0
            sum = val1 + val2 + guardado
            if sum >= 10:
                result.append(sum - 10)
                guardado =+1
            else:
                result.append(sum)
                guardado = 0
        if guardado > 0:
            result.append(guardado)
        return arraytoLinkedlist(result)
    
def arraytoLinkedlist(array):
    dummy = ListNode()
    current = dummy
    for number in array:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
sol = Solution()
r = sol.addTwoNumbers(l1, l2)
print(r)