# Last updated: 7/10/2025, 3:19:00 PM
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        """
        My solution: I think one way to solve this is by doing a recursive function so it changes the value of 
        the function. I think I will need to store the value of the starting somewhere. I will try implementing 
        the recursive solution to see if it works. I don't think a for loop or a while loop work as we don't 
        till when to continue.
        """
        #defining the function right now
        def recFunction(x, y):
            if x < 0 or x >= Rows or y < 0 or y >= Columns:
                return
            if image[x][y] != initColor:
                return
            image[x][y] = color
            recFunction(x + 1, y)
            recFunction(x - 1, y)
            recFunction(x, y+1)
            recFunction(x, y-1)

        Rows = len(image)
        Columns = len(image[0])
        initColor = image[sr][sc]
        if initColor == color:
            return image
        
        recFunction(sr,sc)
        return image
        
        

        
        