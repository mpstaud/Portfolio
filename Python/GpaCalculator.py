import time
from operator import itemgetter

A = 4.00
A_minus = 3.67
B_plus = 3.33
B = 3.00
B_minus = 2.67
C_plus = 2.33
C = 2.00
C_minus = 1.67
D_plus = 1.33
D = 1.00
D_minus = 0.67
F = 1.00

grades = []


def quality_points(credit_hours, grade):
    result = credit_hours * grade
    return result


def enter_grades(course_code, credit_hours, grade):
    grades.append([course_code, credit_hours, grade])


for i in range(0, 1):

    course = input('Enter the course code: ')
    hours = int(input('Enter the credit hours for this course: '))
    letter_grade = input('Enter your letter grade: ')

    time.sleep(0.5)
    enter_grades(course, hours, letter_grade)
    print(grades)
    gColumn = list(map(itemgetter(2), grades))
    print(gColumn)
