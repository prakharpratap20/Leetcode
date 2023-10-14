"""
191. Number of 1 Bits
Write a function that takes the binary representation of an unsigned integer and
returns the number of '1' bits it has (also known as the Hamming weight).
"""

class Solution:
    def hammingWeight(self, n):
        count = 0

        while n > 0:
            # check if the least significant bit is "1"
            if n & 1 == 1:
                count += 1
            # right shift the number to check the next bit 
            n >>= 1
        return count
