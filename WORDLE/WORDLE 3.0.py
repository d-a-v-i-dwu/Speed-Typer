"""
WORDLE
Author: David Wu
"""
import random
import re
import collections

answer_list = ["GUILT", "GROOM","ROUTE", "GLOVE", "FLING", "MODEL", "COMBS", "IRONY", "AVOID", "AWFUL", "ISLES", "UNDER", "URGES","ALLOT", "WIPED", "OUGHT", "STRAW", "STRAP", "SLURP", "PROBE", "PENNY", "LOYAL", "MOGUL", "GOONS", "JOUST", "PALER", "ROACH", "WARES", "WEEPS", "LYNCH", "KITES", "BRICK", "BREAK", "BOUYS", "BOAST", "ICING", "OWNER", "ERODE", "FEARS", "ALONE", "OPENS", "OLDER", "ENTER", "ELDER", "INDIE", "EBONY", "PIANO", "LATHE", "PLUCK", "TRUCK", "WHICH", "WHACK", "WASTE", "FLICK", "FARCE", "EVADE" "JOKER", "BEANS", "BEACH", "PIOUS", "CAROL", "PITCH", "CINCH", "BOMBS", "MEDIA", "POLIO", "GRIME", "AGAIN", "APPLE", "MATCH", "TRAWL", "WINDY" "SMORE", "SMALL", "TESTS", "ROWED", "POWER", "MATTE", "OUTER", "SHOUT", "MERRY", "DAVID", "JELLY", "BATHE", "MOTOR", "AMINE", "HONES", "GAMES", "PHONE"]

answer_picker = random.randrange(0, len(answer_list))
answer = answer_list[answer_picker]

letter1 = answer[0]
letter2 = answer[1]
letter3 = answer[2]
letter4 = answer[3]
letter5 = answer[4]
answer_letters = [letter1, letter2, letter3, letter4, letter5]

correct_guesses1 = []
correct_guesses2 = []
correct_guesses3 = []
correct_guesses4 = []
correct_guesses5 = []

print("=" * 22, "WORDLE", "=" * 22)
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print(*letter_list, sep = " ", )
print()

def guess_code():

    letter_list2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    answer = answer_list[answer_picker]
    letter1_local = answer[0]
    letter2_local = answer[1]
    letter3_local = answer[2]
    letter4_local = answer[3]
    letter5_local = answer[4]
    answer_letters_local = [letter1_local, letter2_local, letter3_local, letter4_local, letter5_local]


    guess = input(" " * 23)
    guess = str.upper(guess)

    def correct_guess(guess):
        if guess == answer:
            print()
            print(" " * 22, answer)
            print("=" * 17, "CONGRATULATIONS!", "=" * 17)
            exit()
        else:
            return

    correct_guess(guess)

    def checking_guess(input):
        try:
            guess_check = int(input)
            print(" " * 19, "LETTERS ONLY")
            exit()
        except ValueError:
            try:
                guess_check = float(input)
                print(" " * 19, "LETTERS ONLY")
                exit()
            except ValueError:
                return
    checking_guess(guess)


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


    def guess_length(input):
        guess_check = str(guess)
        if len(guess_check) != 5:
            print(" " * 13, "GUESS A FIVE LETTER WORD")
            exit()
        else:
            return
        
    guess_length(guess)


    guess_letter1 = guess[0]
    guess_letter2 = guess[1]
    guess_letter3 = guess[2]
    guess_letter4 = guess[3]
    guess_letter5 = guess[4]

                
    letter_finder1 = letter_list2.index(guess_letter1)
        
    if  guess_letter2 == guess_letter1:
        letter_finder2 = 30
    else:
        letter_finder2 = letter_list2.index(guess_letter2)

    if  guess_letter3 == guess_letter2:
        letter_finder3 = 30
    elif guess_letter3 == guess_letter1:
        letter_finder3 = 30
    else:
        letter_finder3 = letter_list2.index(guess_letter3)

    if  guess_letter4 == guess_letter2:
        letter_finder4 = 30
    elif guess_letter4 == guess_letter3:
        letter_finder4 = 30
    elif guess_letter4 == guess_letter1:
        letter_finder4 = 30
    else:
        letter_finder4 = letter_list2.index(guess_letter4)
        
    if  guess_letter5 == guess_letter2:
        letter_finder5 = 30
    elif guess_letter5 == guess_letter3:
        letter_finder5 = 30
    elif guess_letter5 == guess_letter4:
        letter_finder5 = 30
    elif guess_letter5 == guess_letter1:
        letter_finder5 = 30
    else:
        letter_finder5 = letter_list2.index(guess_letter5)

    unwanted = [letter_finder1, letter_finder2, letter_finder3, letter_finder4, letter_finder5]

    for ele in sorted(unwanted, reverse = True):
            del letter_list2[ele]
            letter_list3 = letter_list2

    correct_letters1 = []
    correct_letters2 = []
    correct_letters3 = []
    correct_letters4 = []
    correct_letters5 = []

    def checking_letter1(guess_letter1):
        if guess_letter1 == letter1:
            letter_position = answer_letters_local.index(guess_letter1)
            del answer_letters_local[letter_position]
            correct_letters1.extend(guess_letter1)
            correct_guesses1.extend(guess_letter1)
            return guess_letter1
        else:
            return guess_letter1
        
    guess_letter1 = checking_letter1(guess_letter1)

    def checking_letter2(guess_letter2):
        if guess_letter2 == letter2:
            letter_position = answer_letters_local.index(guess_letter2)
            del answer_letters_local[letter_position]
            correct_letters2.extend(guess_letter2)
            correct_guesses2.extend(guess_letter2)
            return guess_letter2
        else:
            return guess_letter2

    guess_letter2 = checking_letter2(guess_letter2)

    def checking_letter3(guess_letter3):
        if guess_letter3 == letter3:
            letter_position = answer_letters_local.index(guess_letter3)
            del answer_letters_local[letter_position]
            correct_letters3.extend(guess_letter3)
            correct_guesses3.extend(guess_letter3)
            return guess_letter3
        else:
            return guess_letter3

    guess_letter3 = checking_letter3(guess_letter3)

    def checking_letter4(guess_letter4):
        if guess_letter4 == letter4:
            letter_position = answer_letters_local.index(guess_letter4)
            del answer_letters_local[letter_position]
            correct_letters4.extend(guess_letter4)
            correct_guesses4.extend(guess_letter4)
            return guess_letter4
        else:
            return guess_letter4

    guess_letter4 = checking_letter4(guess_letter4)

    def checking_letter5(guess_letter5):
        if guess_letter5 == letter5:
            letter_position = answer_letters_local.index(guess_letter5)
            del answer_letters_local[letter_position]
            correct_letters5.extend(guess_letter5)
            correct_guesses5.extend(guess_letter5)
            return guess_letter5
        else:
            return guess_letter5

    guess_letter5 = checking_letter5(guess_letter5)


    def checking_letter1_final(guess_letter1):
        if guess_letter1 in correct_letters1:
            return guess_letter1
        elif guess_letter1 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter1)
            del answer_letters_local[letter_position]
            guess_letter1 = str.lower(guess_letter1)
        else:
            guess_letter1 = "-"
        return guess_letter1

    guess_letter1 = checking_letter1_final(guess_letter1)

    
    def checking_letter2_final(guess_letter2):
        if guess_letter2 in correct_letters2:
            return guess_letter2
        elif guess_letter2 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter2)
            del answer_letters_local[letter_position]
            guess_letter2 = str.lower(guess_letter2)
        else:
            guess_letter2 = "-"
        return guess_letter2

    guess_letter2 = checking_letter2_final(guess_letter2)

    
    def checking_letter3_final(guess_letter3):
        if guess_letter3 in correct_letters3:
            return guess_letter3
        elif guess_letter3 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter3)
            del answer_letters_local[letter_position]
            guess_letter3 = str.lower(guess_letter3)
        else:
            guess_letter3 = "-"
        return guess_letter3

    guess_letter3 = checking_letter3_final(guess_letter3)

    
    def checking_letter4_final(guess_letter4):
        if guess_letter4 in correct_letters4:
            return guess_letter4
        elif guess_letter4 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter4)
            del answer_letters_local[letter_position]
            guess_letter4 = str.lower(guess_letter4)
        else:
            guess_letter4 = "-"
        return guess_letter4

    guess_letter4 = checking_letter4_final(guess_letter4)

    
    def checking_letter5_final(guess_letter5):
        if guess_letter5 in correct_letters5:
            return guess_letter5
        elif guess_letter5 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter5)
            del answer_letters_local[letter_position]
            guess_letter5 = str.lower(guess_letter5)
        else:
            guess_letter5 = "-"
        return guess_letter5

    guess_letter5 = checking_letter5_final(guess_letter5)
 
    print(" " * 23, guess_letter1, guess_letter2, guess_letter3, guess_letter4, guess_letter5, sep = "")
    return letter_list3


