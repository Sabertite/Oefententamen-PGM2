def Passed_students(L):
    
    return [[student[0], student[1] + 0.5] for student in L if student[2] is True]

print(Passed_students([
    ["0308230", 7.6, True],
    ["8273927", 5.1, False],
    ["8234987", 6.4, False],
    ["2368612", 5.9, True],
    ["9731827", 3.2, False],
]))



