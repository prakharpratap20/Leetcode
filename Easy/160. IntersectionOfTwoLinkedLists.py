"""
160. Intersection of Two Linked Lists
Given heads of two singly linkedlists headA and headB,return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.
"""

#definition of singly linked list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None 

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None 
        
        pA = headA
        pB = headB

        while pA != pB:
            pA = pA.next if pA else pB
            pB = pB.next if pB else pA 

        return pA