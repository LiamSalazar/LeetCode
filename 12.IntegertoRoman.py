class Solution(object):
    def intToRoman(self, num):
        # Declaraciones
        dictionary = {0:"", 1:"I", 5:"V", 10:"X", 50: "L", 100:"C", 500:"D", 1000:"M"}
        reversed_num = str(num)[::-1]
        unities = []
        roman = []
        i = 1
        # Creación de utilities
        for digit in reversed_num:
            unities.append(int(digit) * i)
            i *= 10
        #Construccion de cadena
        if len(unities) > 0 and unities[0] in dictionary:
            roman.append(dictionary[unities[0]])
        
        if len(unities) > 1 and unities[1] in dictionary:
            roman.append(dictionary[unities[1]])

        if len(unities) > 2 and unities[2] in dictionary:
            roman.append(dictionary[unities[2]])

        if len(unities) > 3 and unities[3] in dictionary:
            roman.append(dictionary[unities[3]])

        print(roman)
        
sol = Solution()
print(sol.intToRoman(51))
