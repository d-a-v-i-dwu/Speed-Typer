alist = []
blist = []
for i in range(10000000):
    if (str(i ** 2))[-(len(str(i))):] == str(i):
        alist.append(i)
        blist.append(i ** 2)
print(alist)
print(blist)
