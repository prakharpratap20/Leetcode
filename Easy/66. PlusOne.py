"""
66. Plus One
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""

class Solution:
    def plusOne(self, digits):
        n = len(digits)
        carry = 1
        
        # iterate through the digits array from right to left 
        for i in range(n - 1, -1, -1):
            # add the carry to the current digit 
            sums = digits[i] + carry  
            
            # calculate the new digit value and update the carry 
            digits[i] = sums % 10
            carry = sums // 10
            
        # if there is still a carry after the loop, prepend it to the digits array
        if carry:
            digits.insert(0, carry)
            
        return digits