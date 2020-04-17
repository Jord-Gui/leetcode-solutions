// Remove Duplicates from Sorted List

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode dummy = new ListNode(head.val);
        ListNode l1 = dummy;
        while (head != null) {
            if (head.val != l1.val) {
                l1.next = new ListNode(head.val);
                l1 = l1.next;
            }
            head = head.next;
        }
        return dummy;
    }
}
