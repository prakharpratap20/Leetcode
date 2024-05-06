"""
You are given a string s and an array of strings words. 
All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings 
of any permutation of words concatenated.
For example, if words = ["ab","cd","ef"], 
then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are 
all concatenated strings. "acdbef" is not a concatenated string because 
it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings 
in s. You can return the answer in any order.
"""

from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words):
        length = len(words[0])
        word_count = Counter(words)
        indexes = []

        for i in range(length):
            start = i
            window = defaultdict(int)
            words_used = 0

            for j in range(i, len(s)-length+1, length):
                word = s[j:j+length]

                if word not in word_count:
                    start = j + length
                    window = defaultdict(int)
                    words_used = 0
                    continue

                words_used += 1
                window[word] += 1

                while window[word] > word_count[word]:
                    window[s[start:start + length]] -= 1
                    start += length
                    words_used -= 1

                if words_used == len(words):
                    indexes.append(start)

        return indexes


if __name__ == "__main__":
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
