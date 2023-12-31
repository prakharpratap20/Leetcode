"""
83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, 
delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        current = head

        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else :
                current = current.next

        return head

        