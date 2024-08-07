"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum
of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""


class Solution:
    def isHappy(self, n):
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False

    def sumOfSquares(self, n):
        output = 0

        while n:
            digit = n % 10
            digit = digit**2
            output += digit
            n = n // 10
        return output


# Test cases
sol = Solution()
print(sol.isHappy(19))  # True
print(sol.isHappy(2))  # False
print(sol.isHappy(7))  # True
print(sol.isHappy(111))  # False
print(sol.isHappy(82))  # True
