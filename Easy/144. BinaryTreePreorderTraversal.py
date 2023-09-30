"""
144. Binary Tree Preorder Traversal
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""
# Recursive Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 


class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        result = []

        def traverse(node):
            if node:
                result.append(node.val)
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return result
    
# Iterative Solution

def preorderTraversal(root):
    if not root:
        return []
    
    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # push right child first so that left child is processed first (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        
    return result 