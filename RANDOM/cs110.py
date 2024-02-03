# x = int(input("x"))
# y = int(input("y"))

# answer = x
# while y != 0:
#     y -= 1
#     if y == 0:
#         print(answer)
#     answer += x

# first = int(input("first "))
# second = int(input("second "))

# while second < 20:
#     temp = first
#     first = second
#     second = temp + first
#     print(second, end = '')
#     print(" ", end = '')

stop = 5
factor = 3
value = 1
count = 1
sum = 0
while count <= stop:
    sum = sum + value
    value = value * factor
    count += 1

print(sum)