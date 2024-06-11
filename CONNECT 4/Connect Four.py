"""
My attempt at making connect four
Author: David Wu
"""
line1 = "- 0 - - - - -"
line2 = "x x - - - - -"
line3 = "- x x - - - -"
line4 = "- - x x - - -"
line5 = "- - - x x - -"
line6 = "- - - - - - -"
line7 = "- - - - - - -"
position = "1 2 3 4 5 6 7"

board = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6 + "\n" + line7 + "\n" + position
print(board)

game_progress = True

def player1():

    #Checking player input

    def player_move():
        move = input("Player 1, select a position: ")
        return move
    move = player_move()
    move_position = (int(move) - 1) * 2
    
    def guess_check(move):
        try:
            guess_check = int(move)
        except ValueError:
            print("A number from 1 to 7 please")
            return "retry"
        
        if len(move) > 1:
            print("A number from 1 to 7 please")
            return "retry"
        elif int(move) > 7 or int(move) < 1:
            print("A number from 1 to 7 please")
            return "retry"
        else:
            return "no"
    
    check = guess_check(move)

    while check == "retry":
        move = player_move()
        move_position = (int(move) - 1) * 2
        check = guess_check(move)

    #Enacting player move

    def line1_check():
        global line1
        global line2
        if line1[move_position] == "-" and line2[move_position] == "-":
            return "continue"
        elif line1[move_position]== "-":
            line1 = line1[:move_position] + "0" + line1[(move_position + 1):]
            return "completed"
        else:
            print("Slot is full, pick another")
            return "full"
    
    slot_check = line1_check()

    def line2_check(slot_check):
        global line2
        global line3
        if slot_check == "full":
            return "full"
        elif slot_check == "completed":
            return "completed"
        elif line2[move_position] == "-" and line3[move_position] == "-":
            return "continue"
        else:
            line2 = line2[:move_position] + "0" + line2[(move_position + 1):]
            return "completed"
    
    slot_check = line2_check(slot_check)

    def line3_check(slot_check):
        global line3
        global line4
        if slot_check == "full":
            return "full"
        elif slot_check == "completed":
            return "completed"
        elif line3[move_position] == "-" and line4[move_position] == "-":
            return "continue"
        else:
            line3 = line3[:move_position] + "0" + line3[(move_position + 1):]
            return "completed"
    
    slot_check = line3_check(slot_check)
    
    def line4_check(slot_check):
        global line4
        global line5
        if slot_check == "full":
            return "full"
        elif slot_check == "completed":
            return "completed"
        elif line4[move_position] == "-" and line5[move_position] == "-":
            return "continue"
        else:
            line4 = line4[:move_position] + "0" + line4[(move_position + 1):]
            return "completed"
    
    slot_check = line4_check(slot_check)
        
    def line5_check(slot_check):
        global line5
        global line6
        if slot_check == "full":
            return "full"
        elif slot_check == "completed":
            return "completed"
        elif line5[move_position] == "-" and line6[move_position] == "-":
            return "continue"
        else:
            line5 = line5[:move_position] + "0" + line5[(move_position + 1):]
            return "completed"
    
    slot_check = line5_check(slot_check)
        
    def line6_check(slot_check):
        global line6
        global line7
        if slot_check == "full":
            return "full"
        elif slot_check == "completed":
            return "completed"
        elif line6[move_position] == "-" and line7[move_position] == "-":
            return "continue"
        else:
            line6 = line6[:move_position] + "0" + line6[(move_position + 1):]
            return "completed"
    
    slot_check = line6_check(slot_check)

    def line7_check(slot_check):
        global line7
        if slot_check == "full":
            return "full"
        elif slot_check == "completed":
            return "completed"
        else:
            line7 = line7[:move_position] + "0" + line7[(move_position + 1):]
            return "completed"
    slot_check = line7_check(slot_check)

    while slot_check == "full":
        move = player_move()
        check = guess_check(move)
        move_position = int(move) * 2
        slot_check = line1_check()
        slot_check = line2_check(slot_check)
        slot_check = line3_check(slot_check)
        slot_check = line4_check(slot_check)
        slot_check = line5_check(slot_check)
        slot_check = line6_check(slot_check)
        slot_check = line7_check(slot_check)

    #Checking for a win in columns
    
    def column_check1():
        column = line7[0] + line6[0] +line5[0] + line4[0] +line3[0] + line2[0] + line1[0]
        ele_position = column.rfind("0")
        try:
            if column[ele_position] == "0" and column[ele_position] == column[ele_position - 1] and column[ele_position] == column[ele_position - 2] and column[ele_position] == column[ele_position - 3]:
                print("done")
                return False
            else:
                return True
        except IndexError:
            return True
    game_progress = column_check1()

    def column_check2():
        column = line7[2] + line6[2] +line5[2] + line4[2] +line3[2] + line2[2] + line1[2]
        ele_position = column.rfind("0")
        if game_progress == False:
            return False
        else:
            try:
                if column[ele_position] == "0" and column[ele_position] == column[ele_position - 1] and column[ele_position] == column[ele_position - 2] and column[ele_position] == column[ele_position - 3]:
                    return False
                else:
                    return True
            except IndexError:
                return True
    game_progress = column_check2()

    def column_check3():
        column = line7[4] + line6[4] +line5[4] + line4[4] +line3[4] + line2[4] + line1[4]
        ele_position = column.rfind("0")
        if game_progress == False:
            return False
        else:
            try:
                if column[ele_position] == "0" and column[ele_position] == column[ele_position - 1] and column[ele_position] == column[ele_position - 2] and column[ele_position] == column[ele_position - 3]:
                    return False
                else:
                    return True
            except IndexError:
                return True
    game_progress = column_check3()

    def column_check4():
        column = line7[6] + line6[6] +line5[6] + line4[6] +line3[6] + line2[6] + line1[6]
        ele_position = column.rfind("0")
        if game_progress == False:
            return False
        else:
            try:
                if column[ele_position] == "0" and column[ele_position] == column[ele_position - 1] and column[ele_position] == column[ele_position - 2] and column[ele_position] == column[ele_position - 3]:
                    return False
                else:
                    return True
            except IndexError:
                return True
    game_progress = column_check4()

    def column_check5():
        column = line7[8] + line6[8] +line5[8] + line4[8] +line3[8] + line2[8] + line1[8]
        ele_position = column.rfind("0")
        if game_progress == False:
            return False
        else:
            try:
                if column[ele_position] == "0" and column[ele_position] == column[ele_position - 1] and column[ele_position] == column[ele_position - 2] and column[ele_position] == column[ele_position - 3]:
                    return False
                else:
                    return True
            except IndexError:
                return True
    game_progress = column_check5()

    def column_check6():
        column = line7[10] + line6[10] +line5[10] + line4[10] +line3[10] + line2[10] + line1[10]
        ele_position = column.rfind("0")
        if game_progress == False:
            return False
        else:
            try:
                if column[ele_position] == "0" and column[ele_position] == column[ele_position - 1] and column[ele_position] == column[ele_position - 2] and column[ele_position] == column[ele_position - 3]:
                    return False
                else:
                    return True
            except IndexError:
                return True
    game_progress = column_check6()

    def column_check7():
        column = line7[12] + line6[12] +line5[12] + line4[12] +line3[12] + line2[12] + line1[12]
        ele_position = column.rfind("0")
        if game_progress == False:
            return False
        else:
            try:
                if column[ele_position] == "0" and column[ele_position] == column[ele_position - 1] and column[ele_position] == column[ele_position - 2] and column[ele_position] == column[ele_position - 3]:
                    return False
                else:
                    return True
            except IndexError:
                return True
    game_progress = column_check7()

    #Checking for a win in diagonals

    def down_diagonal_check1():
        line1_list = line1.split(" ")
        global game_progress
        for ele in line1_list:
            ele_position = line1_list.index(ele)
            print(ele, ele_position)
            if game_progress == False:
                game_progress = False
            else:
                try:
                    if line1_list[ele_position] == "0" and line1_list[ele_position] == line2[ele_position + 2] and line1_list[ele_position] == line3[ele_position + 4] and line1_list[ele_position] == line4[ele_position + 6]:
                        game_progress = False
                    else:
                        game_progress = True
                except IndexError:
                    game_progress = True
        return game_progress
    game_progress = down_diagonal_check1()

    def down_diagonal_check2():
        ele_position = line2.find("0")
        if game_progress == False:
            return False
        else:
            try:
                if line2[ele_position] == "0" and line2[ele_position] == line3[ele_position + 2] and line2[ele_position] == line4[ele_position + 4] and line2[ele_position] == line5[ele_position + 6]:
                    return False
                else:
                    return True
            except IndexError:
                return True
    game_progress = down_diagonal_check2()

    def down_diagonal_check3():
        ele_position = line3.find("0")
        if game_progress == False:
            return False
        else:
            try:
                if line3[ele_position] == "0" and line3[ele_position] == line4[ele_position + 2] and line3[ele_position] == line5[ele_position + 4] and line3[ele_position] == line6[ele_position + 6]:
                    return False
                else:
                    return True
            except IndexError:
                return True
    game_progress = down_diagonal_check3()

    def down_diagonal_check4():
        ele_position = line4.find("0")
        if game_progress == False:
            return False
        else:
            try:
                if line4[ele_position] == "0" and line4[ele_position] == line5[ele_position + 2] and line4[ele_position] == line6[ele_position + 4] and line4[ele_position] == line7[ele_position + 6]:
                    return False
                else:
                    return True
            except IndexError:
                return True
    game_progress = down_diagonal_check4()


    return game_progress



def player2():
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)
    print(position)

while game_progress == True:
    game_progress = player1()
    player2()
else:
    print("Game Over!")