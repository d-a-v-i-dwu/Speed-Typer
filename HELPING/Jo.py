# def num_new_points(self, column, row, player):
#         four_in_a_row = 0

#         # To the left
#         count = 0
#         for c in range(column, -1, -1):
#             if self.items[c][row] == player:
#                 count += 1
#             else:
#                 break
#         if count > 3:
#             four_in_a_row += 1

#         # To the right
#         count = 0
#         for c in range(column, self.size - 1):
#             if self.items[c][row] == player:
#                 count += 1
#             else:
#                 break
#         if count > 3:
#             four_in_a_row += 1

#         # To the bottom
#         count = 0
#         for r in range(row, -1, -1):
#             if self.items[column][r] == player:
#                 count += 1
#             else:
#                 break
#         if count > 3:
#             four_in_a_row += 1
        
#         # To the bottom left
#         count = 0
#         idx = 0
#         while self.size > column - idx > -1 and self.size > row - idx > -1:
#             if self.items[column - idx][row - idx] == player:
#                 count += 1
#             else:
#                 break
#             idx += 1
#         if count > 3:
#             four_in_a_row += 1

#         # To the bottom right
#         count = 0
#         idx = 0
#         while self.size > column + idx > -1 and self.size > row - idx > -1:
#             if self.items[column + idx][row - idx] == player:
#                 count += 1
#             else:
#                 break
#             idx += 1
#         if count > 3:
#             four_in_a_row += 1

#         # To the top right
#         count = 0
#         idx = 0
#         while self.size > column + idx > -1 and self.size > row + idx > -1:
#             if self.items[column + idx][row + idx] == player:
#                 count += 1
#             else:
#                 break
#             idx += 1
#         if count > 3:
#             four_in_a_row += 1

#         # To the top left
#         count = 0
#         idx = 0
#         while self.size > column - idx > -1 and self.size > row + idx > -1:
#             if self.items[column - idx][row + idx] == player:
#                 count += 1
#             else:
#                 break
#             idx += 1
#         if count > 3:
#             four_in_a_row += 1

#         return four_in_a_row

""" 
Modified Connect Four Board Game

dwu963 515331201
"""

class GameBoard:
    def __init__(self, size):
        self.size = size
        self.num_entries = [0] * size
        self.items = [[0] * size for i in range(size)]
        self.points = [0] * 2
        self.player_slots = [[],[]]

    def num_free_positions_in_column(self, column):
        free = 0
        for item in self.items[column]:
            if item == 0:
                free += 1
        return free
        
    def game_over(self):
        game_over = True
        for var in self.num_entries:
            if var < self.size:
                game_over = False
        return game_over
        
    def display(self):
        for i in range(self.size-1,-1,-1):
            string = ''
            for j in range(self.size):
                if self.items[j][i] == 1:
                    string += "o "
                elif self.items[j][i] == 2:
                    string += "x "
                else:
                    string += "  "
            print(string)
        print("-" * (self.size * 2 - 1))
        slots = ''
        for i in range(self.size):
            slots += str(i) + ' '
        print(slots)
        print(f"Points player 1: {self.points[0]}\nPoints player 2: {self.points[1]}")

    def num_new_points(self, column, row, player):
        four_in_a_row = 0
        horizontal = [False, False, 0]
        diagonal_left = [False, False, 0]
        diagonal_right = [False, False, 0]
        # To the left
        count = 0
        for c in range(column - 1, -1, -1):
            if self.items[c][row] == player:
                count += 1
                horizontal[0] = True
                horizontal[2] += 1
            else:
                break
        if count > 2:
            four_in_a_row += 1
        print("l", count)

        # To the right
        count = 0
        for c in range(column + 1, self.size - 1):
            if self.items[c][row] == player:
                horizontal[1] = True
                horizontal[2] += 1
                count += 1
            else:
                break
        if count > 2:
            four_in_a_row += 1
        print("r", count)

        # To the bottom
        count = 0
        for r in range(row, -1, -1):
            if self.items[column][r] == player:
                count += 1
            else:
                break
        if count > 3:
            four_in_a_row += 1
        
        # To the bottom left
        count = 0
        idx = 1
        while self.size > column - idx > -1 and self.size > row - idx > -1:
            if self.items[column - idx][row - idx] == player:
                diagonal_right[0] = True
                diagonal_right[2] += 1
                count += 1
            else:
                break
            idx += 1
        if count > 2:
            four_in_a_row += 1
        print("bl", count)

        # To the bottom right
        count = 0
        idx = 1
        while self.size > column + idx > -1 and self.size > row - idx > -1:
            if self.items[column + idx][row - idx] == player:
                diagonal_left[0] = True
                diagonal_left[2] += 1
                count += 1
            else:
                break
            idx += 1
        if count > 2:
            four_in_a_row += 1
        print("br", count)

        # To the top right
        count = 0
        idx = 1
        while self.size > column + idx > -1 and self.size > row + idx > -1:
            if self.items[column + idx][row + idx] == player:
                diagonal_right[1] = True
                diagonal_right[2] += 1
                count += 1
            else:
                break
            idx += 1
        if count > 2:
            four_in_a_row += 1
        print("tr", count)

        # To the top left
        count = 0
        idx = 1
        while self.size > column - idx > -1 and self.size > row + idx > -1:
            if self.items[column - idx][row + idx] == player:
                diagonal_left[1] = True
                diagonal_left[2] += 1
                count += 1
            else:
                break
            idx += 1
        print("tl", count)
        if count > 2:
            four_in_a_row += 1

        if horizontal[0] and horizontal[1] and horizontal[2] > 3:
            four_in_a_row += 1
        if diagonal_left[0] and diagonal_left[1] and diagonal_left[2] > 3:
            four_in_a_row += 1
        if diagonal_right[0] and diagonal_right[1] and diagonal_right[2] > 3:
            four_in_a_row += 1
        
        if horizontal[0] and horizontal[1] and horizontal[2] == 3:
            four_in_a_row += 1
        if diagonal_left[0] and diagonal_left[1] and diagonal_left[2] == 3:
            four_in_a_row += 1
        if diagonal_right[0] and diagonal_right[1] and diagonal_right[2] == 3:
            four_in_a_row += 1

        return four_in_a_row

    def add(self, column, player):
        global ghost
        ghost = False
        if self.num_entries[column] >= self.size or column < 0 or column >= self.size:
            return False
        row = self.num_entries[column]
        self.items[column][row] = player
        self.num_entries[column] += 1
        self.points[player - 1] += self.num_new_points(column, row, player)

        self.display()

        return True
        
    def free_slots_as_close_to_middle_as_possible(self):
        free_slots = []
        if self.size % 2 == 0:
            middle = self.size // 2 - 1
            j = 1
        else:
            middle = self.size // 2
            j = 0
        check = True
        i = 0
        while check == True:
            try:
                if self.num_entries[middle - i] < self.size and middle - i not in free_slots and middle - i >= 0:
                    free_slots.append(middle - i)
            except IndexError:
                check = False
            try:
                if self.num_entries[middle + i + j] < self.size and middle + i + j not in free_slots:
                    free_slots.append(middle + i + j)
            except IndexError:
                check = False
            i += 1
        return free_slots
    
    def column_resulting_in_max_points(self, player):
        global ghost
        maximum = [0, 0]
        free_slots = self.free_slots_as_close_to_middle_as_possible()
        for i in range(self.size):
            if self.num_entries[i] < self.size:
                row = self.num_entries[i]
                ghost = True
                test_value = self.num_new_points(i, row, player)
                if test_value > maximum[0]:
                    maximum[0], maximum[1] = test_value, i
                elif i in free_slots and maximum[1] in free_slots:
                    if test_value == maximum[0] and free_slots.index(i) < free_slots.index(maximum[1]):
                        maximum[1] = i
        return(maximum[1], maximum[0])

