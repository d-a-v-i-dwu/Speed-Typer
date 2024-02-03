import random
from nltk.corpus import gutenberg

def main():
    continue_game = "Y"
    while continue_game == "Y":
        guessed_letters = []
        answer = word_picker()
        print("=" * 22, "WORDL", "=" * 22)
        print(" " * 13, "GUESS A FIVE LETTER WORD")
        for turn in range(5):
            guess_info = guess_checker(answer)
            if guess_info == "end":
                continue_game = input("\nType Y to play again: ").upper()
                break
            else:
                guess_visualiser(guessed_letters, guess_info)
            if turn == 4:
                print()
                print("=" * 15, "THE WORD WAS:", answer, "=" * 15)
                continue_game = input("\nType Y to play again: ").upper()

def word_picker():
    entire_list = gutenberg.words()
    word_list = []
    for word in entire_list:
        if len(word) == 5 and word.isalpha() == True:
            word_list.append(word.upper())
    return (word_list[random.randrange(len(word_list))])

def guess_visualiser(guessed_letters, guess_info):
    for letter in guess_info[1]:
        if letter not in guessed_letters:
            guessed_letters.append(letter)
    spaces = (51 - (2 * len(guessed_letters) - 1)) // 2
    prev_guess = ''.join(guess_info[0])
    letters = ' '.join(sorted(guessed_letters))
    print(" " * 22, prev_guess)
    print(' ' * spaces, letters, sep = '')

def guess_checker(answer):
    check = True
    while check == True:
        print()
        guess = list(input(" " * 23).upper())
        if guess == list(answer):
            print()
            print(" " * 22, answer)
            print("=" * 17, "CONGRATULATIONS!", "=" * 17)
            return "end"
        guess_list = []
        idx = 0
        temp_list = list(answer)
        if len(guess) != 5:
            print(" " * 16, "A FIVE LETTER WORD")
        elif ''.join(guess).isalpha() == False:
            print(" " * 19, "LETTERS ONLY")
        else:
            for idx in range(5):
                if guess[idx] == answer[idx]:
                    guess_list.append(guess[idx])
                    temp_list.remove(guess[idx])
                else:
                    guess_list.append("-")
            for idx in range(5):
                if guess_list[idx] == "-" and guess[idx] in temp_list:
                    guess_list[idx] = guess[idx].lower()
                    temp_list.remove(guess[idx])
            check = False
    return (guess_list, guess)

main()