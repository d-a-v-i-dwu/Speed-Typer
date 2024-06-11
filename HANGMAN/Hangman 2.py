"""
First try at Hangman
Author: David Wu
"""
import time

def main():
    print("===WELCOME TO HANGMAN===")
    print()
    intro()
    answer = "i like you"
    result = gamecode(answer)
    end(result, answer)
    print()

def intro():
    time.sleep(1)

    print("Generating words...")
    time.sleep(0.8)

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
    line1 = r"||\_______"
    midlines = [line5, line4, line3, line2]
    midlines_new = [line10, line9, line8, line7]

    hidden_word = ["_", " ", "_", "_", "_", "_", " ", "_", "_", "_"]

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
        if letter not in guessed_letters:
            print(letter, end = ' ')
    print()

def guess_validity(letters, guessed_letters):
        guess_check = True
        while guess_check == True:
            player_guess = input("Guess a letter or the phrase: ")
            if len(player_guess) == 1:
                if player_guess.isdigit() == True or player_guess.upper() not in letters:
                    print("A 'letter' or phrase please")
                elif player_guess.upper() in guessed_letters:
                    print("You've guessed this already")
                else:
                    guessed_letters.append(player_guess.upper())
                    guess_check = False
            elif len(player_guess) == 10:
                guess_check = False
            else:
                print("One at a time or all at once")
            print()
        return player_guess.lower()
        
def checking_guess(player_guess, answer, hidden_word):
    if player_guess == answer:
        for i in range(len(answer)):
            hidden_word.pop(i)
            hidden_word.insert(i, answer[i])
            correct = True
    else:
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

    if counter == 0 and not correct:
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
        print()
        print("You saved the man! It seems as though he's taken a liking to you")
        time.sleep(0.8)
        print()
        like = input("Do you like him back? (Y/N): ")
        time.sleep(0.01)
        print()
        print("Processing...")
        time.sleep(1.2)
        print()

        if like.lower() == "y":
            print("Such splendid input to his terminal!")
            time.sleep(0.99)
            smile = "            ██████████              \n        ████          ██████        \n      ██                    ██      \n    ████  ████      ████    ████    \n  ██▒▒▒▒██▒▒▒▒██  ██▒▒▒▒████▒▒▒▒██  \n  ██▒▒▒▒▒▒▒▒▒▒██  ██▒▒▒▒▒▒▒▒▒▒▒▒██  \n██  ██▒▒▒▒▒▒██      ██▒▒▒▒▒▒▒▒██  ██\n██    ██▒▒██          ██▒▒▒▒██    ██\n██    ░░██  ░░  ░░░░    ██▓▓      ██\n██                                ██\n██    ████████████████████████    ██\n  ██    ██              ████    ██  \n  ██      ██████████████        ██  \n    ██      ██████████        ██    \n      ██      ██████        ██      \n        ████          ██████        \n            ██████████       "
            for ele in smile:
                time.sleep(0.01)
                print(ele, end = "")
            print()
            print()
            time.sleep(1)
            print(" " * 7, "What a happy ending :)")
        else:
            print("That's too bad :(")
    elif result == "loss":
        print("You hanged the man!")
        print('The answer was "', answer, '"', sep = "")

main()