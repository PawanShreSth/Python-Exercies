# Method to check if grade is an integer and is between 0 and 100.
def validate_grade(grade):
    grade = int(grade)
    if (str(type(grade)) != "<class 'int'>"): return False

    if (grade < 0 or grade > 100): return False

    return True


# Get grade based on the number
def get_grade(grade):
    grade = int(grade)

    if (grade >= 90 and grade <= 100): 
        return 'A'
    elif (grade >= 80 and grade <= 89):
        return 'B'
    elif (grade >= 70 and grade <= 79):
        return 'C'
    elif (grade >= 60 and grade <= 69):
        return 'D'
    elif (grade >= 40 and grade <= 59):
        return 'E'
    else:
        return 'F'