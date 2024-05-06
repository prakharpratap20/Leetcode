"""
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character 
in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
"""


class Solution:
    def minWindow(self, s: str, t: str):
        if t == "":
            return ""

        charCountT, charCountWindow = {}, {}
        for c in t:
            charCountT[c] = 1 + charCountT.get(c, 0)

        charsMatched, charsNeeded = 0, len(charCountT)
        result, minWindowLength = [-1, 1], float("inf")
        leftPointer = 0

        for rightPointer in range(len(s)):
            currentChar = s[rightPointer]
            charCountWindow[currentChar] = 1 + \
                charCountWindow.get(currentChar, 0)

            if currentChar in charCountT and \
                    charCountT[currentChar] == charCountWindow[currentChar]:
                charsMatched += 1

            while charsMatched == charsNeeded:
                if (rightPointer - leftPointer + 1) < minWindowLength:
                    result = [leftPointer, rightPointer]
                    minWindowLength = (
                        rightPointer - leftPointer + 1)
                charCountWindow[s[leftPointer]] -= 1
                if s[leftPointer] in charCountT and \
                        charCountWindow[s[leftPointer]] < \
                        charCountT[s[leftPointer]]:
                    charsMatched -= 1
                leftPointer += 1

        left, right = result

        return s[left:right + 1] if minWindowLength != float("inf") else ""


if __name__ == "__main__":
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
