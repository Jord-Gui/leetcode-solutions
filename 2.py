# Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        acc = 0
        result = ListNode(0)
        l3 = result
        while l1 != None and l2 != None:
            l3.next = ListNode((l1.val + l2.val + acc)%10)
            acc = (l1.val + l2.val + acc) // 10
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        while l1 != None:
            l3.next = ListNode((l1.val + acc)%10)
            acc = (l1.val + acc) // 10
            l1 = l1.next
            l3 = l3.next
        while l2 != None:
            l3.next = ListNode((l2.val + acc)%10)
            acc = (l2.val + acc) // 10
            l2 = l2.next
            l3 = l3.next
        if acc > 0:
            l3.next = ListNode(acc)
        return result.next
