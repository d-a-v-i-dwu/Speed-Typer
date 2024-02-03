
# string = "David"
# position = string.find("z")
# print(position)



# 120 Assignment Q1

# print("1a.")
# number = 7
# while number > 0:
#     if (number ** 2) % 8 == 1:
#         print(number, end = " ")
#     number -= 1


# from collections import deque
 
 
# # Recursive function to print all distinct subsets of `S`.
# # `S`   ——> input set
# # `i`   ——> index of next element in set `S` to be processed
# # `out` ——> list to store elements of a subset
# def printPowerSet(S, i, out=deque()):
 
#     # if all elements are processed, print the current subset
#     if i < 0:
#         print(list(out))
#         return
 
#     # include the current element in the current subset and recur
#     out.append(S[i])
#     printPowerSet(S, i - 1, out)
 
#     # backtrack: exclude the current element from the current subset
#     out.pop()
 
#     # remove adjacent duplicate elements
#     while i > 0 and S[i] == S[i - 1]:
#         i = i - 1
 
#     # exclude the current element from the current subset and recur
#     printPowerSet(S, i - 1, out)
 
 
# # Wrapper over `printPowerSet()` function
# def findPowerSet(S):
 
#     # sort the set
#     S.sort()
 
#     # print the power set
#     printPowerSet(S, len(S) - 1)
 
 
# if __name__ == '__main__':
 
#     S = ["d", "e", "l", "t", "a"]
 
#     findPowerSet(S)


# check = True
# while check == True:
#     factors = (input("Enter x: "))
#     try:
#         factors = int(factors)
#         n = 1
#         while n < factors:
#             if factors % n == 0:
#                 if (factors ** 2 + 1) % n == 0:
#                     print(n)
#                     n += 1
#                 else:
#                     n += 1
#             else:
#                 n += 1
#     except ValueError:
#         check = False

# import random
# check = True
# while check == True:
#     number = random.randrange(10, 100)
#     number_sqr = number ** 2
#     string = "What's the square root of " + str(number_sqr) + ": "
#     user_input = input(string)
#     try:
#         if int(user_input) == number:
#             print("yay nice")
#         else:
#             print("nope")
#             print(number)
#     except ValueError:
#         check = False

#     number = random.randrange(10, 100)
#     number_sqr = number ** 2
#     string = "What's the square of " + str(number) + ": "
#     user_input = input(string)
#     try:
#         if int(user_input) == number_sqr:
#             print("yay nice")
#         else:
#             print("nope")
#             print(number_sqr)
#     except ValueError:
#         check = False

# def word_puzzle(horizontal_str,vertical_str):
#     count = 0
#     for ele in horizontal_str:
#         if vertical_str.find(ele) > -1:
#             letter_height = vertical_str.find(ele)
#             letter_width = horizontal_str.find(ele)
#             count += 1
    # if count == 0:
#         print("The strings do not intersect")
#         return
#     tracker = 0
#     for letter in vertical_str:
#         if tracker == 0:
#             if letter_height == vertical_str.find(letter):
#                 print(horizontal_str)
#                 tracker += 1
#             else:
#                 print(" " * letter_width, letter, sep = "")
#         else:
#             print(" " * letter_width, letter, sep = "")
#     else:
#         return

# check = True
# while check:
#     vertical_str = input("Enter the vertical string: ")
#     horizontal_str = input("Enter the horizontal string: ")
#     word_puzzle(horizontal_str, vertical_str)

# a_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
# print(a_tuple[-2], a_tuple[2:5], a_tuple[:4], a_tuple[-4:-1:2])

# a_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
# a_tuple.pop(1)
# print(a_tuple)

# Numbers left [304, 205, 88, 419, 233, 370, 290, 464, 160, 148, 203, 28, 378, 176, 50, 432, 259, 460, 256, 466, 191, 449]

# Numbers left [304, 205, 88, 419, 233, 370, 290, 464, 160, 148, 203, 28, 176, 50, 259, 460, 256, 466, 191, 449]

# def remove_multiples_of_3(numbers):
#     threes = []
#     for ele in numbers:
#         if ele % 3 == 0:
#             threes.append(ele)
#         else:
#             continue
#     print(threes)
#     for ele in threes:
#         ele_pos = numbers.index(ele)
#         numbers.pop(ele_pos)
#     return numbers

