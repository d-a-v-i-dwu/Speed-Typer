"""
Making a general personality quiz function
"""
import time
import random

def quiz():
    personality1 = ""
    personality2 = ""
    personality3 = ""
    personality4 = ""
    personality5 = ""
    personality_types_list = [personality1, personality2, personality3, personality4, personality5]
    personalities_list = [0, 0, 0, 0, 0]
    print("Format for a personality quiz")
    print()
    question_one(personalities_list)
    question_two(personalities_list)
    question_three(personalities_list)
    result(personalities_list, personality_types_list)

def question_one(personalities_list):
    answers = [("", 0), ("", 1), ("", 2), ("", 3), ("", 4)]
    random.shuffle(answers)
    pretext = ["A)", "B)", "C)", "D)", "E)"]
    print("?")
    print()
    for idx in range(5):
        print(pretext[idx], answers[idx][0])
    personality_position = user_input(answers)
    personality_tracker(personality_position, personalities_list)

def question_two(personalities_list):
    answers = [("", 0), ("", 1), ("", 2), ("", 3), ("", 4)]
    random.shuffle(answers)
    pretext = ["A)", "B)", "C)", "D)", "E)"]
    print("?")
    print()
    for idx in range(5):
        print(pretext[idx], answers[idx][0])
    personality_position = user_input(answers)
    personality_tracker(personality_position, personalities_list)

def question_three(personalities_list):
    answers = [("", 0), ("", 1), ("", 2), ("", 3), ("", 4)]
    random.shuffle(answers)
    pretext = ["A)", "B)", "C)", "D)", "E)"]
    print("?")
    print()
    for idx in range(5):
        print(pretext[idx], answers[idx][0])
    personality_position = user_input(answers)
    personality_tracker(personality_position, personalities_list)

def user_input(answers):
    answer_list = ["A", "B", "C", "D", "E"]
    check = True
    while check:
        answer = input("Your answer: ")
        print()
        try:
            answer = answer.upper()
            if answer in answer_list:
                personality = answers[answer_list.index(answer)][1]
                check = False
            else:
                print("Please answer A, B, C, or D")
        except AttributeError:
            print("Please answer A, B, C, or D")
    return personality
    
def personality_tracker(personality_position, personalities_list):
    personality_value = personalities_list[personality_position] + 1
    personalities_list.pop(personality_position)
    personalities_list.insert(personality_position, personality_value)

def result(personalities_list, personality_types_list):
    personality = max(personalities_list)
    print("Calculating personality...")
    time.sleep(1.5)
    print("Results are in!")
    time.sleep(0.75)
    personality_type = personalities_list.index(personality)
    if personalities_list.count(personality) == 1:
        vowel_list = ["A", "E", "I", "O", "U"]
        if personality_types_list[personality_type][0] in vowel_list:
            determiner = "an"
        else:
            determiner = "a"
        print("You are", determiner, personality_types_list[personality_type])
    else:
        print("It seems you are a mix of personalities!")
        multiple_personalities = []
        check = True
        while check:
            try:
                personality_type = personalities_list.index(personality)
                multiple_personalities.append(personality_types_list[personality_type])
                personalities_list.pop(personality_type)
                personality_types_list.pop(personality_type)
            except ValueError:
                check = False
            except IndexError:
                check = False
        print("You are equal parts ", end = "")
        for ele in multiple_personalities:
            if multiple_personalities.index(ele) == len(multiple_personalities) - 1:
                print("and", ele)
            else:
                print(ele, ", ", sep = "", end = "")
    time.sleep(100000)

quiz()