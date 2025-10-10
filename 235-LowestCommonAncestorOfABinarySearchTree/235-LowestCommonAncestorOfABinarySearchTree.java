// Last updated: 10/9/2025, 8:10:46 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        while (true){
            if (root.val > p.val && root.val > q.val){
                root = root.left;
                ;
            } else if (root.val < p.val && root.val < q.val){
                root = root.right;
            } else{
                return root;
            }
        }
    }
}