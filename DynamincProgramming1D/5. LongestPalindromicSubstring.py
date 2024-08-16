class Solution:
    def longestPalindrome(self, s):
        res = ""
        resLen = 0

        # for each character in the string
        for i in range(len(s)):
            # odd length
            left, right = i, i
            # while left and right are within the bounds of the string and the characters at left and right are the same
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left: right + 1]
                    resLen = right - left + 1
                    left -= 1
                    right += 1

            # even length
            left, right = i, i + 1
            # while left and right are within the bounds of the string and the characters at left and right are the same
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left: right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1
            return res
