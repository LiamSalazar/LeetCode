class Solution(object):
    def containsDuplicate(self, nums):
        group = set()
        for num in nums:
            if num in group:
                return True
            else:
                group.add(num)
        return False