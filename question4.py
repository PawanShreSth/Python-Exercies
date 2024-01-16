"""
Create a Python program that acts as a basic grade calculator. 
Prompt the user to enter a numerical score (0 to 100).

Use conditional statements (if, elif, else) to determine the corresponding letter grade based on the following scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
E: 40-59
	F: 0-39
Display both the numerical score entered by the user and the calculated letter grade.
Ensure your program handles edge cases (scores outside the 0-100 range) and provides meaningful feedback to the user.

"""

from question4Utils import validate_grade, get_grade

grade = input("Enter your score to know you grade (0-100): ")

def question4(grade):
    if (validate_grade(grade) == False):
        print("Please ensure that you have entered a number between 0 - 100! 🙃🙃")
        return

    print(f"You have entered {grade} which is equivalent to you securing Grade {get_grade(grade)}. 😊👍👍👍")

question4(grade)

    
