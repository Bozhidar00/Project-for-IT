n = int(input())
w = input()
l = []

for i in range(n):
    s = input()
    l.append(s)
print(l)

for i in range(len(l) -1,-1,-1):
    e = l[i]
    if w not in e:
        l.remove(e)
print(l)