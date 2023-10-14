"""
203. Remove Linked List Elements
Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        # create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        current = dummy 

        # iterate throguh the linked list
        while current.next:
            if current.next.val == val:
                # remove the node with the specified value
                current.next = current.next.next 
            else:
                # move to the next node
                current = current.next
        # return the updated head
        return dummy.next