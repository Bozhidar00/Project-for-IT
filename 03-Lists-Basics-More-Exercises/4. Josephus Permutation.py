p = input().split()
pl = []
k = int(input())
l = []
i = 0

for j in p:
    pint = int(j)
    pl.append(pint)

while len(pl) > 0:
    i = (i + k - 1) % len(pl)
    l.append(pl.pop(i))

print(l)