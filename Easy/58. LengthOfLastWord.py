"""
58. Length Of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""
class Solution:
    def lengthofLastWord(self, s):
        # remove any trailling spaces 
        s = s.strip()
        
        # create a variable to keep track of the last word's length 
        last_word_length = 0
        
        # iterate through the string from the end
        for i in range(len(s) - 1, -1, -1):
            # if we encounter a space we have reached the end of the last word
            if s[i] == ' ':
                break
            #otherwise increment the length of the last word
            last_word_length += 1
            
        return last_word_length