# numbers = [304, 205, 88, 419, 233, 370, 290, 464, 90, 160, 148, 203, 28, 363, 378, 176, 186, 50, 105, 432, 259, 460, 256, 466, 191, 449]
# remove_multiples_of_3(numbers)

# t1 = (3, 7, 2, 7, 7, 9, 7)
# values =  []
# while 7 in t1:
#     index = t1.index(7)
#     values.append(index)
#     t1 = t1[index + 1:]
# print(values)

# numbers = [69, 37, 78, 3, 79, 83, 26, 32, 6, 50]

# def double_up(numbers):
#     for ele in numbers:
#         new_number = ele * 2
#         if numbers.count(ele) > 1:
#             ele_pos = numbers.index(ele)
#             a_list = numbers[ele_pos + 1:]
#             b_list = numbers[:ele_pos]
#             number_pos = a_list.index(ele) + len(b_list) + 1
#         else:
#             number_pos = numbers.index(ele)
#         numbers.pop(number_pos)
#         numbers.insert(number_pos, new_number)

# def double_up(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i] * 2
#     return numbers

# print(double_up(numbers))
import random

# def move_random_character_to_end(coins_list):
#     position = random.randrange(len(coins_list))
#     element = coins_list[position]
#     coins_list.pop(position)
#     coins_list.append(element)
    
# def create_coins_list():
#     coins_list = ['-', '$', '-', '$', '-', '$', '-', '$', '-']
#     for i in range(4):
#         move_random_character_to_end(coins_list)
#         print("hi")
#         i += 1

# create_coins_list()

# scores_dict = { 5: ['solve', 'learn', 'enjoy'], 3: ['but', 'all'], 7: ['journey', 'lessons']}

# def print_ascending_descending(scores_dict):
#     key_list = []
#     for ele in scores_dict.keys():
#         key_list.append(ele)
#     for ele in key_list:
#         values = sorted(scores_dict[ele], reverse = True)
#         values = " ".join(values)
#         print("Key = ", ele, " , values = ", values, sep = "")

# print_ascending_descending(scores_dict)

# def do_something():
#     x = []
#     for ele in [1,2,3,4,5,6,7,8,9,10]:
#         if ele <= 4 or ele >= 8 and ele % 2 == 0:
#             x += [ele]
#     print(x)

# do_something()

# def get_sorted_in_parallel(tuples1, tuples2):
#     a_dict = {}
#     for i in range(len(tuples1)):
#         a_dict[tuples1[i]] = tuples2[i]
#     tuple3 = tuple(sorted(tuples1))
#     tuple4 = []
#     sorted_dict = sorted(a_dict.keys())
#     for key in sorted_dict:
#         tuple4.append(a_dict[key])
#     tuple4 = tuple(tuple4)
#     return tuple3, tuple4

	
# data1 = (63, 34, 46, 31, 60, 42, 10, 68, 40, 28)
# data2 = (58, 74, 67, 4, 31, 36, 26, 16, 44, 35)
# tuple3, tuple4 = get_sorted_in_parallel(data1, data2)
# print(data1, "-", data2)
# print(tuple3, "-", tuple4)

def get_longest_increasing(numbers_list):
    starting_index = 0
    longest_chain = 0
    for i in range(len(numbers_list)):
        consecutives = 0
        check = True
        counter = 0
        if i + counter + 1 > len(numbers_list) - 1:
            continue
        while check == True:
            number = numbers_list[i + counter]
            if i + counter + 1 > len(numbers_list) - 1:
                check = False
            else:
                next_number = numbers_list[i + counter + 1]
            if next_number > number:
                counter += 1
                consecutives += 1
            else:
                check = False
        if consecutives > longest_chain:
            starting_index = i
            longest_chain = consecutives
    if longest_chain < 1:
        return None
    else:
        longest_chain += 1
        return starting_index, longest_chain

print(get_longest_increasing([19, 18, 36, 9, 16, 14, 30, 29, 21, 2, 5, 42, 11, 9, 24, 2, 15, 40, 0, 26]))