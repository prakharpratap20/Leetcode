"""
Given an array of strings words and a width maxWidth, 
format the text such that each line has exactly maxWidth characters 
and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words 
as you can in each line. Pad extra spaces ' ' when necessary so that each 
line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible.
 If the number of spaces on a line does not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on 
the right.
For the last line of text, it should be left-justified, and no extra space is inserted between words.
Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
"""


class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                extra_space = maxWidth - length
                spaces = extra_space // max(1, len(line)-1)
                remainder = extra_space % max(1, len(line)-1)

                for j in range(max(1, len(line)-1)):
                    line[j] += " "*spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1

                result.append("".join(line))
                length = 0
                line = []

            line.append(words[i])
            length += len(words[i])
            i += 1

        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        result.append(last_line + " "*trail_space)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.fullJustify(["This", "is", "an", "example",
          "of", "text", "justification."], 16))
