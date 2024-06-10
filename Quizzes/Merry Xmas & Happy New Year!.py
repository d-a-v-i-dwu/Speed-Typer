"""
Making a general personality quiz function
"""
import time
import random
def quiz():
    personality1 = "Fran"
    personality2 = "David"
    personality3 = "Fred"
    personality4 = "Peanut"
    personality5 = "Yarrick"
    personality_types_list = [personality1, personality2, personality3, personality4, personality5]
    personalities_list = [0, 0, 0, 0, 0]
    print("Hello!")
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    print("What better way to celebrate a new year than to see who you've become in this last one with a\nlittle personality quiz?")
    time.sleep(4)
    print()
    print("So, welcome to:")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("Which personality are you from David and Fran's lives?")
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    print()
    time.sleep(2)
    question_one(personalities_list)
    question_two(personalities_list)
    question_three(personalities_list)
    question_four(personalities_list)
    question_five(personalities_list)
    question_six(personalities_list)
    question_seven(personalities_list)
    result(personalities_list, personality_types_list)

def question_one(personalities_list):
    answers = [("Fox", 0), ("Monkey", 1), ("Possum", 2), ("Raccoon", 3), ("Brown bear", 4)]
    random.shuffle(answers)
    pretext = ["A)", "B)", "C)", "D)", "E)"]
    print("What animal were you in your past life?")
    print()
    for idx in range(5):
        print(pretext[idx], answers[idx][0])
    personality_position = user_input(answers)
    personality_tracker(personality_position, personalities_list)
    
def question_two(personalities_list):
    answers = [("The intimate parts of Europe", 0), ("The heaven on Earth known as Rarotonga", 1), ("470 Mount Eden Road", 2), ("The bedroom of a vulnerable girl", 3), ("The gym or anywhere you can bring your Nintendo Switch", 4)]
    random.shuffle(answers)
    pretext = ["A)", "B)", "C)", "D)", "E)"]
    print("What's your dream holiday getaway?")
    print()
    for idx in range(5):
        print(pretext[idx], answers[idx][0])
    personality_position = user_input(answers)
    personality_tracker(personality_position, personalities_list)

def question_three(personalities_list):
    answers = [("Someone who holds you in their heart above everyone else, yet is still able to maintain a fruitful life outside of\nyour relationship", 0), ("You but the opposite gender", 1), ("Someone you work with who can match your skills and careless yet professional vibe", 2), ("A cute, indie, alty girl who will adore your work and admire your big words", 3), ("Princess Peach, or maybe Princess Daisy. You'll have to confirm with your mum", 4)]
    random.shuffle(answers)
    pretext = ["A)", "B)", "C)", "D)", "E)"]
    print("What is your dream partner like?")
    print()
    for idx in range(5):
        print(pretext[idx], answers[idx][0])
    personality_position = user_input(answers)
    personality_tracker(personality_position, personalities_list)
    
def question_four(personalities_list):
    answers = [("Be a passenger princess", 0), ("Complain but drive anyways", 1), ("Speed and make everyone in the car nervous", 2), ('"Walk ominously"', 3), ("Take the bus with your mum", 4)]
    random.shuffle(answers)
    pretext = ["A)", "B)", "C)", "D)", "E)"]
    print("If you had to get somewhere, how would you do it?")
    print()
    for idx in range(5):
        print(pretext[idx], answers[idx][0])
    personality_position = user_input(answers)
    personality_tracker(personality_position, personalities_list)

def question_five(personalities_list):
    answers = [("Book editor/publisher", 0), ("Software engineer", 1), ("Bartender", 2), ("Pretentious poet", 3), ("Twitch streamer", 4)]
    random.shuffle(answers)
    pretext = ["A)", "B)", "C)", "D)", "E)"]
    print("What's your dream job?")
    print()
    for idx in range(5):
        print(pretext[idx], answers[idx][0])
    personality_position = user_input(answers)
    personality_tracker(personality_position, personalities_list)
    
