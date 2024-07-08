"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character
while preserving the order of characters. No two characters may map to the
same character, but a character may map to itself.
"""


class Solution:
    def isIsomorphic(self, s, t):
        s_map, t_map = {}, {}

        for c1, c2 in zip(s, t):
            if (c1 in s_map and s_map[c1] != c2) or (c2 in t_map and t_map[c2] != c1):
                return False
            s_map[c1] = c2
            t_map[c2] = c1

        return True


sol = Solution()
print(sol.isIsomorphic("egg", "add"))  # Output: True

sol = Solution()
print(sol.isIsomorphic("foo", "bar"))  # Output: False

sol = Solution()
print(sol.isIsomorphic("paper", "title"))  # Output: True
