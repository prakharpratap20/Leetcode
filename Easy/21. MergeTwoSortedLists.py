"""
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together 
the nodes of the first two lists.
Return the head of the merged linked list.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy_head = ListNode()
        curr = dummy_head
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next 
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next 
            
        if list1:
            curr.next = list1 
        elif list2:
            curr.next = list2
        
        return dummy_head.next
            
            