def question_six(personalities_list):
    answers = [("Gardening, reading, and spending time with family", 0), ("Gaming with friends or combatting the fear of having schizophrenia and autism", 1), ("At work because that's the only thing you know", 2), ("Writing love poems and self insert fanfics", 3), ("Playing videogames or watching anime. Alone.", 4)]
    random.shuffle(answers)
    pretext = ["A)", "B)", "C)", "D)", "E)"]
    print("How do you like to spend a day off?")
    print()
    for idx in range(5):
        print(pretext[idx], answers[idx][0])
    personality_position = user_input(answers)
    personality_tracker(personality_position, personalities_list)

def question_seven(personalities_list):
    answers = [("That they worship you above everyone and everything", 0), ("Having the same sense of humor", 1), ("Them rivaling your love for hospitality", 2), ("That it ends with you getting some", 3), ("Their adoration of your extensive knowledge about anime and videogames", 4)]
    random.shuffle(answers)
    pretext = ["A)", "B)", "C)", "D)", "E)"]
    print("What do you value most in a friendship?")
    print()
    for idx in range(5):
        print(pretext[idx], answers[idx][0])
    personality_position = user_input(answers)
    personality_tracker(personality_position, personalities_list)

def user_input(answers):
    answer_list = ["A", "B", "C", "D", "E"]
    interludes = ["Really?!", "That's a surprise", "Very revealing...", "Why would you pick that..?", "That's... definitely an answer!", "Of course you would pick that", "Taking that into account...", "How unexpected", "Oh, interesting...", "Good pick!", "How unique", "That says a lot about you", "I can see why you chose that", "Interesting choice!"]
    check = True
    while check:
        answer = input("Your answer: ")
        print()
        try:
            answer = answer.upper()
            if answer in answer_list:
                personality = answers[answer_list.index(answer)][1]
                time.sleep(0.5)
                if personality > 1:
                    print(interludes[random.randrange(len(interludes))])
                else:
                    print(interludes[random.randrange(8,len(interludes))])
                check = False
            else:
                print("Please answer A, B, C, D, or E")
        except AttributeError:
            print("Please answer A, B, C, D, or E")
    print()
    print()
    time.sleep(1)
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
        print("You got:", personality_types_list[personality_type])
        explanations([personality_types_list[personality_type]])
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
            except:
                check = False
        print("You are equal parts ", end = "")
        if len(multiple_personalities) == 2:
            print(multiple_personalities[0], "and", multiple_personalities[1])
        else:
            for ele in multiple_personalities:
                if multiple_personalities.index(ele) == len(multiple_personalities) - 1:
                    print("and", ele)
                else:
                    print(ele, ", ", sep = "", end = "")
        explanations(multiple_personalities)

def explanations(personalities):
    explanations = [("Fran", "You're a witty, funny, and interesting individual who has a gravity that attracts those around you.\n\nYou likely give off the impression of having a simple life, but are still somehow a constant stream of\ndelightful surprises even to people who'd like to think they know you well.\n\nYou have many admirable talents and skills, and are projected to have a wonderful year ahead.\n\nBut, alas, there is one personality that's better."), ("David", "Well done, you got the best one."), ("Fred", "Work is the number one thing in your life, and you flaunt that fact unapologetically.\n\nYou were raised rich and are now a pretentious, slimy asshole, whether you realize it or not.\n\nYou're probably a little creepy around younger girls, but your type is still mature women\n(minimum 10yrs hospo experience)."), ("Peanut", "You're the type of person to call chasing after women a form of art, even though it's one you're not\nparticularly good at.\n\nYou enjoy writing not because it's a means of catharsis, but rather because you see it as a tool to\nimpress people.\n\nYou have a tendency to do cringe things that are painful even just to hear about, and your excuses\ninvolve either alcohol or your" +  ' "mates."'), ("Yarrick", "You're potentially a tad racist and misogynistic, traits which are inherited from your\nmother who is the central figure in your life\n\nYou likely have one ancient friend who you reference non-stop and who you reminisce about daily, even\nthough he hasn't talked to nor though of you since you parted ways five years ago.\n\nYou like putting on an air of superiority around people you're older than, despite\nyou having arguably fewer life achievements and prospects.")]
    print()
    time.sleep(1)
    print("But what does this mean?")
    print()
    time.sleep(1)
    for ele in explanations:
        if ele[0] in personalities:
            print(ele[0], ":", sep='')
            print()
            print(ele[1])
            print("--------------------------------")
            print()
    time.sleep(10000)

quiz()