"""
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        def check_balance_and_height(node):
            # If the 'node' is None, return True and 0
            if not node:
                return True, 0
            left_balanced, left_height = check_balance_and_height(
                node.left)  # Recursively check the left subtree

            # If the left subtree is not balanced, return False and 0
            if not left_balanced:
                return False, 0
            right_balanced, right_height = check_balance_and_height(
                node.right)  # Recursively check the right subtree
            if not right_balanced:
                return False, 0

            # If the absolute difference between the heights of the left and right subtrees is greater than 1, return False and 0
            if abs(left_height - right_height) > 1:
                return False, 0
            return True, max(left_height, right_height) + 1

        return check_balance_and_height(root)[0]
