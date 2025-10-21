class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        next = {}         
        stack = []    
        for x in nums2:
            while stack and stack[-1] < x:
                prev = stack.pop()
                next[prev] = x
            stack.append(x)
        return [next.get(v, -1) for v in nums1]


s = Solution()
print(s.nextGreaterElement([4,1,2], [1,3,4,2]))  # [-1, 3, -1]
print(s.nextGreaterElement([2,4], [1,2,3,4]))  # [3,-1]
