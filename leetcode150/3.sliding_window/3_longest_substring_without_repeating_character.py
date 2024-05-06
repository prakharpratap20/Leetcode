"""
Given a string s, find the length of the longest 
substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