letter_list3 = guess_code()
print(*letter_list3, sep = " ")


def guess_code1():

    answer = answer_list[answer_picker]
    letter1_local = answer[0]
    letter2_local = answer[1]
    letter3_local = answer[2]
    letter4_local = answer[3]
    letter5_local = answer[4]
    answer_letters_local = [letter1_local, letter2_local, letter3_local, letter4_local, letter5_local]

    guess = input(" " * 23)
    guess = str.upper(guess)

    def correct_guess(guess):
        if guess == answer:
            print()
            print(" " * 22, answer)
            print("=" * 17, "CONGRATULATIONS!", "=" * 17)
            exit()
        else:
            return

    correct_guess(guess)

    def checking_guess(input):
        try:
            guess_check = int(input)
            print(" " * 19, "LETTERS ONLY")
            exit()
        except ValueError:
            try:
                guess_check = float(input)
                print(" " * 19, "LETTERS ONLY")
                exit()
            except ValueError:
                return
    checking_guess(guess)


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


    def guess_length(input):
        guess_check = str(guess)
        if len(guess_check) != 5:
            print(" " * 13, "GUESS A FIVE LETTER WORD")
            exit()
        else:
            return
        
    guess_length(guess)


    guess_letter1 = guess[0]
    guess_letter2 = guess[1]
    guess_letter3 = guess[2]
    guess_letter4 = guess[3]
    guess_letter5 = guess[4]
                
    def letter_remover1(guess_letter1):
        try:
            letter_finder1 = letter_list3.index(guess_letter1)
            return letter_finder1
        except ValueError:
            letter_finder1 = 30
            return letter_finder1
    letter_finder1 = letter_remover1(guess_letter1)

    def letter_remover2(guess_letter2):
        if  guess_letter2 == guess_letter1:
            letter_finder2 = 30
            return letter_finder2
        else:
            try:
                letter_finder2 = letter_list3.index(guess_letter2)
                return letter_finder2
            except ValueError:
                letter_finder2 = 30
                return letter_finder2
    letter_finder2 = letter_remover2(guess_letter2)

    def letter_remover3(guess_letter3):
        if  guess_letter3 == guess_letter2:
            letter_finder3 = 30
            return letter_finder3
        elif guess_letter3 == guess_letter1:
            letter_finder3 = 30
            return letter_finder3
        else:
            try:                
                letter_finder3 = letter_list3.index(guess_letter3)
                return letter_finder3
            except ValueError:
                letter_finder3 = 30
                return letter_finder3
    letter_finder3 = letter_remover3(guess_letter3)

    def letter_remover4(guess_letter4):
        if  guess_letter4 == guess_letter2:
            letter_finder4 = 30
            return letter_finder4
        elif guess_letter4 == guess_letter3:
            letter_finder4 = 30
            return letter_finder4
        elif guess_letter4 == guess_letter1:
            letter_finder4 = 30
            return letter_finder4
        else:
            try:   
                letter_finder4 = letter_list3.index(guess_letter4)
                return letter_finder4
            except ValueError:
                letter_finder4 = 30
                return letter_finder4
    letter_finder4 = letter_remover4(guess_letter4)

    def letter_remover5(guess_letter5):
        if  guess_letter5 == guess_letter2:
            letter_finder5 = 30
            return letter_finder5
        elif guess_letter5 == guess_letter3:
            letter_finder5 = 30
            return letter_finder5
        elif guess_letter5 == guess_letter4:
            letter_finder5 = 30
            return letter_finder5
        elif guess_letter5 == guess_letter1:
            letter_finder5 = 30
            return letter_finder5
        else:
            try:
                letter_finder5 = letter_list3.index(guess_letter5)
                return letter_finder5
            except ValueError:
                letter_finder5 = 30
                return letter_finder5
    letter_finder5 = letter_remover5(guess_letter5)

    unwanted = [letter_finder1, letter_finder2, letter_finder3, letter_finder4, letter_finder5]

    for ele in sorted(unwanted, reverse = True):
            del letter_list3[ele]
            letter_list4 = letter_list3

    correct_letters1 = []
    correct_letters2 = []
    correct_letters3 = []
    correct_letters4 = []
    correct_letters5 = []

    def checking_letter1(guess_letter1):
        if guess_letter1 in correct_guesses1:
            correct_letters1.extend(guess_letter1)
            answer_letters_local.remove(guess_letter1)
            return guess_letter1
        elif guess_letter1 == letter1:
            try:    
                letter_position = answer_letters_local.index(guess_letter1)
                del answer_letters_local[letter_position]
                correct_letters1.extend(guess_letter1)
                return guess_letter1
            except ValueError:
                correct_letters1.extend(guess_letter1)
                correct_guesses1.extend(guess_letter1)
                return guess_letter1
        else:
            return guess_letter1
        
    guess_letter1 = checking_letter1(guess_letter1)

    def checking_letter2(guess_letter2):
        if guess_letter2 in correct_guesses2:
            correct_letters2.extend(guess_letter2)
            answer_letters_local.remove(guess_letter2)
            return guess_letter2
        elif guess_letter2 == letter2:
            try:    
                letter_position = answer_letters_local.index(guess_letter2)
                del answer_letters_local[letter_position]
                correct_letters2.extend(guess_letter2)
                return guess_letter2
            except ValueError:
                correct_letters2.extend(guess_letter2)
                correct_guesses2.extend(guess_letter2)
                return guess_letter2
        else:
            return guess_letter2
        
    guess_letter2 = checking_letter2(guess_letter2)

    def checking_letter3(guess_letter3):
        if guess_letter3 in correct_guesses3:
            correct_letters3.extend(guess_letter3)
            answer_letters_local.remove(guess_letter3)
            return guess_letter3
        elif guess_letter3 == letter3:
            try:    
                letter_position = answer_letters_local.index(guess_letter3)
                del answer_letters_local[letter_position]
                correct_letters3.extend(guess_letter3)
                return guess_letter3
            except ValueError:
                correct_letters3.extend(guess_letter3)
                correct_guesses3.extend(guess_letter3)
                return guess_letter3
        else:
            return guess_letter3

    guess_letter3 = checking_letter3(guess_letter3)

    def checking_letter4(guess_letter4):
        if guess_letter4 in correct_guesses4:
            correct_letters1.extend(guess_letter4)
            answer_letters_local.remove(guess_letter4)
            return guess_letter4
        elif guess_letter4 == letter4:
            try:    
                letter_position = answer_letters_local.index(guess_letter4)
                del answer_letters_local[letter_position]
                correct_letters4.extend(guess_letter4)
                return guess_letter4
            except ValueError:
                correct_letters4.extend(guess_letter4)
                correct_guesses4.extend(guess_letter4)
                return guess_letter4
        else:
            return guess_letter4

    guess_letter4 = checking_letter4(guess_letter4)

    def checking_letter5(guess_letter5):
        if guess_letter5 in correct_guesses5:
            correct_letters5.extend(guess_letter5)
            answer_letters_local.remove(guess_letter5)
            return guess_letter5
        elif guess_letter5 == letter5:
            try:
                letter_position = answer_letters_local.index(guess_letter5)
                del answer_letters_local[letter_position]
                correct_letters5.extend(guess_letter5)
                return guess_letter5
            except ValueError:
                correct_letters5.extend(guess_letter5)
                correct_guesses5.extend(guess_letter5)
                return guess_letter5
        else:
            return guess_letter5

    guess_letter5 = checking_letter5(guess_letter5)
    
    def checking_letter1_final(guess_letter1):
        if guess_letter1 in correct_letters1:
            return guess_letter1
        elif guess_letter1 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter1)
            del answer_letters_local[letter_position]
            guess_letter1 = str.lower(guess_letter1)
        else:
            guess_letter1 = "-"
        return guess_letter1

    guess_letter1 = checking_letter1_final(guess_letter1)

    def checking_letter2_final(guess_letter2):
        if guess_letter2 in correct_letters2:
            return guess_letter2
        elif guess_letter2 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter2)
            del answer_letters_local[letter_position]
            guess_letter2 = str.lower(guess_letter2)
        else:
            guess_letter2 = "-"
        return guess_letter2

    guess_letter2 = checking_letter2_final(guess_letter2)

    
    def checking_letter3_final(guess_letter3):
        if guess_letter3 in correct_letters3:
            return guess_letter3
        elif guess_letter3 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter3)
            del answer_letters_local[letter_position]
            guess_letter3 = str.lower(guess_letter3)
        else:
            guess_letter3 = "-"
        return guess_letter3

    guess_letter3 = checking_letter3_final(guess_letter3)

    
    def checking_letter4_final(guess_letter4):
        if guess_letter4 in correct_letters4:
            return guess_letter4
        elif guess_letter4 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter4)
            del answer_letters_local[letter_position]
            guess_letter4 = str.lower(guess_letter4)
        else:
            guess_letter4 = "-"
        return guess_letter4

    guess_letter4 = checking_letter4_final(guess_letter4)

    
    def checking_letter5_final(guess_letter5):
        if guess_letter5 in correct_letters5:
            return guess_letter5
        elif guess_letter5 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter5)
            del answer_letters_local[letter_position]
            guess_letter5 = str.lower(guess_letter5)
        else:
            guess_letter5 = "-"
        return guess_letter5

    guess_letter5 = checking_letter5_final(guess_letter5)
    
    print(" " * 23, guess_letter1, guess_letter2, guess_letter3, guess_letter4, guess_letter5, sep = "")
    return letter_list4

