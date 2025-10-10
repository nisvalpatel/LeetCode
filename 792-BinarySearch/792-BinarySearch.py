# Last updated: 10/9/2025, 8:10:39 PM
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        """
        My Solution: See you easily achieve this in O(n) time by simply parsing through the list
        but we can implement faster algorithm by treating the middle of the list as a root. And
        then splitting it into multiple halves and treating the middle of those as roots. This way,
        I don't have to go through the entire list

        Results: My algorithm beat 100% for runtime complexity so wooooooo. It also beat 62.93% 
        for the memory which is also pretty good. I think the algorithm was good but I can 
        def improve the memory for this problem. 

        Optimal Solution: They used the same algorithm so WWWWWWW and I am not too worried about 
        the memory not going to lie.
        """
        
        start = 0
        end = len(nums) - 1
        while end >= start:
            if end == start and nums[end] == target:
                return end
            temp = ((end - start) / 2) + start
            if nums[temp] == target:
                return temp
            elif nums[temp] > target:
                end = temp - 1
            else: 
                start = temp + 1
        return -1