"""
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # Initialize an array to store the number of ways to reach each step
        dp = [0] * (n+1)
        # There is only one way to reach step 0 (base case)
        dp[0] = 1
        # There is only one way to reach step 1 (base case)
        dp[1] = 1

        # calculate the number of ways to reach each step up to n 
        for i in range(2, n+1):
            # the number of ways to reach step i is the sum of ways to reach steps(i -1) and (i-2)
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]