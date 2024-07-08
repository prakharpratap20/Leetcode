"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection
between a letter in pattern and a non-empty word in s.
"""


class Solution:
    def wordPattern(self, pattern, s):
        map1, map2 = [], []
        s = s.split()

        for i in pattern:
            map1.append(pattern.index(i))
        for i in s:
            map2.append(s.index(i))
        if map1 == map2:
            return True

        return False


sol = Solution()
print(sol.wordPattern("abba", "dog cat cat dog"))  # Output: True

sol = Solution()
print(sol.wordPattern("abba", "dog cat cat fish"))  # Output: False

sol = Solution()
print(sol.wordPattern("aaaa", "dog dog dog dog"))  # Output: True
