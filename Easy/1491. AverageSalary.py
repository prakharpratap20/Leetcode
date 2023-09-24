"""
1491. Average Salary Excluding the Minimum and Maximum Salary
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
Return the average salary of employees excluding the minimum and maximum salary.
Answers within 10-5 of the actual answer will be accepted.
"""

class Solution:
    def average_salary(self, salary):
        salary.sort()
        salary = salary[1:-1]
        average_salary = sum(salary)/len(salary)
        return average_salary
