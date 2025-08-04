// Last updated: 8/4/2025, 4:30:30 PM
/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        // int ans = 0;
        // for(int i=1;i<=n;i++){
        //    if(isBadVersion(i)){
        //    ans=i;
        //    break;
        int l=0,r=n;
        int ans=0;
        while(l<=r){
        int mid=l+(r-l)/2;
            if(isBadVersion(mid)){
               ans=mid;
               r=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return ans;
    }
}