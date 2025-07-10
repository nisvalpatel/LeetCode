# Last updated: 7/10/2025, 11:58:18 AM
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        s = s.lower()
        new_string = [char for char in s if char in alphabet_list]
        x = 0
        y = len(new_string) - 1

        while y > x:
            if new_string[x] != new_string[y]:
                return False
            y -= 1
            x += 1

        return True
            