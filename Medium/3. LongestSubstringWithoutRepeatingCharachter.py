"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest 
substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        maxLength = 0 
        charSet = set()
        left = 0

        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength
    


# Test case 1
s1 = "abcabcbb"
# Longest substring without repeating characters: "abc"
# Expected output: 3

# Test case 2
s2 = "bbbbb"
# Longest substring without repeating characters: "b"
# Expected output: 1

# Test case 3
s3 = "pwwkew"
# Longest substring without repeating characters: "wke"
# Expected output: 3

# Test case 4
s4 = "abcdefg"
# Longest substring without repeating characters: "abcdefg"
# Expected output: 7

# Test case 5
s5 = "aab"
# Longest substring without repeating characters: "ab"
# Expected output: 2

# Test case 6
s6 = ""
# Longest substring without repeating characters: ""
# Expected output: 0

# Test case 7
s7 = "abcdefghijklmnopqrstuvwxyz"
# Longest substring without repeating characters: "abcdefghijklmnopqrstuvwxyz"
# Expected output: 26

# Create an instance of Solution
solution = Solution()

print(solution.lengthOfLongestSubstring(s1))  # Output: 3
print(solution.lengthOfLongestSubstring(s2))  # Output: 1
print(solution.lengthOfLongestSubstring(s3))  # Output: 3
print(solution.lengthOfLongestSubstring(s4))  # Output: 7
print(solution.lengthOfLongestSubstring(s5))  # Output: 2
print(solution.lengthOfLongestSubstring(s6))  # Output: 0
print(solution.lengthOfLongestSubstring(s7))  # Output: 26
