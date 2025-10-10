# Last updated: 10/9/2025, 8:10:40 PM
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]

        """
        res = []
        resmap = {}
        if not mat:
            return []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j in resmap:
                    resmap[i + j].append(mat[i][j])
                else:
                    resmap[i+j] = [mat[i][j]]
        count = 0
        for values in resmap.values():
            if count % 2 != 0:
                res += (values)
            else:
                res += (values[::-1])
            count += 1
        return res