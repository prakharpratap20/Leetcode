"""
190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.
"""

class Solution:
    def reverseBits(self, n):
        # initialize the result to 0
        result = 0

        # iterate through 32 bits
        for _ in range(32):
            # shift the result to the left to make space for the next bit 
            result <<= 1
            # get the least significant bit of n and add it to the result
            result |= n & 1
            # right shift n to move to the next bit 
            n >>= 1
        return result