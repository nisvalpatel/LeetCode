// Last updated: 10/9/2025, 8:10:45 PM
import java.util.HashMap;
class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int BestCount = 0;
        int BestKey = 0;
        for (int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i])){
                
                map.put(nums[i], map.get(nums[i])+ 1);
            }else{
                map.put(nums[i], 1);
            }
            if (map.get(nums[i])>BestCount){
                BestCount = map.get(nums[i]);
                BestKey = nums[i];
            }
        }
        return BestKey;
    }
}