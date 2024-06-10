def main():
    """Execute the Mastermind program"""
    display_list = ["----------","Code||Mark","----------","....||....","....||....","....||....","....||....","....||....","....||....","....||....","....||....","....||....","....||....","----------"]
    display_board(display_list)
    turn_counter = 1
    valid_guesses = []
    valid_choices = ["r","o","y","g","b","v"]
    n = 4
    hidden_code = generate_goal(valid_choices, n)
    valid_guesses += [guess(turn_counter)]
    x = 0
    display_list[turn_counter + 2] = f"{valid_guesses[0]}||{check_valid_guess(valid_guesses, hidden_code, x)}"
    display_board(display_list)
    if check_valid_guess(valid_guesses, hidden_code, x) == "BBBB":
        return print("You win!")
    else:
        turn_counter += 1
        valid_guesses += [guess(turn_counter)]
        x = 1
        display_list[turn_counter + 2] = f"{valid_guesses[1]}||{check_valid_guess(valid_guesses, hidden_code, x)}"
        display_board(display_list)
        if check_valid_guess(valid_guesses, hidden_code, x) == "BBBB":
            return print("You win!")
        else:
            turn_counter += 1
            valid_guesses += [guess(turn_counter)]
            x = 2
            display_list[turn_counter + 2] = f"{valid_guesses[2]}||{check_valid_guess(valid_guesses, hidden_code, x)}"
            display_board(display_list)
            if check_valid_guess(valid_guesses, hidden_code, x) == "BBBB":
                return print("You win!")
            else:
                turn_counter += 1
                valid_guesses += [guess(turn_counter)]
                x = 3 
                display_list[turn_counter + 2] = f"{valid_guesses[3]}||{check_valid_guess(valid_guesses, hidden_code, x)}"
                display_board(display_list)
                if check_valid_guess(valid_guesses, hidden_code, x) == "BBBB":
                    return print("You win!")
                else:
                    turn_counter += 1
                    valid_guesses += [guess(turn_counter)]
                    x = 4
                    display_list[turn_counter + 2] = f"{valid_guesses[4]}||{check_valid_guess(valid_guesses, hidden_code, x)}"
                    display_board(display_list)
                    if check_valid_guess(valid_guesses, hidden_code, x) == "BBBB":
                        return print("You win!")
                    else:
                        turn_counter += 1
                        valid_guesses += [guess(turn_counter)]
                        x = 5
                        display_list[turn_counter + 2] = f"{valid_guesses[5]}||{check_valid_guess(valid_guesses, hidden_code, x)}"
                        display_board(display_list)
                        if check_valid_guess(valid_guesses, hidden_code, x) == "BBBB":
                            return print("You win!")
                        else:
                            turn_counter += 1
                            valid_guesses += [guess(turn_counter)]
                            x = 6
                            display_list[turn_counter + 2] = f"{valid_guesses[6]}||{check_valid_guess(valid_guesses, hidden_code, x)}"
                            display_board(display_list)
                            if check_valid_guess(valid_guesses, hidden_code, x) == "BBBB":
                                return print("You win!")
                            else:
                                turn_counter += 1
                                valid_guesses += [guess(turn_counter)]
                                x = 7
                                display_list[turn_counter + 2] = f"{valid_guesses[7]}||{check_valid_guess(valid_guesses, hidden_code, x)}"
                                display_board(display_list)
                                if check_valid_guess(valid_guesses, hidden_code, x) == "BBBB":
                                    return print("You win!")
                                else:
                                    turn_counter += 1
                                    valid_guesses += [guess(turn_counter)]
                                    x = 8
                                    display_list[turn_counter + 2] = f"{valid_guesses[8]}||{check_valid_guess(valid_guesses, hidden_code, x)}"
                                    display_board(display_list)
                                    if check_valid_guess(valid_guesses, hidden_code, x) == "BBBB":
                                        return print("You win!")
                                    else:
                                        turn_counter += 1
                                        valid_guesses += [guess(turn_counter)]
                                        x = 9
                                        display_list[turn_counter + 2] = f"{valid_guesses[9]}||{check_valid_guess(valid_guesses, hidden_code, x)}"
                                        display_board(display_list)
                                        turn_counter += 1
                                        print("You lose!")
    
    
def guess(turn_counter):
    """Confirming and processing user guess"""
    guess_list  = ["r","o","y","g","b","v"]
    counter = 0
    while counter != 4:
        user_input = input(f"{turn_counter} (roygbv): ")
        if len(user_input) == 4:
            counter = 0 
            for i in range(len(user_input)):
                if user_input[i] in guess_list:
                    counter += 1
    else:
            return (user_input)
        
def check_valid_guess(valid_guesses, hidden_code, x):
    user_guess = []
    user_guess += valid_guesses[x]
    hidden_code_list = []
    hidden_code_list += hidden_code
    exact_match_string = ""
    for i in range(len(user_guess)):
        if user_guess[i] == hidden_code_list[i]:
            exact_match_string += "B"
            user_guess[i] = "-"
            hidden_code_list[i] = "-"
    exact_match_string += white_peg_check(user_guess, hidden_code_list)
    while len(exact_match_string) != 4:
        exact_match_string += "."
    return exact_match_string

def white_peg_check(user_guess, hidden_code_list):
    white_peg_count = ""
    for i in range(len(user_guess)):
        if user_guess[i].isalpha() and user_guess[i] in hidden_code_list:
            white_peg_count += "W"
            hidden_code_list.remove(user_guess[i])
            user_guess[i] = "-"
    return white_peg_count
        
import random
def generate_goal(valid_choices, n):
    """Given a string of letters and an integer value n,
    return a string containing a random selection of n characters
    selected from the letters in valid_choices"""
    goal = ""
    for i in range(0, n):
        goal += random.choice(valid_choices)    
    return goal

def display_board(display_list):
    """Display the Mastermind board"""
    for i in range(len(display_list)):
        print(display_list[i])
        
main()
