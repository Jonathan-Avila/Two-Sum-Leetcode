from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        dict_of_chars = dict(Counter(s))
        list_of_chars = []
        
        for key, value in dict_of_chars.items():
            if value == 1:
                list_of_chars.append(key)
                
        for index, element in enumerate(s):
            if element in list_of_chars:
                return index
        return -1
        
        
                
            
        
        
