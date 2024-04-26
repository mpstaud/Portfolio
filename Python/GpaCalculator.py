import time
from operator import itemgetter

# quality point values for each grade
qPoints = {'A': 4.00, 'A-': 3.67, 'B+': 3.33, 'B': 3.00, 'B-': 2.67,
           'C+': 2.33, 'C': 2.00, 'C-': 1.67, 'D+': 1.33, 'D': 1.00,
           'F': 0.00}
# qPoints['A-'] will get the value for a letter grade
grades = []
total_points = []


def quality_points(credit_hours, grade):
    result = credit_hours * grade
    print(result)
    total_points.append(result)


def log_grades(course_code, credit_hours, grade):
    grades.append(grade)
    print(course_code, credit_hours, grade)


def run_entry():

    done = False

    while not done:

        # prompts user for course details
        course = input('Course Code: ')
        hours = int(input('Credits: '))
        letter_grade = input('Letter Grade: ')
        qp = qPoints.get(letter_grade)
        quality_points(hours, qp)
        # delay 0.5 seconds
        time.sleep(0.5)
        log_grades(course, hours, letter_grade)
        yn = input('Press C to enter another or D for done: ')
        if yn == 'D':
            done = True


run_entry()

print(sum(total_points))
