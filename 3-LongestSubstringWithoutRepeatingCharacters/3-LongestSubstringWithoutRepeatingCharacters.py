# Last updated: 7/10/2025, 11:58:26 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = ""
        high_score = 0
        for char in s:
            if char in sub_str:
                high_score = max(len(sub_str), high_score)
                sub_str = sub_str[sub_str.index(char) + 1:]
                sub_str += char
            else:
                sub_str += char

        high_score  = max(len(sub_str), high_score)
        return high_score

