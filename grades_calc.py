# Python Program - Calculate Grade

import csv


def mean(*args):
    """ returns average of variable number of arguments """
    if len(args) > 1:
        return sum(args) // len(args)
    else:
        return args[0]


def mark_percentage(mark1, mark2):
    """ return percentage average of variable number of arguments """
    return mark1 + mark2 * 100 / 150


def print_result(average, grade, mark1, mark2, name):
    """ output grade result and percentage """

    print(f"{name} Grade is {grade}, percentage: {(mark1+mark2)*100/150:.1f}%")


def check_result(average, mark1, mark2, name='Your'):
    """ determine grade for mark average and output result"""

    a_result = False
    grade = ''
    if average > 68:  # A is 69 to 99
        grade = 'A'
        a_result = True
    elif average > 59:  # B is 60 to 68
        grade = 'B'
    elif average > 49:  # C is 50 to 59
        grade = 'C'
    elif average > 44:  # D is 45 to 49
        grade = 'D'
    else:  # FAIL is 1 to 44
        grade = 'FAIL'

    print_result(average, grade, mark1, mark2, name)

    return a_result


def two_marks():
    """ prompt for two marks and generate result """
    print("Enter 2 marks: ")

    while True:
        try:
            mark1 = int(input("Enter first mark: "))
            mark2 = int(input("Enter second mark: "))
        except:
            print('Integers only please!')
            continue

        if mark1 > 0 and mark2 > 0 and mark1 < 61 and mark2 < 91:  # valid grades 1 - 60 for gr1 and 1 - 90 for gr2
            break
        else:
            print('Only positive integers please. Try again.')

    average = (mark1 + mark2) // 2
    check_result(average, mark1, mark2)


def check_student_results():
    """ output results for all students in file """

    def find_max(number_list):
        """ return largest number from list of numbers """
        largest = max(number_list)

        print(f"The highest mark is {largest}")

    marks = []

    a_count = 0

    with open("studentinfosamplee.csv", 'r') as studentInfo:  # you have double 'e' in the name. Is it a typo?
        studentList = csv.reader(studentInfo)
        for student in studentList:
            fullName = student[0]
            mark1 = int(student[1])
            mark2 = int(student[2])
            average = mean(mark1, mark2)
            marks.append(average)
            a_count += check_result(average, mark1, mark2, name=fullName)

    find_max(marks)
    print(f'{a_count} students gained an A')


if __name__ == "__main__":
    two_marks()
    check_student_results()  # keep in mind that your results are not part of the calculation
