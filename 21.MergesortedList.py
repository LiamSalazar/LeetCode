class Solution(object):
    def mergeTwoLists(self, list1, list2):
        array1 = []
        array2 = []
        while list1:
            array1.append(list1.val)
            list1=list1.next
        while list2:
            array2.append(list2.val)
            list2 = list2.next
        array3 = array1 + array2
        array3.sort()
        return arraytoLinkedList(array3)
        
def arraytoLinkedList(array3):
    if not array3:
        return None
    else: 
        begin = ListNode(array3[0])
        current = begin
        for number in array3[1:]:
            current.next = ListNode(number)
            current = current.next
        return begin

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Prueba
list1 = [1, 3]
list2 = [2, 4]
list3 = list1 + list2
list3.sort()
print(list3)
print(list3)
sol = Solution()
r = sol.mergeTwoLists(list1, list2)
print(r)  