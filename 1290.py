# Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        i = 0
        another = head.next
        while another != None:
            i += 1
            another = another.next
        val = 0
        while head != None:
            val += head.val * 2**i
            i -= 1
            head = head.next
        return val
