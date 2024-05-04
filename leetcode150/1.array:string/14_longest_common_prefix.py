"""
Write a function to find the longest common prefix 
string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs):
        if not str:
            return ""

        strs.sort()

        first_str = strs[0]
        last_str = strs[-1]

        prefix = ""
        for i in range(len(first_str)):
            if first_str[i] == last_str[i]:
                prefix += first_str[i]
            else:
                break

        return prefix


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