letter_list4 = guess_code1()
print(*letter_list4, sep = " ")


def guess_code2():

    answer = answer_list[answer_picker]
    letter1_local = answer[0]
    letter2_local = answer[1]
    letter3_local = answer[2]
    letter4_local = answer[3]
    letter5_local = answer[4]
    answer_letters_local = [letter1_local, letter2_local, letter3_local, letter4_local, letter5_local]


    guess = input(" " * 23)
    guess = str.upper(guess)

    def correct_guess(guess):
        if guess == answer:
            print()
            print(" " * 22, answer)
            print("=" * 17, "CONGRATULATIONS!", "=" * 17)
            exit()
        else:
            return

    correct_guess(guess)

    def checking_guess(input):
        try:
            guess_check = int(input)
            print(" " * 19, "LETTERS ONLY")
            exit()
        except ValueError:
            try:
                guess_check = float(input)
                print(" " * 19, "LETTERS ONLY")
                exit()
            except ValueError:
                return
    checking_guess(guess)


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


    def guess_length(input):
        guess_check = str(guess)
        if len(guess_check) != 5:
            print(" " * 13, "GUESS A FIVE LETTER WORD")
            exit()
        else:
            return
        
    guess_length(guess)


    guess_letter1 = guess[0]
    guess_letter2 = guess[1]
    guess_letter3 = guess[2]
    guess_letter4 = guess[3]
    guess_letter5 = guess[4]
                
    def letter_remover1(guess_letter1):
        try:
            letter_finder1 = letter_list4.index(guess_letter1)
            return letter_finder1
        except ValueError:
            letter_finder1 = 30
            return letter_finder1
    letter_finder1 = letter_remover1(guess_letter1)

    def letter_remover2(guess_letter2):
        if  guess_letter2 == guess_letter1:
            letter_finder2 = 30
            return letter_finder2
        else:
            try:
                letter_finder2 = letter_list4.index(guess_letter2)
                return letter_finder2
            except ValueError:
                letter_finder2 = 30
                return letter_finder2
    letter_finder2 = letter_remover2(guess_letter2)

    def letter_remover3(guess_letter3):
        if  guess_letter3 == guess_letter2:
            letter_finder3 = 30
            return letter_finder3
        elif guess_letter3 == guess_letter1:
            letter_finder3 = 30
            return letter_finder3
        else:
            try:                
                letter_finder3 = letter_list4.index(guess_letter3)
                return letter_finder3
            except ValueError:
                letter_finder3 = 30
                return letter_finder3
    letter_finder3 = letter_remover3(guess_letter3)

    def letter_remover4(guess_letter4):
        if  guess_letter4 == guess_letter2:
            letter_finder4 = 30
            return letter_finder4
        elif guess_letter4 == guess_letter3:
            letter_finder4 = 30
            return letter_finder4
        elif guess_letter4 == guess_letter1:
            letter_finder4 = 30
            return letter_finder4
        else:
            try:   
                letter_finder4 = letter_list4.index(guess_letter4)
                return letter_finder4
            except ValueError:
                letter_finder4 = 30
                return letter_finder4
    letter_finder4 = letter_remover4(guess_letter4)

    def letter_remover5(guess_letter5):
        if  guess_letter5 == guess_letter2:
            letter_finder5 = 30
            return letter_finder5
        elif guess_letter5 == guess_letter3:
            letter_finder5 = 30
            return letter_finder5
        elif guess_letter5 == guess_letter4:
            letter_finder5 = 30
            return letter_finder5
        elif guess_letter5 == guess_letter1:
            letter_finder5 = 30
            return letter_finder5
        else:
            try:
                letter_finder5 = letter_list4.index(guess_letter5)
                return letter_finder5
            except ValueError:
                letter_finder5 = 30
                return letter_finder5
    letter_finder5 = letter_remover5(guess_letter5)

    unwanted = [letter_finder1, letter_finder2, letter_finder3, letter_finder4, letter_finder5]

    for ele in sorted(unwanted, reverse = True):
            del letter_list4[ele]
            letter_list5 = letter_list4

    correct_letters1 = []
    correct_letters2 = []
    correct_letters3 = []
    correct_letters4 = []
    correct_letters5 = []

    def checking_letter1(guess_letter1):
        if guess_letter1 in correct_guesses1:
            correct_letters1.extend(guess_letter1)
            answer_letters_local.remove(guess_letter1)
            return guess_letter1
        elif guess_letter1 == letter1:
            try:    
                letter_position = answer_letters_local.index(guess_letter1)
                del answer_letters_local[letter_position]
                correct_letters1.extend(guess_letter1)
                return guess_letter1
            except ValueError:
                correct_letters1.extend(guess_letter1)
                correct_guesses1.extend(guess_letter1)
                return guess_letter1
        else:
            return guess_letter1
        
    guess_letter1 = checking_letter1(guess_letter1)

    def checking_letter2(guess_letter2):
        if guess_letter2 in correct_guesses2:
            correct_letters2.extend(guess_letter2)
            answer_letters_local.remove(guess_letter2)
            return guess_letter2
        elif guess_letter2 == letter2:
            try:    
                letter_position = answer_letters_local.index(guess_letter2)
                del answer_letters_local[letter_position]
                correct_letters2.extend(guess_letter2)
                return guess_letter2
            except ValueError:
                correct_letters2.extend(guess_letter2)
                correct_guesses2.extend(guess_letter2)
                return guess_letter2
        else:
            return guess_letter2
        
    guess_letter2 = checking_letter2(guess_letter2)

    def checking_letter3(guess_letter3):
        if guess_letter3 in correct_guesses3:
            correct_letters3.extend(guess_letter3)
            answer_letters_local.remove(guess_letter3)
            return guess_letter3
        elif guess_letter3 == letter3:
            try:    
                letter_position = answer_letters_local.index(guess_letter3)
                del answer_letters_local[letter_position]
                correct_letters3.extend(guess_letter3)
                return guess_letter3
            except ValueError:
                correct_letters3.extend(guess_letter3)
                correct_guesses3.extend(guess_letter3)
                return guess_letter3
        else:
            return guess_letter3

    guess_letter3 = checking_letter3(guess_letter3)

    def checking_letter4(guess_letter4):
        if guess_letter4 in correct_guesses4:
            correct_letters1.extend(guess_letter4)
            answer_letters_local.remove(guess_letter4)
            return guess_letter4
        elif guess_letter4 == letter4:
            try:    
                letter_position = answer_letters_local.index(guess_letter4)
                del answer_letters_local[letter_position]
                correct_letters4.extend(guess_letter4)
                return guess_letter4
            except ValueError:
                correct_letters4.extend(guess_letter4)
                correct_guesses4.extend(guess_letter4)
                return guess_letter4
        else:
            return guess_letter4

    guess_letter4 = checking_letter4(guess_letter4)

    def checking_letter5(guess_letter5):
        if guess_letter5 in correct_guesses5:
            correct_letters5.extend(guess_letter5)
            answer_letters_local.remove(guess_letter5)
            return guess_letter5
        elif guess_letter5 == letter5:
            try:
                letter_position = answer_letters_local.index(guess_letter5)
                del answer_letters_local[letter_position]
                correct_letters5.extend(guess_letter5)
                return guess_letter5
            except ValueError:
                correct_letters5.extend(guess_letter5)
                correct_guesses5.extend(guess_letter5)
                return guess_letter5
        else:
            return guess_letter5

    guess_letter5 = checking_letter5(guess_letter5)

    
    def checking_letter1_final(guess_letter1):
        if guess_letter1 in correct_letters1:
            return guess_letter1
        elif guess_letter1 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter1)
            del answer_letters_local[letter_position]
            guess_letter1 = str.lower(guess_letter1)
        else:
            guess_letter1 = "-"
        return guess_letter1

    guess_letter1 = checking_letter1_final(guess_letter1)

    
    def checking_letter2_final(guess_letter2):
        if guess_letter2 in correct_letters2:
            return guess_letter2
        elif guess_letter2 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter2)
            del answer_letters_local[letter_position]
            guess_letter2 = str.lower(guess_letter2)
        else:
            guess_letter2 = "-"
        return guess_letter2

    guess_letter2 = checking_letter2_final(guess_letter2)

    
    def checking_letter3_final(guess_letter3):
        if guess_letter3 in correct_letters3:
            return guess_letter3
        elif guess_letter3 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter3)
            del answer_letters_local[letter_position]
            guess_letter3 = str.lower(guess_letter3)
        else:
            guess_letter3 = "-"
        return guess_letter3

    guess_letter3 = checking_letter3_final(guess_letter3)

    
    def checking_letter4_final(guess_letter4):
        if guess_letter4 in correct_letters4:
            return guess_letter4
        elif guess_letter4 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter4)
            del answer_letters_local[letter_position]
            guess_letter4 = str.lower(guess_letter4)
        else:
            guess_letter4 = "-"
        return guess_letter4

    guess_letter4 = checking_letter4_final(guess_letter4)

    
    def checking_letter5_final(guess_letter5):
        if guess_letter5 in correct_letters5:
            return guess_letter5
        elif guess_letter5 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter5)
            del answer_letters_local[letter_position]
            guess_letter5 = str.lower(guess_letter5)
        else:
            guess_letter5 = "-"
        return guess_letter5

    guess_letter5 = checking_letter5_final(guess_letter5)
    
    print(" " * 23, guess_letter1, guess_letter2, guess_letter3, guess_letter4, guess_letter5, sep = "")
    return letter_list5


