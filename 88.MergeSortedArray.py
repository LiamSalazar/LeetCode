def merge(nums1, nums2, m, n):
    lastmerge0 = m + n 
    for i in range (m, lastmerge0, 1):
        nums1[i] = nums2[i-m]
    nums1.sort()

# Caso de prueba 1:
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
merge(nums1, nums2, m, n)
print(nums1)  # Salida esperada: [1, 2, 2, 3, 5, 6]
# Caso de prueba 2:
nums1 = [1] 
m = 1 
nums2 = []
n = 0
merge(nums1, nums2, m, n)
print(nums1)  # Salida esperada: [1]
# Caso de prueba 3:
nums1 = [0] 
m = 0 
nums2 = [1]
n = 1
merge(nums1, nums2, m, n)
print(nums1)  # Salida esperada: [1]