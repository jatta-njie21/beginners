
def total_marks(*args):

    total_mark_of_subjects = 0
    grades = []
    total_grades = 0

    for mark in args:
        total_mark_of_subjects += mark
        if mark >= 90:
            grades.append(4)
        elif mark >=80:
            grades.append(3)
        elif mark >= 70:
            grades.append(2)
        elif mark <= 69:
            grades.append(1)

        for grade in grades:
            total_grades += grade


    print("Marks obtained =",total_mark_of_subjects)

    print("Grades obtained =",total_grades)

    average = total_mark_of_subjects / len(args)

    print("average =",average)

    cgpa = (total_mark_of_subjects * total_grades) / total_grades

    print("cgpa =", cgpa)

total_marks(45,67,97,32,45,67,96,23,56,78,79)   
