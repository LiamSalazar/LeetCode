def removeElement(nums, val):
    for element in nums:
        if nums[element] == val:
            nums.remove(element)
    for i in range(0, element, 1):
        nums.append('_')
    k = len(nums) - (i+1)
    print(k, ", nums = ", nums, sep='')



nums = [0,1,2,2,3,0,4,2]
val = 2
removeElement(nums, val)