# Last updated: 7/10/2025, 11:58:20 AM
class Solution(object):
    def isAnagram(self, s, t):
        if (len(s)==len(t)):
            a=set(s)
            for i in a:
                if(s.count(i)!=t.count(i)):
                    return False 
            return True 

        return False