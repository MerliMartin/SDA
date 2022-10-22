#  implement a function that takes student score and tells their grade.
# use the scale in this description in the link
# https://www.studyineurope.eu/study-in-estonia/grades
# i.e below 40 is "Fail"
# Note as an exception: if student is below 40 and has medical condition then return "Pass" result
def student_grade(score):
    score = float(score)
    if 91 <= score >= 100:
        result = "A"
    elif 81 <= score >= 90:
        result = "B"
    elif 71 <= score >= 80:
        result = "C"
    elif 61 <= score >= 70:
        result = "D"
    # In the link the min score was 50, but in this task it is 40
    # Below 40 the result is Fail
    elif 40 <= score >= 60:
        result = "F"
    else:
        student_medical_condition = input("Do you have a medical condition?(yes/no): ")
        if student_medical_condition == "yes":
            result = "Pass"
        else:
            result = "Fail"
    return result


student_score = input("Please insert your test score: ")
student_result = student_grade(student_score)
print(student_result)
