"""
9. Palindrome Number
Given an integer x, return true if x is a palindrome and false otherwise.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
    # Convert the integer to a string
        x_str = str(x)
        
        # Compare the string with its reverse
        if x_str == x_str[::-1]:
            return True
        else:
            return False