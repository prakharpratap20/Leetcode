"""
108. Convert Sorted Array to Binary Search Tree
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):

        # If the 'nums' list is empty, return None
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        # Recursively build the left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])

        # If the 'nums' list has an odd number of elements, the right subtree
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

