"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.
"""


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True


# Test cases
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))  # True
print(sol.isAnagram("rat", "car"))  # False
print(sol.isAnagram("listen", "silent"))  # True
print(sol.isAnagram("hello", "world"))  # False
print(sol.isAnagram("python", "typhon"))  # True
