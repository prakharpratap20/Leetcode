"""
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the
root node down to the nearest leaf node.
Note: A leaf is a node with no children.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Definition for a binary tree node.
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        queue = [(root, 1)]

        while queue:
            node, depth = queue.pop(0)

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0
