# Merge k Sorted Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        num_heap = []
        for linked_list in lists:
            while linked_list:
                heapq.heappush(num_heap, linked_list.val)
                linked_list = linked_list.next
        if len(num_heap) > 0:
            root = ListNode(heapq.heappop(num_heap))
            tail = root
            for _ in range(len(num_heap)):
                tail.next = ListNode(heapq.heappop(num_heap))
                tail = tail.next
            return root
        