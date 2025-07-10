# Last updated: 7/10/2025, 11:58:20 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def recursive_function(node):
            if root is None:
                return None
            
            swap(node)
            if node.left:
                recursive_function(node.left)
            if node.right:
                recursive_function(node.right) 
            

        def swap(node):
            temp = node.left
            node.left = node.right
            node.right = temp 

        recursive_function(root)
        return root
        