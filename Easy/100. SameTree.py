"""
100. Same Tree
Given the roots of two binary trees p and q,
write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        # If both 'p' and 'q' are None, return True
        if not p and not q:
            return True
        # If either 'p' or 'q' is None, return False
        if not p or not q:
            return False
        # If the values of 'p' and 'q' are not equal, return False
        if p.val != q.val:
            return False

        # Recursively check the left and right subtrees of 'p' and 'q'
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
