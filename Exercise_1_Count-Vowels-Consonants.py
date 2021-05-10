#Excersie 1: Vowel and Consonant Counter
"""
I want to know whether a character in a string is a vowel or a consonant

Topics
1. f-strings:
 are strings that have an "f" before the opening quote
 they're just like regular strings, but if there are {} inside of them,
 the {} are evaluated




"""
def main():
    count_vowel_consonant()


def count_vowel_consonant():
    print()
    word = input("Enter a word: ").lower()
    vowel_count = 0
    consonant_count = 0
    for char in word:
       # if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
        if (char in "aeiou"):
                vowel_count += 1
        else:
                consonant_count += 1
    #print("Vowels count: {}".format(vowel_count))
    #print("Consonants count: {}".format(consonant_count))
    print(f"Vowels count: {vowel_count}") #curly braces in f-string are evaluated
    print(f"Consonants count: {consonant_count}")

print()
print("Welcome To Exercise 1. Count number of vowels and consonants from the user input")

if __name__ == "__main__":
    main()