n = input().split(", ")

for i in n:
    if i == "0":
        n.remove(i)
        n.append(i)

print(n)