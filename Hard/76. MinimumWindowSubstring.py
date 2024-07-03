"""
76. Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
"""


class Solution:
    def minWindow(self, s, t):
        if t == "":
            return ""

        # count the character in string t
        charCountT, charCountWindow = {}, {}

        for char in t:
            charCountT[char] = 1 + charCountT.get(char, 0)

        charsMatched, charsNeeded = 0, len(charCountT)
        result, minWindowLength = [-1, -1], float("inf")
        leftPointer = 0

        for rightPointer in range(len(s)):
            currentChar = s[rightPointer]
            charCountWindow[currentChar] = 1 + charCountWindow.get(currentChar, 0)

            # check if the current character is in string t and if we've found all required occurences
            if (
                currentChar in charCountT
                and charCountWindow[currentChar] == charCountT[currentChar]
            ):
                charsMatched += 1

            # try to minimize the window by moving the left pointer
            while charsMatched == charsNeeded:
                # update the result if the current window is smaller
                if (rightPointer - leftPointer + 1) < minWindowLength:
                    result = [leftPointer, rightPointer]
                    minWindowLength = rightPointer - leftPointer + 1
                # remove characters from the left of the window
                charCountWindow[s[leftPointer]] -= 1
                if (
                    s[leftPointer] in charCountT
                    and charCountWindow[s[leftPointer]] < charCountT[s[leftPointer]]
                ):
                    charsMatched -= 1
                leftPointer += 1

        left, right = result
        return s[left : right + 1] if minWindowLength != float("inf") else ""

