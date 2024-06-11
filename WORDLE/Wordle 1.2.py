"""
WORDLE
Author: David Wu
"""
import random
"""
answer_list = ["PIANO", "JOKER", "BEANS" "PIOUS", "CAROL", "PITCH", "CINCH", "BOMBS", "MEDIA", "POLIO", "AGAIN", "APPLE", "MATCH", "TRAWL", "WINDY" "SMORE", "SMALL", "TESTS", "ROWED", "POWER", "MATTE", "OUTER", "SHOUT", "MERRY", "DAVID", "JELLY", "BATHE", "MOTOR", "AMINE", "HONES", "BORED", "GAMES", "PHONE"]
"""
answer_list = ["AEIOU"]
answer_picker = random.randrange(0, len(answer_list))
answer = answer_list[answer_picker]

letter1 = answer[0]
letter2 = answer[1]
letter3 = answer[2]
letter4 = answer[3]
letter5 = answer[4]
answer_letters = [letter1, letter2, letter3, letter4, letter5]

print("=" * 22, "WORDLE", "=" * 22)
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print(*letter_list, sep = " ")
print()

def guess_code():

    letter_list2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    answer = answer_list[answer_picker]
    guess = input(" " * 23)
    guess = str.upper(guess)

    def guess_length(input):
        guess_check = str(guess)
        if len(guess_check) != 5:
            print(" " * 13, "GUESS A FIVE LETTER WORD")
            exit()
        else:
            return
        
    guess_length(input)

    guess_letter1 = guess[0]
    guess_letter2 = guess[1]
    guess_letter3 = guess[2]
    guess_letter4 = guess[3]
    guess_letter5 = guess[4]
    guess_letter_list = (guess_letter1, guess_letter2, guess_letter3, guess_letter4, guess_letter5)

    def correct_guess(guess):
        if guess == answer:
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
                try:
                    sorted(guess_letter_list)
                    return
                except TypeError:
                    print(" " * 19, "LETTERS ONLY")
                    exit()
                    

    checking_guess(guess)

                
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


    def checking_letter1(guess_letter1):
        if guess_letter1 == letter1:
            letter_position = answer_letters.index(guess_letter1)
            del answer_letters[letter_position]
        elif guess_letter1 in answer_letters:
            guess_letter1 = str.lower(guess_letter1)
        else:
            guess_letter1 = "-"
        return guess_letter1

    guess_letter1 = checking_letter1(guess_letter1)

    def checking_letter2(guess_letter2):
        if guess_letter2 == letter2:
            letter_position = answer_letters.index(guess_letter2)
            del answer_letters[letter_position]
        elif guess_letter2 in answer_letters:
            guess_letter2 = str.lower(guess_letter2)
        else:
            guess_letter2 = "-"
        return guess_letter2

    guess_letter2 = checking_letter2(guess_letter2)

    def checking_letter3(guess_letter3):
        if guess_letter3 == letter3:
            letter_position = answer_letters.index(guess_letter3)
            del answer_letters[letter_position]
        elif guess_letter3 in answer_letters:
            guess_letter3 = str.lower(guess_letter3)
        else:
            guess_letter3 = "-"
        return guess_letter3

    guess_letter3 = checking_letter3(guess_letter3)

    def checking_letter4(guess_letter4):
        if guess_letter4 == letter4:
            letter_position = answer_letters.index(guess_letter4)
            del answer_letters[letter_position]
        elif guess_letter4 in answer_letters:
            guess_letter4 = str.lower(guess_letter4)
        else:
            guess_letter4 = "-"
        return guess_letter4

    guess_letter4 = checking_letter4(guess_letter4)

    def checking_letter5(guess_letter5):
        if guess_letter5 == letter5:
            letter_position = answer_letters.index(guess_letter5)
            del answer_letters[letter_position]
        elif guess_letter5 in answer_letters:
            guess_letter5 = str.lower(guess_letter5)
        else:
            guess_letter5 = "-"
        return guess_letter5

    guess_letter5 = checking_letter5(guess_letter5)
 
    print(" " * 23, guess_letter1, guess_letter2, guess_letter3, guess_letter4, guess_letter5, sep = "")
    print()
    return letter_list3
   
letter_list3 = guess_code()
print(*letter_list3, sep = " ")


letter_list4 = guess_code1()
print(*letter_list4, sep = " ")


letter_list5 = guess_code2()
print(*letter_list5, sep = " ")


letter_list6 = guess_code3()
print(*letter_list6, sep = " ")


guess_code4()
print()
print("THE WORD WAS:", answer)
exit()
