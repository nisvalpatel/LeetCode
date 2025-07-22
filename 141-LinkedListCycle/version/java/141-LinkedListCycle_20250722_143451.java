// Last updated: 7/22/2025, 2:34:51 PM
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null){return false;}
        ListNode fastPointer = head;
        ListNode slowPointer = head;
        
        while (true){
            for (int i = 0; i < 2; i++){
                if (fastPointer.next == null){
                    return false;
                }
                fastPointer = fastPointer.next;
            }
            slowPointer = slowPointer.next;
            if (slowPointer == fastPointer){return true;}
        }
    }
}