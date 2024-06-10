"""
First try at Hangman
Author: David Wu
"""
import random
import time
from nltk.corpus import words

def main():
    print("===WELCOME TO HANGMAN===")
    print()
    repeat = "Y"
    while repeat == "Y" or repeat == "y":
        # difficulty = intro()
        intro()
        # answer = word_picker(difficulty)
        answer = word_picker()
        result = gamecode(answer)
        end(result, answer)
        print()
        repeat = input("Type Y to play again ")
        print()

def intro():
    time.sleep(1)
    # print("easy//intermediate//hard")
    print("Generating word...")
    time.sleep(0.8)
    # difficulty = input("choose your difficulty: ")
    # difficulty_list = ["easy", "intermediate", "hard"]
    # if difficulty.isdigit() == True or difficulty.lower() not in difficulty_list:
    #     check = True
    # else:
    #     check = False
    # while check == True:
    #     print()
    #     difficulty = input("not a valid difficulty, pick again: ")
    #     if difficulty.isdigit() == False and difficulty.lower() in difficulty_list:
    #         check = False

    # return difficulty
def word_picker():
# def word_picker(difficulty):
    # if difficulty == "easy":
    #     word_list = ["hello"]
    # elif difficulty == "hard":
    #     word_list = ["knave"]
    # else:
    #     word_list = []
    word_list = words.words()
    answer = word_list[random.randrange(len(word_list))]
    return answer

def gamecode(answer):
    letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    guessed_letters = []
    counter = 0
    line10 = "||/     |"
    line9 = "||      O"
    line8 = "||     /|\\"
    line7 = "||     / \\"
    line6 = "[+]=====+"
    line5 = "||/"
    line4 = "||"
    line3 = "||"
    line2 = "||"
    line1 = "||\_______"
    midlines = [line5, line4, line3, line2]
    midlines_new = [line10, line9, line8, line7]

    hidden_word = []
    for i in range(len(answer)):
            hidden_word.append("_")

    game_end = False
    while game_end == False:

        print(''.join(hidden_word))

        letter_printer(letters, guessed_letters)

        player_guess = guess_validity(letters, guessed_letters)

        correct = checking_guess(player_guess, answer, hidden_word)

        counter = printing_hangman(correct, counter, midlines, midlines_new, line1, line6)

        game_progress = progress_check(answer, counter, hidden_word)

        game_end = game_progress[0]

        result = game_progress[1]

    return result

def letter_printer(letters, guessed_letters):
    for letter in letters:
        if letter in guessed_letters:
            print(letter, end = ' ')
    print()

def guess_validity(letters, guessed_letters):
        guess_check = True
        while guess_check == True:
            player_guess = input("Guess a letter: ")
            if len(player_guess) == 1:
                if player_guess.isdigit() == True or player_guess.upper() not in letters:
                    print("A 'letter' please")
                elif player_guess.upper() in guessed_letters:
                    print("You've guessed this already")
                else:
                    guessed_letters.append(player_guess.upper())
                    guess_check = False
            else:
                print("One at a time")
            print()
        return player_guess.lower()
        
def checking_guess(player_guess, answer, hidden_word):
    correct = False
    for i in range(len(answer)):
        if answer[i] == player_guess:
            hidden_word.pop(i)
            hidden_word.insert(i, player_guess)
            correct = True
    return correct

def printing_hangman(correct, counter, midlines, midlines_new, line1, line6):

    if correct == False:
        counter += 1

    if counter == 0:
        print("||")
    elif counter == 1:
        print(line1)
    elif counter == 2:
        for line in midlines:
            print(line)
        print(line1)
    elif counter == 3:
        print(line6)
        for line in midlines:
            print(line)
        print(line1)
    else:
        replacement = counter - 4
        midlines.pop(replacement)
        midlines.insert(replacement, midlines_new[replacement])
        print(line6)
        for line in midlines:
            print(line)
        print(line1)
    
    print()
    return counter

def progress_check(answer, counter, hidden_word):
    if ''.join(hidden_word) == answer:
        return True, "win"
    elif counter == 6:
        print("Final Guess!")
        return False, "ongoing"
    elif counter == 7:
        return True, "loss"
    else:
        return False, "ongoing"

def end(result, answer):
    if result == "win":
        print(answer)
        print("You saved the man!")
    elif result == "loss":
        print("You hanged the man!")
        print('The answer was "', answer, '"', sep = "")

main()