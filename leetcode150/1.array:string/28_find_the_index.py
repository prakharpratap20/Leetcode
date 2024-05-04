"""
Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i

        return -1


if __name__ == "__main__":
    print(Solution().strStr("hello", "ll"))
