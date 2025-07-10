# Last updated: 7/10/2025, 11:58:23 AM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for words in strs:
            key = tuple(sorted(words))
            if key not in hashmap.keys():
                hashmap[key] = []
            
            hashmap[key].append(words)
        return list(hashmap.values())