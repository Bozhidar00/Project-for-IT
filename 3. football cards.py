a = ["A-1","A-2","A-3","A-4","A-5","A-6","A-7","A-8","A-9","A-10","A-11"]
b = ["B-1","B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
n = input().split(" ")

for i in n:
    if i in a:
        a.remove(i)

    elif i in b:
        b.remove(i)

print(a)
print(b)