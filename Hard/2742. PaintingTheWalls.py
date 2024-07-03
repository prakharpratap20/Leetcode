"""
2742. Painting the Walls
You are given two 0-indexed integer arrays, cost and time, of size n representing the costs and the
time taken to paint n different walls respectively. There are two painters available:
A paid painter that paints the ith wall in time[i] units of time and takes cost[i] units of money.
A free painter that paints any wall in 1 unit of time at a cost of 0.
But the free painter can only be used if the paid painter is already occupied.
Return the minimum amount of money required to paint the n walls.
"""


class Solution:
    def paintWalls(self, cost, time):
        # calculate postfix times, i.e, the cumulative time to paint walls
        # from the current wall to the last wall
        postfix_times = time.copy()
        for i in range(len(postfix_times) - 2, -1, -1):
            postfix_times[i] += postfix_times[i + 1]

        # create a dictionary to store previously calculated results
        visited = {}

        def dp(index, time_painted):
            if index == len(cost):
                # base case: all wall are painted
                # if there is still positive time_painted, return 0
                # otherwise return infinity
                return 0 if time_painted >= 0 else float("inf")

            if time_painted >= len(cost) - index:
                # base case: we have more time than walls left to paint
                # return 0 as we can use the free painter
                return 0

            if time_painted + postfix_times[index] < 0:
                # if the cumulative time required for the remaining walls is
                # more than available time, return inifinity
                return float("inf")

            if (index, time_painted) in visited:
                # if we have already calculate this state, return the cached result
                return visited[(index, time_painted)]

            # recursive step calculate the minimum cost for current state
            visited[(index, time_painted)] = min(
                dp(index + 1, time_painted - 1),  # paint with the paid painter
                cost[index]
                + dp(
                    index + 1, time_painted + time[index]
                ),  # pain wtih the free painter
            )
            return visited[(index, time_painted)]

        # start dynamic programming
        return dp(0, 0)

