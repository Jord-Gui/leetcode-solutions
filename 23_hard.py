# Merge k Sorted Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            list0 = lists.pop(0)
            list1 = lists.pop(0)
            if list0 and list1:
                mergedList = self.mergeLists(list0, list1)
                lists.append(mergedList)
            elif list0:
                lists.append(list0)
            elif list1:
                lists.append(list1)
        return lists[0] if len(lists) > 0 else None
    
    def mergeLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        newList = None
        
        # set base case of new list
        if list1.val < list2.val:
            newList = ListNode(list1.val)
            list1 = list1.next
        else:
            newList = ListNode(list2.val)
            list2 = list2.next
            
        pointer = newList
            
        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = ListNode(list1.val)
                pointer = pointer.next
                list1 = list1.next
            else:
                pointer.next = ListNode(list2.val)
                pointer = pointer.next
                list2 = list2.next
                
        if list1:
            pointer.next = list1
        elif list2:
            pointer.next = list2
        
        return newList
        