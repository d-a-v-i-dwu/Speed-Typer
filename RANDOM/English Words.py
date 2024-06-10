from nltk.corpus import words
import random

words = words.words()

word_count = input("Word count: ")

def word_generator(word_count):
    words = []
    words_list = words.words()
    for i in range(word_count):
        words.append(words_list[random.randrange(len(words_list))])
    words = ' '.join(words)
    print(words)

word_generator(word_count)