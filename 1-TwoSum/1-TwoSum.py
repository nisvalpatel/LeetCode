# Last updated: 7/10/2025, 11:58:29 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for x in nums:
            if target - x in lst:
                return(len(lst), lst.index(target-x))
            lst.append(x)