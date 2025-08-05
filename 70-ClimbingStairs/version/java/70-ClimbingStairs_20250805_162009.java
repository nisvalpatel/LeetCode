// Last updated: 8/5/2025, 4:20:09 PM
class Solution {
    public int climbStairs(int n) {
        if (n== 0 || n == 1){return 1;}
        int twoAgo = 1;
        int oneAgo = 1;
        int temp;
        for (int i = 0; i < n-1; i++){
            temp = oneAgo;
            oneAgo = oneAgo + twoAgo;
            twoAgo = temp;
        }
        
        return oneAgo;

    }
}