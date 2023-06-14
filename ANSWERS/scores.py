scores_by_student = {}

with open("../DATA/testscores.dat") as scores_in:

    for line in scores_in:
        name, score = line.split(":")
        score = int(score)
        scores_by_student[name] = score

def calculate_grade(score):
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'
    return grade

for student, score in scores_by_student.items():
    grade = calculate_grade(score)
    print("{:20s} {} {}".format(student, score, grade))

sum_of_scores = sum(scores_by_student.values())
average = sum_of_scores/len(scores_by_student)
print("\naverage score is  {:.2f}\n".format(average))
