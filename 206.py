# Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        reverseList = ListNode(head.val)
        head = head.next
        while head != None:
            newNode = ListNode(head.val)
            newNode.next = reverseList
            reverseList = newNode
            head = head.next
        return reverseList
