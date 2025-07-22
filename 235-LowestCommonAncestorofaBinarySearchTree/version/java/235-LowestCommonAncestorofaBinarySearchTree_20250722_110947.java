// Last updated: 7/22/2025, 11:09:47 AM
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
        boolean gurt = true;
        while (gurt){
            if (root.val > p.val && root.val > q.val){
                root = root.left;
                ;
            } else if (root.val < p.val && root.val < q.val){
                root = root.right;
            } else{
                gurt = false;
            }
        }

        return root;
    }
}