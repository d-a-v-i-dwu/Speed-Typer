from nltk.corpus import words
import time
import random

words_list = words.words()

def main(words_list):
    print("===SPEED TYPER===")
    time.sleep(0.8)
    loop = True
    while loop == True:
        word_count = number_of_words()
        words = word_generator(word_count, words_list)
        user_performance = typing(words)
        performance = result(user_performance, words)
        loop = print_result(performance)

def number_of_words():
    loop = True
    while loop == True:
        print()
        print("How many words do you want to type?")
        word_count = input()
        try:
            word_count = int(word_count)
            loop = False
        except ValueError:
            print("A number, please")
    return word_count

def word_generator(word_count, words_list):
    words = []
    for i in range(word_count):
        words.append(words_list[random.randrange(len(words_list))])
    words = ' '.join(words)
    return words

def typing(words):
    print()
    print("Type these words as fast as you can:")
    print(words)
    print()
    print("Press Enter to submit")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print('GO!')
    start = time.time()
    user_words = input()
    end = time.time()
    elapsed = end - start
    print()
    return user_words, elapsed

def result(user_performance, words):
    speed = (60 / user_performance[1]) * ((len(words) + 1) / 5)
    speed = round(speed, 2)
    user_words = user_performance[0]
    accuracy_check = min(len(words), len(user_words))
    correct = 0
    for letter in range(accuracy_check):
        if user_words[letter] == words[letter]:
            correct += 1
    accuracy = (correct / len(words)) * 100
    accuracy = round(accuracy, 2)
    return speed, accuracy

def print_result(performance):
    print("You typed at ", performance[0], "WPM", sep = '')
    print("Your accuracy was ", performance[1], "%", sep = '')
    try_again = input("Type 'Y' to try again: ")
    if try_again == "y" or try_again == "Y":
        loop = True
    else:
        loop = False
    return loop

main(words_list)