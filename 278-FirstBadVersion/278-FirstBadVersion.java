// Last updated: 10/9/2025, 8:10:42 PM
/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {

    public int firstBadVersion(int n) {

        int front = 1;

        while (n > front){
            int middle = (n-front)/2 + front;

            if (isBadVersion(middle)){
                n = middle;
            } else{
                front = middle + 1;
            }
        }
        return n;        
    }
}