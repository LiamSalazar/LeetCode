class TrieTree(object):    
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
    

class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        trie = TrieTree()
        for num in arr1:
            current_node = trie
            for digit in str(num):
                if digit not in current_node.children:
                    current_node.children[digit] = TrieTree()
                current_node = current_node.children[digit]
            current_node.is_end_of_word = True 
        #Imprimir por nivel
        for digit, child in trie.children.items():
            print(f"Digit: {digit}, Children: {child.children.keys()}, Is End of Word: {child.is_end_of_word}")
    


arr1 = [1,10,100, 2, 20]
arr2 = [1000]
solution = Solution()  
print(solution.longestCommonPrefix(arr1, arr2))
