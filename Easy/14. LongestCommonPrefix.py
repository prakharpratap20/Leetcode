"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs):
        # if the input list is empty, return an empty string 
        if not strs:
            return ""

        prefix = ""
        n = len(strs[0])

        # loop through each charachter position in the first string 
        for i in range(n):
            # get the charachter at the current position in the first string 
            char = strs[0][i]
            
            # compare the charachter with the same position in the other string 
            for j in range (1, len(strs)):
                # If the current string is shorter than the first string or
                # if the character at the current position doesn't match,
                # return the current common prefix found so far
                if i >= len(strs[j]) or strs[j][i] != char:
                    return prefix

            prefix += char
        
        return prefix
    
# there is an alternative solution to this problem which gives better runtime 

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        min_len = min(len(s) for s in strs)
        low = 0
        high = min_len
        
        while low < high:
            mid = (low + high + 1) // 2
            prefix = strs[0][:mid]
            
            if all(s.startswith(prefix) for s in strs):
                low = mid
            else:
                high = mid - 1
                
        return strs[0][:low]