def column_resulting_in_max_points(self, player):
        current_score = self.points[player - 1]
        max_score = 0
        slots = self.free_slots_as_close_to_middle_as_possible()

        four_in_row_set = {}
        if slots:
            slot = slots[0]

            self.items[slot][self.num_entries[slot]] = player

            for column in range(self.size):
                for row in range(self.size):

                    max_score += self.num_new_points(column, row, player)

            self.items[slot][self.num_entries[slot]] = 0

            if max_score > current_score:
                return slot, max_score - current_score

        middle = (0 + self.size - 1) / 2
        free_slots = []
        for column_num in range(self.size):
            for row_num in range(self.num_entries[column_num], self.size):
                if self.items[column_num][row_num] == 0:
                    free_slots.append((column_num, abs((column_num - middle)) + abs((row_num - middle))))

        free_slots = sorted(free_slots, key=lambda x: x[1], reverse=False)
        slot = free_slots[0][0]

        self.items[slot][self.num_entries[slot]] = player

        max_score = 0
        for column in range(self.size):
            for row in range(self.size):
                max_score += self.num_new_points(column, row, player)

        self.items[slot][self.num_entries[slot]] = 0

        return slot, max_score - current_score,

board = GameBoard(6)
board.add(2,1)
board.add(3,2)
board.add(3,1)
board.add(2,2)
board.add(4,1)
board.add(1,2)
board.add(2,1)
board.add(3,2)
board.add(0,1)
board.add(4,2)
board.add(3,1)
board.add(4,2)
board.add(5,1)
board.add(4,2)
board.add(4,1)
board.add(2,2)
board.add(1,1)
board.add(1,2)
board.add(1,1)
board.add(1,2)
board.add(1,1)
board.add(0,2)
board.add(0,1)
board.add(0,2)
board.add(0,1)
board.add(0,2)
print("Newly created 4-in-a-row sequences: ",board.num_new_points(0,5,2))
board.display()


# class FourInARow:
#     def __init__(self, size):
#         self.board=GameBoard(size)
#     def play(self):
#         print("*****************NEW GAME*****************")
#         self.board.display()
#         player_number=0
#         print()
#         while not self.board.game_over():
#             print("Player ",player_number+1,": ")
#             if player_number==0:
#                 valid_input = False
#                 while not valid_input:
#                     try:
#                         column = int(input("Please input slot: "))       
#                     except ValueError:
#                         print("Input must be an integer in the range 0 to ", self.board.size)
#                     else:
#                         if column<0 or column>=self.board.size:
#                             print("Input must be an integer in the range 0 to ", self.board.size)
#                         else:
#                             if self.board.add(column, player_number+1):
#                                 valid_input = True
#                             else:
#                                 print("Column ", column, "is alrady full. Please choose another one.")
#             else:
#                 (best_column, max_points)=self.board.column_resulting_in_max_points(2)
#                 if max_points>0:
#                     column=best_column
#                 else:
#                     (best_column, max_points)=self.board.column_resulting_in_max_points(1)
#                     if max_points>0:
#                         column=best_column
#                     else:
#                         column = self.board.free_slots_as_close_to_middle_as_possible()[0]
#                 self.board.add(column, player_number+1)
#                 print("The AI chooses column ", column)
#             self.board.display()   
#             player_number=(player_number+1)%2
#         if (self.board.points[0]>self.board.points[1]):
#             print("Player 1 (circles) wins!")
#         elif (self.board.points[0]<self.board.points[1]):    
#             print("Player 2 (crosses) wins!")
#         else:  
#             print("It's a draw!")
            
# game = FourInARow(10)
# game.play()        