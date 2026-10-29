/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode check=head;
        for(int i=0;i<k;i++){
            if(check==null){
                return head;
            }
            check=check.next;
        }
        ListNode current=head;
        ListNode prev=null;
        ListNode temp=null;
        for(int i=0;i<k;i++){
            temp=current.next;
            current.next=prev;
            prev=current;
            current=temp;
        }
        head.next=reverseKGroup(current,k);
        return prev;
    }
}