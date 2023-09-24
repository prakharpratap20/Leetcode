"""
119. Pascal's Triangle II
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

class Solution:
    def  getRow(self, rowIndex):
        if rowIndex < 0:
            return []
        
        row = [1] # intitializing the first row

        for i in range(1, rowIndex + 1):
            new_row = [1] # the first element of each row is always 1

            for j in range(1, len(row)):
                new_element = row[j-1] + row[j]
                new_row.append(new_element)

            new_row.append(1) # the last element of each row is always 1 
            row = new_row 

        return row 
