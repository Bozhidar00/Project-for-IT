o = input()
b = int(input())

ol = o.split(", ")
of = []

for i in ol:
    of.append(int(i))

bs = [0] * b

for j in range(len(of)):
        bi = j % b
        bs[bi] += of[j]

print(bs)