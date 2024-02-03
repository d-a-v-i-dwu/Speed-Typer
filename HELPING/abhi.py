sentence = input("Please enter a sentence: ")
word_list = sentence.split()
uniques = []

for word in word_list:
    if word not in uniques:
        uniques.append(word)
    else:
        continue

print("Unique words: ", sep = '', end = '')

uniques.reverse()

for word in uniques:
    if uniques.index(word) == len(uniques) - 1:
        print(word)
    else:
        print(word, ", ", sep = '', end = '')