"""
168. Excel Sheet Column Title
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
"""

class Solution:
    def convertToTitle(self, columnNumber):
        result = ""

        while columnNumber > 0:
            columnNumber -= 1 # Adjust columnNumber to make "A" correspond to 0, "B" to 1, etc.
            quotient, remainder = divmod(columnNumber, 26) # calculate quotient and remainder
            result = chr(65 + remainder) + result # Convert remainder to a character and append to the result
            columnNumber = quotient # update columnNumber with the quotient
        return result