recuStudents = []
with open("students.txt") as gradesFile:
    for line in gradesFile:
        student_grade = line
        student_grade = student_grade.split(" ")
        if int(student_grade[1]) < 6:
            recuStudents.append(student_grade[0] + "\n")

with open("recuStudents.txt", mode="w, r") as recuStudentsFile:
    recuStudentsFile.writelines(recuStudents)

with open("recuStudents.txt", mode='r') as studentsReprove:
    for students in studentsReprove:
        print(students)
