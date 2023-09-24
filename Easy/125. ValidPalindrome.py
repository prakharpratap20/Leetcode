"""
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and remove non-alphanumeric characters
        s = ''.join(char.lower() for char in s if char.isalnum())  # isalnum() allows to remove all non-alphanumric char

        # Compare the string with its reverse
        return s == s[::-1]
