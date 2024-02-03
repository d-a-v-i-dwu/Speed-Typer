"""
number = input()
def number_check(number):
    if int(number) > 4:
        print("yo")
    else:
        print("no")
        return
number_check(number)
"""
"""
thing = input("yo")
def check(thing):
    if thing == "p":
        print("yay")
        return "hi"
    else:
        return
outcome = check(thing)
print(outcome)
"""
"""
line1 = "1234567890"
line2 = "1234567890"
column1 = line1[0] + line2[0]

user = input("pick a number")

def letter_change():
    global line1
    global line2
    line1 = "01234567890"
    return line1
letter_change()

print(line1)
print(column1)
"""
"""
string = "- - - - - -"

progress = True
def x_list():
    string_list = string.split(" ")
    for x in string_list:
        x_pos = string_list.index(x)
        print(x_pos)
        if progress == False:
            print("False")
        else:
            print("hello")
x_list()

line1 = "- - - - - - -"

game_progress = False

def down_diagonal_check1():
    line1_list = line1.split(" ")
    print(line1_list)
    for ele in line1_list:
        ele_position = line1_list.index(ele)
        print(ele_position)
        if game_progress == False:
            print("False")
        else:
            print("True")
game_progress = down_diagonal_check1()
"""
"""
word = "hello"
sentence = "hi there hello my friend"
word_pos = sentence.find(word)
print(word_pos)
"""
string = "-  -  -  -  -  -  -\n"
print(len(string))