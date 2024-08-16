"""
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).
"""


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):

        # Helper function to check if two trees are mirrors of each other
        def isMirror(left, right):
            # If both 'left' and 'right' are None, return True
            if not left and not right:
                return True
            # If either 'left' or 'right' is None, return
            if not left or not right:
                return False

            # Check if the values of 'left' and 'right' are equal
            return left.val == right.val and isMirror(
                left.left, right.right) and isMirror(left.right, right.left)

        # If the 'root' is None, return True
        if not root:
            return True

        # Return the result of the helper function
        return isMirror(root.left, root.right)
