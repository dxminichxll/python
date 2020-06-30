while True:
    analysisGrade = int(input("Grade for analysis /25:"))
    designGrade = int(input("Grade for design /25:"))
    implementationGrade = int(input("Grade for implementation /25:"))
    evaluationGrade = int(input("Grade for evaluation /25:"))

    if analysisGrade > 25 or designGrade > 25 or implementationGrade > 25 or evaluationGrade > 25:
        print('Those grades aren\'t possible, try again')
    else:
        break

totalMarks = analysisGrade + designGrade + implementationGrade + evaluationGrade
print("\nYour total marks are", totalMarks)

gradeU = 1
grade1 = 2
grade2 = 4
grade3 = 13
grade4 = 22
grade5 = 31
grade6 = 41
grade7 = 54
grade8 = 67
grade9 = 80

if totalMarks >= grade9:
    grade = 9
elif grade9 > totalMarks >= grade8:
    grade = 8
    nextGrade = 80
elif grade8 > totalMarks >= grade7:
    grade = 7
    nextGrade = 67
elif grade7 > totalMarks >= grade6:
    grade = 6
    nextGrade = 54
elif grade6 > totalMarks >= grade5:
    grade = 5
    nextGrade = 41
elif grade5 > totalMarks >= grade4:
    grade = 4
    nextGrade = 31
elif grade4 > totalMarks >= grade3:
    grade = 3
    nextGrade = 22
elif grade3 > totalMarks >= grade2:
    grade = 2
    nextGrade = 12
elif grade2 > totalMarks >= grade1:
    grade = 1
    nextGrade = 4
elif totalMarks <= gradeU:
    grade = 'U'
    nextGrade = 2

print("Your final grade is a", grade)
if grade == 9:
    print("You got the highest grade")
else:
    print("You needed", nextGrade - totalMarks, "more marks to get a", grade + 1)
