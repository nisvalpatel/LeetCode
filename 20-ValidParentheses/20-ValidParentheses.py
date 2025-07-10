# Last updated: 7/10/2025, 11:58:25 AM
class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        mapping = {")": "(", "}": "{", "]": "["}  

        for x in s:
            if x in mapping.values(): 
                temp.append(x)
            elif not temp or temp[-1] != mapping[x]:  
                return False
            else:
                temp.pop()  

        return not temp  


