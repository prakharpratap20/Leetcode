"""
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Given a roman numeral, convert it to an integer.
"""

class Solution:
    def romanToInt(self, s:str) ->int :
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        
        for char in s[::-1]:
            value = roman_values[char]
            if value < prev_value:
                total -= value
            else: 
                total += value 
            
            prev_value = value
            
        return total
                
# an alternative approach to solving this problem

class Solution:
    def romanToInt(self, s):
        total = 0
        prev_value = 0
        
        for char in s[::-1]:
            if char == "I":
                value = 1
            elif char == 'V':
                value = 5
            elif char == 'X':
                value = 10
            elif char == 'L':
                value = 50
            elif char == 'C':
                value = 100
            elif char == 'D':
                value = 500
            elif char == 'M':
                value = 1000
            else:
                return 0  # Invalid character
            
            if value < prev_value:
                total -= value
            else:
                total += value
            
            prev_value = value
        
        return total