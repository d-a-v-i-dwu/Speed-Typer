stones = input("Input a number:")

def checking_input(input):
    try:
        int(stones)
        return stones
    except ValueError:
        try:
            float(stones)
            print("A whole number please")
            exit()
        except ValueError:
            str(stones)
            print("A number please")
            exit()
            return
stones = checking_input(input)

stone_piles = int(stones)
piles = 0
n = 0

while piles < stone_piles:
    new_stones = int(stones) + n
    print(new_stones, end = " ")
    piles += 1
    n += 2
