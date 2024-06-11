# check = True
# total = 0
# tally = 0

# while check == True:
#     number = float(input("Enter a number: "))
#     if number > 0:
#         total += number
#         tally += 1
#     else:
#         check = False

# if total <= 0:
#     print("Average undefined")
# else:
#     average = round(total / tally, 2)
#     print("Average:", average)


# " Pell's number "
# def get_pell_number():
#     number = int(input("n = "))

#     retain1 = 0
#     retain2 = 1
#     current = 0
#     n = 1
#     while n < number:
#         current = (retain2 * 2) + retain1
#         retain1 = retain2
#         retain2 = current
#         n += 1
#         print(retain1, retain2, current)
#     return retain2

# print(get_pell_number())

# def main():
#     """Execute the Mastermind program"""
#     turn_counter = 1
#     turn_counter = guess(turn_counter)
#     turn_counter = guess(turn_counter)
#     turn_counter = guess(turn_counter)
#     turn_counter = guess(turn_counter)
#     turn_counter = guess(turn_counter)
#     turn_counter = guess(turn_counter)
#     turn_counter = guess(turn_counter)
#     turn_counter = guess(turn_counter)
#     turn_counter = guess(turn_counter)
#     turn_counter = guess(turn_counter)
    

    
# def guess(turn_counter):
#     display_board()
#     """Confirming and processing user guess"""
#     guess_list  = ["r","o","y","g","b","v"]
#     counter = 0
#     while counter != 4:
#         user_input = input(f"{turn_counter} (roygbv): ")
#         if len(user_input) == 4:
#             counter = 0 
#             for i in range(len(user_input)):
#                 if user_input[i] in guess_list:
#                     counter += 1
#     else:
#             new_counter = turn_counter + 1
#             return new_counter
        
        

# def display_board():
#     """Display the Mastermind board"""
#     print("----------")
#     print("Code||Mark")
#     print("----------")
#     print("....||....")
#     print("....||....")
#     print("....||....")
#     print("....||....")
#     print("....||....")
#     print("....||....")
#     print("....||....")
#     print("....||....")
#     print("....||....")
#     print("....||....")
#     print("----------")
    
# main()