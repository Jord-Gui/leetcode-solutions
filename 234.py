# Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def reverseList(head: ListNode) -> ListNode:
#     reverseList = ListNode(head.val)
#     head = head.next
#     while head != None:
#         newNode = ListNode(head.val)
#         newNode.next = reverseList
#         reverseList = newNode
#         head = head.next
#     return reverseList
    
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         if head is None:
#             return True
#         reversedList = reverseList(head)
#         while reversedList != None and head != None:
#             if reversedList.val == head.val:
#                 reversedList = reversedList.next
#                 head = head.next
#             else:
#                 return False
#         return True
    
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        s=[]
        while head:
            s.append(head.val)
            head = head.next
        return s==s[::-1]
