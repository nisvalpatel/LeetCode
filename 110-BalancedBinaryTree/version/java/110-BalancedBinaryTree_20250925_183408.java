// Last updated: 9/25/2025, 6:34:08 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }i nu
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        int temp = recursionFunc(root);
        if (temp == -1){
            return false;
        }
        return true;
    }

    private int recursionFunc(TreeNode root){
        if (root == null){return 0;}
        // base case
        if (root.left == null && root.right == null){
            return 1;
        }

        int tempLeft = recursionFunc(root.left);
        int tempRight = recursionFunc(root.right);
        if (tempLeft == -1 || tempRight == -1 || Math.abs(tempRight - tempLeft) > 1 ){
            return -1;
        } else if (tempRight > tempLeft){
            return (tempRight + 1);
        } else{
            return (tempLeft + 1);
        }
    }
}