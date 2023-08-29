"""28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack."""

class Solution:
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)
        
        # if needle is empty string, it is always present in the haystack at index 0
        if m == 0:
            return 0
        
        # iterate through the haystack using a sliding window of size equal to length of needle 
        for i in range(n-m+1):
            # check if the window (substring of haystack) is equal to the needle 
            if haystack[i:i + m] == needle:
                return i
            
        # if needle is not found in haystack return -1