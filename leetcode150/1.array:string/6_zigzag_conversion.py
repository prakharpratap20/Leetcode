"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a
given number of rows like this: (you may want to display this
pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given
a number of rows:
string convert(string s, int numRows);
"""


class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s

        rows = ["" for _ in range(numRows)]
        index, step = 0, 1

        for c in s:
            rows[index] += c
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return "".join(rows)


if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 3))
