"""
171. Excel Sheet Column Number
Given a string columnTitle that represents the column title as appears in an Excel sheet,
return its corresponding column number.
"""

class Solution:
    def titleToNumber(self, columnTitle):
        columnNumber = 0
        for char in columnTitle:
            # convert the character to its corresponding number
            char_number = ord(char) - ord("A") + 1
            # update the column number by multiplying the previous number by 26
            # and adding the current characters number
            columnNumber = columnNumber * 26 + char_number

        return columnNumber