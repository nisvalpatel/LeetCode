# Last updated: 7/10/2025, 11:58:19 AM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowel_list = ["a", "e", "i", "o", "u"]
        window_start = 0
        window_end = 0
        loop_count = k
        temp = 0
        # the following part will check if k is greater than the len(s) or not
        if k > len(s):
            return sum(1 for char in s if char in vowel_list)
        #this loop just loops to get the size of the window before sliding the window
        for x in range(loop_count):
            if s[x] in vowel_list:
                count += 1
            window_end += 1

        #just updated the max_count with the current count since its prob bigger than max_count
        max_count = count

        while window_end < len(s):      #change this up but subtracting two makes sense
            if s[window_start] in vowel_list:
                count -= 1
            window_start += 1    
            if s[window_end] in vowel_list:
                count += 1    
            window_end += 1

            
            max_count = max(max_count, count)
        
        return max_count






        