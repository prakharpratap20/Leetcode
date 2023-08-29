"""
7. Add Binary
Given two binary strings a and b, return their sum as a binary string.
"""

class Solution:
    def addBinary(self, a, b):
        result = []
        carry = 0 
        i = len(a) - 1
        j = len(b) - 1
        
        # iterate through both binary strings form right to left
        while i >= 0 or j >= 0 or carry:
            # get the integer value of the current bit in both strings (or 0 if index is out of range)
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # perform binary addition for the current bit and the carry from the previous addition 
            sum_ = bit_a + bit_b + carry
            
            # calculate the new bit value and update the carry 
            result.append(str(sum_ % 2))
            carry = sum_ // 2
            
            # move the indices to the left
            i -= 1
            j -= 1
            
        # reverse the return list to get the correct order of the bits
        return "".join(result[::-1])