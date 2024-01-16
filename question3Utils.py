# Method that simply returns the lenght of the string
def get_length_of_prompt(str):
    return len(str)



#Method that converts the passed argument to uppercase string
def uppercase_prompt(str):
    return str.upper()



#Method that counts the occurrence of vowel letter in the passed argument
def vowel_occurrence(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    vowel_occurrence_in_total = 0

    for i in range(len(str)):
        if (str[i] in vowels):
            vowel_occurrence_in_total += 1
    
    return vowel_occurrence_in_total



# Method that returns true if string is palindrome
def is_Palindrome(str):
    original_string = str.lower()
    reversed_string = str[::-1].lower()

    if (original_string == reversed_string): return True

    return False