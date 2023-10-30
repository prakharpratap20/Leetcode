"""
1269. Number of Ways to Stay in the Same Place After Some Steps
You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 
1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).
Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. 
Since the answer may be too large, return it modulo 109 + 7
"""

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # determine the maximum number of positions that can be reached
        n = min(steps // 2 + 1, arrLen)

        # create a 2D dynamic programming array dp
        dp = [[0] * n for _ in range(steps+1)]

        # initialize the starting position with 1 way
        dp[0][0] = 1
        mod = 10 ** 9 + 7 # define a constant for modulo operation

        # fill in the dp array using dynamic programming
        for i in range(1, steps+1):
            for j in range(n):
                dp[i][j] = dp[i-1][j] # carry over ways from the previous step
                if j > 0:
                    dp[i][j] += dp[i-1][j-1] # add ways from the previous step, moving one position left
                if j < n - 1:
                    dp[i][j] += dp[i-1][j+1] # add ways from the previous step, moving one position right

        # return the number of ways to reach position 0 after "steps" steps, modulo "mod"
        return dp[steps][0] % mod