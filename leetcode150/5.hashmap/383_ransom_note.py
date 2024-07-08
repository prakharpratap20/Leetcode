"""
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the
letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""


class Solution:
    def canConstruct(self, ransomNote, magazine):
        mag_freq = {}

        for char in magazine:
            mag_freq[char] = mag_freq.get(char, 0) + 1

        for char in ransomNote:
            if char not in mag_freq or mag_freq[char] == 0:
                return False
            mag_freq[char] -= 1

        return True


sol = Solution()
print(sol.canConstruct("a", "b"))  # Output: False

sol = Solution()
print(sol.canConstruct("aa", "ab"))  # Output: False

sol = Solution()
print(sol.canConstruct("aa", "aab"))  # Output: True
