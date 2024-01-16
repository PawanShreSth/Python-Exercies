"""
Create a Python program that performs various string manipulations. 

Prompt the user to enter a sentence.
Display the length of the entered sentence.
Convert the sentence to uppercase and display the result.
Count the number of vowels in the sentence (consider both uppercase and lowercase vowels).
Check if the sentence is a palindrome (reads the same backward as forward) and display the result.

"""
#user_input = input("Enter any sentence: ")

from question3Utils import get_length_of_prompt, uppercase_prompt, vowel_occurrence, is_Palindrome


def question3(str):
    print(f"Length of the entered sentence: {get_length_of_prompt(str)}")

    print(f"Uppercase: {uppercase_prompt(str)}")

    print(f"Vowel Occurrence: {vowel_occurrence(str)}")

    print("Sentence is Palindrome" if is_Palindrome(str) else "Sentence is not Plaindrome")


question3(input("Enter any sentence: "))