letter_list5 = guess_code2()
print(*letter_list5, sep = " ")


def guess_code3():

    answer = answer_list[answer_picker]
    letter1_local = answer[0]
    letter2_local = answer[1]
    letter3_local = answer[2]
    letter4_local = answer[3]
    letter5_local = answer[4]
    answer_letters_local = [letter1_local, letter2_local, letter3_local, letter4_local, letter5_local]

    guess = input(" " * 23)
    guess = str.upper(guess)

    def correct_guess(guess):
        if guess == answer:
            print()
            print(" " * 22, answer)
            print("=" * 17, "CONGRATULATIONS!", "=" * 17)
            exit()
        else:
            return

    correct_guess(guess)

    def checking_guess(input):
        try:
            guess_check = int(input)
            print(" " * 19, "LETTERS ONLY")
            exit()
        except ValueError:
            try:
                guess_check = float(input)
                print(" " * 19, "LETTERS ONLY")
                exit()
            except ValueError:
                return
    checking_guess(guess)


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


    def guess_length(input):
        guess_check = str(guess)
        if len(guess_check) != 5:
            print(" " * 13, "GUESS A FIVE LETTER WORD")
            exit()
        else:
            return
        
    guess_length(guess)


    guess_letter1 = guess[0]
    guess_letter2 = guess[1]
    guess_letter3 = guess[2]
    guess_letter4 = guess[3]
    guess_letter5 = guess[4]
                
    def letter_remover1(guess_letter1):
        try:
            letter_finder1 = letter_list5.index(guess_letter1)
            return letter_finder1
        except ValueError:
            letter_finder1 = 30
            return letter_finder1
    letter_finder1 = letter_remover1(guess_letter1)

    def letter_remover2(guess_letter2):
        if  guess_letter2 == guess_letter1:
            letter_finder2 = 30
            return letter_finder2
        else:
            try:
                letter_finder2 = letter_list5.index(guess_letter2)
                return letter_finder2
            except ValueError:
                letter_finder2 = 30
                return letter_finder2
    letter_finder2 = letter_remover2(guess_letter2)

    def letter_remover3(guess_letter3):
        if  guess_letter3 == guess_letter2:
            letter_finder3 = 30
            return letter_finder3
        elif guess_letter3 == guess_letter1:
            letter_finder3 = 30
            return letter_finder3
        else:
            try:                
                letter_finder3 = letter_list5.index(guess_letter3)
                return letter_finder3
            except ValueError:
                letter_finder3 = 30
                return letter_finder3
    letter_finder3 = letter_remover3(guess_letter3)

    def letter_remover4(guess_letter4):
        if  guess_letter4 == guess_letter2:
            letter_finder4 = 30
            return letter_finder4
        elif guess_letter4 == guess_letter3:
            letter_finder4 = 30
            return letter_finder4
        elif guess_letter4 == guess_letter1:
            letter_finder4 = 30
            return letter_finder4
        else:
            try:   
                letter_finder4 = letter_list5.index(guess_letter4)
                return letter_finder4
            except ValueError:
                letter_finder4 = 30
                return letter_finder4
    letter_finder4 = letter_remover4(guess_letter4)

    def letter_remover5(guess_letter5):
        if  guess_letter5 == guess_letter2:
            letter_finder5 = 30
            return letter_finder5
        elif guess_letter5 == guess_letter3:
            letter_finder5 = 30
            return letter_finder5
        elif guess_letter5 == guess_letter4:
            letter_finder5 = 30
            return letter_finder5
        elif guess_letter5 == guess_letter1:
            letter_finder5 = 30
            return letter_finder5
        else:
            try:
                letter_finder5 = letter_list5.index(guess_letter5)
                return letter_finder5
            except ValueError:
                letter_finder5 = 30
                return letter_finder5
    letter_finder5 = letter_remover5(guess_letter5)

    unwanted = [letter_finder1, letter_finder2, letter_finder3, letter_finder4, letter_finder5]

    for ele in sorted(unwanted, reverse = True):
            del letter_list5[ele]
            letter_list6 = letter_list5

    correct_letters1 = []
    correct_letters2 = []
    correct_letters3 = []
    correct_letters4 = []
    correct_letters5 = []

    def checking_letter1(guess_letter1):
        if guess_letter1 in correct_guesses1:
            correct_letters1.extend(guess_letter1)
            answer_letters_local.remove(guess_letter1)
            return guess_letter1
        elif guess_letter1 == letter1:
            try:    
                letter_position = answer_letters_local.index(guess_letter1)
                del answer_letters_local[letter_position]
                correct_letters1.extend(guess_letter1)
                return guess_letter1
            except ValueError:
                correct_letters1.extend(guess_letter1)
                correct_guesses1.extend(guess_letter1)
                return guess_letter1
        else:
            return guess_letter1
        
    guess_letter1 = checking_letter1(guess_letter1)

    def checking_letter2(guess_letter2):
        if guess_letter2 in correct_guesses2:
            correct_letters2.extend(guess_letter2)
            answer_letters_local.remove(guess_letter2)
            return guess_letter2
        elif guess_letter2 == letter2:
            try:    
                letter_position = answer_letters_local.index(guess_letter2)
                del answer_letters_local[letter_position]
                correct_letters2.extend(guess_letter2)
                return guess_letter2
            except ValueError:
                correct_letters2.extend(guess_letter2)
                correct_guesses2.extend(guess_letter2)
                return guess_letter2
        else:
            return guess_letter2
        
    guess_letter2 = checking_letter2(guess_letter2)

    def checking_letter3(guess_letter3):
        if guess_letter3 in correct_guesses3:
            correct_letters3.extend(guess_letter3)
            answer_letters_local.remove(guess_letter3)
            return guess_letter3
        elif guess_letter3 == letter3:
            try:    
                letter_position = answer_letters_local.index(guess_letter3)
                del answer_letters_local[letter_position]
                correct_letters3.extend(guess_letter3)
                return guess_letter3
            except ValueError:
                correct_letters3.extend(guess_letter3)
                correct_guesses3.extend(guess_letter3)
                return guess_letter3
        else:
            return guess_letter3

    guess_letter3 = checking_letter3(guess_letter3)

    def checking_letter4(guess_letter4):
        if guess_letter4 in correct_guesses4:
            correct_letters1.extend(guess_letter4)
            answer_letters_local.remove(guess_letter4)
            return guess_letter4
        elif guess_letter4 == letter4:
            try:    
                letter_position = answer_letters_local.index(guess_letter4)
                del answer_letters_local[letter_position]
                correct_letters4.extend(guess_letter4)
                return guess_letter4
            except ValueError:
                correct_letters4.extend(guess_letter4)
                correct_guesses4.extend(guess_letter4)
                return guess_letter4
        else:
            return guess_letter4

    guess_letter4 = checking_letter4(guess_letter4)

    def checking_letter5(guess_letter5):
        if guess_letter5 in correct_guesses5:
            correct_letters5.extend(guess_letter5)
            answer_letters_local.remove(guess_letter5)
            return guess_letter5
        elif guess_letter5 == letter5:
            try:
                letter_position = answer_letters_local.index(guess_letter5)
                del answer_letters_local[letter_position]
                correct_letters5.extend(guess_letter5)
                return guess_letter5
            except ValueError:
                correct_letters5.extend(guess_letter5)
                correct_guesses5.extend(guess_letter5)
                return guess_letter5
        else:
            return guess_letter5

    guess_letter5 = checking_letter5(guess_letter5)

    
    def checking_letter1_final(guess_letter1):
        if guess_letter1 in correct_letters1:
            return guess_letter1
        elif guess_letter1 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter1)
            del answer_letters_local[letter_position]
            guess_letter1 = str.lower(guess_letter1)
        else:
            guess_letter1 = "-"
        return guess_letter1

    guess_letter1 = checking_letter1_final(guess_letter1)

    
    def checking_letter2_final(guess_letter2):
        if guess_letter2 in correct_letters2:
            return guess_letter2
        elif guess_letter2 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter2)
            del answer_letters_local[letter_position]
            guess_letter2 = str.lower(guess_letter2)
        else:
            guess_letter2 = "-"
        return guess_letter2

    guess_letter2 = checking_letter2_final(guess_letter2)

    
    def checking_letter3_final(guess_letter3):
        if guess_letter3 in correct_letters3:
            return guess_letter3
        elif guess_letter3 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter3)
            del answer_letters_local[letter_position]
            guess_letter3 = str.lower(guess_letter3)
        else:
            guess_letter3 = "-"
        return guess_letter3

    guess_letter3 = checking_letter3_final(guess_letter3)

    
    def checking_letter4_final(guess_letter4):
        if guess_letter4 in correct_letters4:
            return guess_letter4
        elif guess_letter4 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter4)
            del answer_letters_local[letter_position]
            guess_letter4 = str.lower(guess_letter4)
        else:
            guess_letter4 = "-"
        return guess_letter4

    guess_letter4 = checking_letter4_final(guess_letter4)

    
    def checking_letter5_final(guess_letter5):
        if guess_letter5 in correct_letters5:
            return guess_letter5
        elif guess_letter5 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter5)
            del answer_letters_local[letter_position]
            guess_letter5 = str.lower(guess_letter5)
        else:
            guess_letter5 = "-"
        return guess_letter5

    guess_letter5 = checking_letter5_final(guess_letter5)
    

    print(" " * 23, guess_letter1, guess_letter2, guess_letter3, guess_letter4, guess_letter5, sep = "")
    return letter_list6

