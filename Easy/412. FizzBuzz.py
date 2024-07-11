"""
412. Fizz Buzz
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""


class Solution:
    def fizzBuzz(self, n):
        d = {3: "Fizz", 5: "Buzz"}
        return [''.join([d[k] for k in d if i % k == 0]) or str(i) for i in range(1, n+1)]

