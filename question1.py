"""
Write a program that takes a string and returns the dictionary with each character as key and its count as value.
For example: 
String = "aaaaabbbbcccdde"
It should return { ’a’ : 5, ’b’ : 4, ’c’ : 3, ’d’ : 2, ’e’ : 1 }
"""


# Approach 1
def count_characters(str):
    unique_characters = list(set(str))
    characters_count = {}
    
    for i in range(len(unique_characters)):
        value = unique_characters[i]
        count = 0

        for j in range(len(str)):
            if (value == str[j]):
                count = count + 1

        characters_count[value] = count
    
    return characters_count
                
print(count_characters("Pawan Shrestha"))



# Approach 2
def count_characters_2(str):
    unique_characters = list(set(str))
    characters_count = {}

    for i in range(len(unique_characters)):
        characters_count[unique_characters[i]] = str.count(unique_characters[i])

    print(characters_count)

count_characters_2("Pawan Shrestha")



#Approach 3 (Using dictionary comprehension)
def count_characters_3(str):
    unique_characters = list(set(str))
    characters_count = { unique_characters[i] : str.count(unique_characters[i]) for i in range(len(unique_characters)) }

    print(characters_count)

count_characters_3("aaaccddehahahahahahaaabbbbc")