letter_list6 = guess_code3()
print(*letter_list6, sep = " ")


def guess_code4():

    answer = answer_list[answer_picker]
    letter1_local = answer[0]
    letter2_local = answer[1]
    letter3_local = answer[2]
    letter4_local = answer[3]
    letter5_local = answer[4]
    answer_letters_local = [letter1_local, letter2_local, letter3_local, letter4_local, letter5_local]
    print(" " * 19, "FINAL GUESS")
    guess = input(" " * 23)
    guess = str.upper(guess)

    def correct_guess(guess):
        if guess == answer:
            print()
            print(" " * 22, answer)
            print("=" * 17, "CONGRATULATIONS!", "=" * 17)
            exit()
        else:
            return

    correct_guess(guess)

    def checking_guess(input):
        try:
            guess_check = int(input)
            print(" " * 19, "LETTERS ONLY")
            exit()
        except ValueError:
            try:
                guess_check = float(input)
                print(" " * 19, "LETTERS ONLY")
                exit()
            except ValueError:
                return
    checking_guess(guess)


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


    def guess_length(input):
        guess_check = str(guess)
        if len(guess_check) != 5:
            print(" " * 13, "GUESS A FIVE LETTER WORD")
            exit()
        else:
            return
        
    guess_length(guess)


    guess_letter1 = guess[0]
    guess_letter2 = guess[1]
    guess_letter3 = guess[2]
    guess_letter4 = guess[3]
    guess_letter5 = guess[4]
                
    def letter_remover1(guess_letter1):
        try:
            letter_finder1 = letter_list6.index(guess_letter1)
            return letter_finder1
        except ValueError:
            letter_finder1 = 30
            return letter_finder1
    letter_finder1 = letter_remover1(guess_letter1)

    def letter_remover2(guess_letter2):
        if  guess_letter2 == guess_letter1:
            letter_finder2 = 30
            return letter_finder2
        else:
            try:
                letter_finder2 = letter_list6.index(guess_letter2)
                return letter_finder2
            except ValueError:
                letter_finder2 = 30
                return letter_finder2
    letter_finder2 = letter_remover2(guess_letter2)

    def letter_remover3(guess_letter3):
        if  guess_letter3 == guess_letter2:
            letter_finder3 = 30
            return letter_finder3
        elif guess_letter3 == guess_letter1:
            letter_finder3 = 30
            return letter_finder3
        else:
            try:                
                letter_finder3 = letter_list6.index(guess_letter3)
                return letter_finder3
            except ValueError:
                letter_finder3 = 30
                return letter_finder3
    letter_finder3 = letter_remover3(guess_letter3)

    def letter_remover4(guess_letter4):
        if  guess_letter4 == guess_letter2:
            letter_finder4 = 30
            return letter_finder4
        elif guess_letter4 == guess_letter3:
            letter_finder4 = 30
            return letter_finder4
        elif guess_letter4 == guess_letter1:
            letter_finder4 = 30
            return letter_finder4
        else:
            try:   
                letter_finder4 = letter_list6.index(guess_letter4)
                return letter_finder4
            except ValueError:
                letter_finder4 = 30
                return letter_finder4
    letter_finder4 = letter_remover4(guess_letter4)

    def letter_remover5(guess_letter5):
        if  guess_letter5 == guess_letter2:
            letter_finder5 = 30
            return letter_finder5
        elif guess_letter5 == guess_letter3:
            letter_finder5 = 30
            return letter_finder5
        elif guess_letter5 == guess_letter4:
            letter_finder5 = 30
            return letter_finder5
        elif guess_letter5 == guess_letter1:
            letter_finder5 = 30
            return letter_finder5
        else:
            try:
                letter_finder5 = letter_list6.index(guess_letter5)
                return letter_finder5
            except ValueError:
                letter_finder5 = 30
                return letter_finder5
    letter_finder5 = letter_remover5(guess_letter5)

    unwanted = [letter_finder1, letter_finder2, letter_finder3, letter_finder4, letter_finder5]

    for ele in sorted(unwanted, reverse = True):
            del letter_list6[ele]
            letter_list7 = letter_list6

    correct_letters1 = []
    correct_letters2 = []
    correct_letters3 = []
    correct_letters4 = []
    correct_letters5 = []


    def checking_letter1(guess_letter1):
        if guess_letter1 in correct_guesses1:
            correct_letters1.extend(guess_letter1)
            answer_letters_local.remove(guess_letter1)
            return guess_letter1
        elif guess_letter1 == letter1:
            try:    
                letter_position = answer_letters_local.index(guess_letter1)
                del answer_letters_local[letter_position]
                correct_letters1.extend(guess_letter1)
                return guess_letter1
            except ValueError:
                correct_letters1.extend(guess_letter1)
                correct_guesses1.extend(guess_letter1)
                return guess_letter1
        else:
            return guess_letter1
        
    guess_letter1 = checking_letter1(guess_letter1)

    def checking_letter2(guess_letter2):
        if guess_letter2 in correct_guesses2:
            correct_letters2.extend(guess_letter2)
            answer_letters_local.remove(guess_letter2)
            return guess_letter2
        elif guess_letter2 == letter2:
            try:    
                letter_position = answer_letters_local.index(guess_letter2)
                del answer_letters_local[letter_position]
                correct_letters2.extend(guess_letter2)
                return guess_letter2
            except ValueError:
                correct_letters2.extend(guess_letter2)
                correct_guesses2.extend(guess_letter2)
                return guess_letter2
        else:
            return guess_letter2
        
    guess_letter2 = checking_letter2(guess_letter2)

    def checking_letter3(guess_letter3):
        if guess_letter3 in correct_guesses3:
            correct_letters3.extend(guess_letter3)
            answer_letters_local.remove(guess_letter3)
            return guess_letter3
        elif guess_letter3 == letter3:
            try:    
                letter_position = answer_letters_local.index(guess_letter3)
                del answer_letters_local[letter_position]
                correct_letters3.extend(guess_letter3)
                return guess_letter3
            except ValueError:
                correct_letters3.extend(guess_letter3)
                correct_guesses3.extend(guess_letter3)
                return guess_letter3
        else:
            return guess_letter3

    guess_letter3 = checking_letter3(guess_letter3)

    def checking_letter4(guess_letter4):
        if guess_letter4 in correct_guesses4:
            correct_letters1.extend(guess_letter4)
            answer_letters_local.remove(guess_letter4)
            return guess_letter4
        elif guess_letter4 == letter4:
            try:    
                letter_position = answer_letters_local.index(guess_letter4)
                del answer_letters_local[letter_position]
                correct_letters4.extend(guess_letter4)
                return guess_letter4
            except ValueError:
                correct_letters4.extend(guess_letter4)
                correct_guesses4.extend(guess_letter4)
                return guess_letter4
        else:
            return guess_letter4

    guess_letter4 = checking_letter4(guess_letter4)

    def checking_letter5(guess_letter5):
        if guess_letter5 in correct_guesses5:
            correct_letters5.extend(guess_letter5)
            answer_letters_local.remove(guess_letter5)
            return guess_letter5
        elif guess_letter5 == letter5:
            try:
                letter_position = answer_letters_local.index(guess_letter5)
                del answer_letters_local[letter_position]
                correct_letters5.extend(guess_letter5)
                return guess_letter5
            except ValueError:
                correct_letters5.extend(guess_letter5)
                correct_guesses5.extend(guess_letter5)
                return guess_letter5
        else:
            return guess_letter5

    guess_letter5 = checking_letter5(guess_letter5)
 
    def checking_letter1_final(guess_letter1):
        if guess_letter1 in correct_letters1:
            return guess_letter1
        elif guess_letter1 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter1)
            del answer_letters_local[letter_position]
            guess_letter1 = str.lower(guess_letter1)
        else:
            guess_letter1 = "-"
        return guess_letter1

    guess_letter1 = checking_letter1_final(guess_letter1)

    
    def checking_letter2_final(guess_letter2):
        if guess_letter2 in correct_letters2:
            return guess_letter2
        elif guess_letter2 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter2)
            del answer_letters_local[letter_position]
            guess_letter2 = str.lower(guess_letter2)
        else:
            guess_letter2 = "-"
        return guess_letter2

    guess_letter2 = checking_letter2_final(guess_letter2)

    
    def checking_letter3_final(guess_letter3):
        if guess_letter3 in correct_letters3:
            return guess_letter3
        elif guess_letter3 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter3)
            del answer_letters_local[letter_position]
            guess_letter3 = str.lower(guess_letter3)
        else:
            guess_letter3 = "-"
        return guess_letter3

    guess_letter3 = checking_letter3_final(guess_letter3)

    
    def checking_letter4_final(guess_letter4):
        if guess_letter4 in correct_letters4:
            return guess_letter4
        elif guess_letter4 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter4)
            del answer_letters_local[letter_position]
            guess_letter4 = str.lower(guess_letter4)
        else:
            guess_letter4 = "-"
        return guess_letter4

    guess_letter4 = checking_letter4_final(guess_letter4)

    
    def checking_letter5_final(guess_letter5):
        if guess_letter5 in correct_letters5:
            return guess_letter5
        elif guess_letter5 in answer_letters_local:
            letter_position = answer_letters_local.index(guess_letter5)
            del answer_letters_local[letter_position]
            guess_letter5 = str.lower(guess_letter5)
        else:
            guess_letter5 = "-"
        return guess_letter5

    guess_letter5 = checking_letter5_final(guess_letter5)
    
    print(" " * 23, guess_letter1, guess_letter2, guess_letter3, guess_letter4, guess_letter5, sep = "")
    return letter_list7

letter_list7 = guess_code4()
print(*letter_list7, sep = " ")
print()
print("=" * 15, "THE WORD WAS:", answer, "=" * 16)
exit()
