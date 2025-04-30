class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        current = head
        nums = []
        while current:
            nums.append(current.val)
            current = current.next
        half = len(nums) // 2
        secondHalf = nums[half:]
        firstHalf = nums[:half][::-1]
        current = head
        count = 1
        while current:
            if count % 2 == 0 or firstHalf == []:
                current.val = secondHalf.pop()
            else:
                current.val = firstHalf.pop()
            count += 1
            current = current.next
        return head
