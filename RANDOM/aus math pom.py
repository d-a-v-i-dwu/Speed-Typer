import math

alist = []

n = 6
k = 4
previous_answer = 1
for i in range(1, 10):
    
    answer = math.factorial(i + n) / (math.factorial(k) * math.factorial(n + i - k))
    print(answer, "/", previous_answer)
    previous_answer = answer
    alist.append(round(answer))

print(alist)
print(sum(alist) / 35)
