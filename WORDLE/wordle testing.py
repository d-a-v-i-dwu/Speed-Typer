"""
answer = ["a"]

def check():
    answer = "a"
    guess = input()
    guess = str(guess)
    
    if guess == answer:
        print("yay")
    else:
        print("nope")
check()
"""
"""
letter_list = ["a", "b"]

guess_letter1 = "a"

def removing_letters():

    letter_list = ["a", "b"]

    guess_letter1 = "a"
    
    if guess_letter1 in letter_list:
        updated_list = letter_list.remove(guess_letter1)
        return updated_list
    else:
        print("no")
        return updated_list
    

updated_list = removing_letters()

print(updated_list)
"""
"""
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print(*letter_list, sep = " ")


letter_removed = str.upper(input("Pick a letter to remove: "))
guess_letter_position = letter_list.index(letter_removed)

updated_letter_list = letter_list[:guess_letter_position] + letter_list[guess_letter_position + 1:]

print(*updated_letter_list, sep = " ")
"""
"""
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letter = input()
letter = str.upper(letter)
letter_finder = letter_list.index(letter)
print(letter_finder)



list1 = [11, 5, 17, 18, 23, 50]

unwanted = [0, 3, 4]

for ele in sorted(unwanted, reverse = True):
	del list1[ele]

print (*list1)

"""

"""
letter_list = ["a", "b", "c"]
def letter_remover():
    letter = input()
    letter1 = str(letter[0])
    print(letter1)
    if letter1 in letter_list:
        letter_list.remove(letter1)
        print(letter_list)
    else:
        print("nope")
letter_remover()
"""
"""
inputString = input()
import re

def has_numbers(guess):
    return bool(re.search(r'\d', guess))

has_numbers_final = has_numbers(guess)


def check(has_numbers_final):
    if has_numbers_final == True:
        print(" " * 19, "LETTERS ONLY")
        exit()
    else:
        return
check(has_numbers_final)
"""
"""
def letter_duplicates(answer_letters):
    if len(answer_letters) == len(set(answer_letters)):
        return False
    else:
        return True
letter_duplicates = letter_duplicates(answer_letters)
"""
"""
p = ["A", "B"]
p.remove("B")
print(p)

"""
# string = "wqdwqdqwdWDASDWDA''"
# print(string.isalpha())

# string = input().lower()
# print(string)

# from nltk.corpus import brown
# words = brown.words()

# print(len(words))

# for i in range(100):
#     print(words[i])

# word = "hiwhdoaidh12qw132123'123'12'wefndwkqlmvef2.3w,fw."
# wordlist = list(word.upper())
# wordfinal = ''.join(wordlist)

# print(wordlist)
# print(wordfinal)