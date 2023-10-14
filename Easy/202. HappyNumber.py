"""
202. Happy Number
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

class Solution:
    def isHappy(self, n):
        # define a function to calculate the sum of the squares of the digits of a number
        def get_next(n):
            total_sum = 0
            while n > 0:
                # get the last digit of n 
                digit = n % 10
                # add the square of the digit to the total sum
                total_sum = total_sum + digit ** 2
                # remove the last from n 
                n = n // 10
            return total_sum
        

        # create a set to keep track of seen numbers to detect cycles
        seen = set()

        # continue looping until we find a happy number (n becomes 1) or detect a cycle
        while n != 1:
            if n in seen:
                return False # cycle detected it's not a happy number
            seen.add(n)
            n = get_next(n)

        return True # if we reach here, n is 1, so it's a happy number
            
