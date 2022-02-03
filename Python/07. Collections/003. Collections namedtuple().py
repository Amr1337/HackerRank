# Problem: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Score: 20


from collections import namedtuple
students_number = int(input())
students = namedtuple("student", input())
total = 0
for i in range(students_number):
    student = students(*input().split())
    total += int(student.MARKS)
print('{:.2f}'.format(total/students_number))
