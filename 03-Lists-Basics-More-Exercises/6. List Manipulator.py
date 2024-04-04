ls = input().split()
l = []
fee = []
foe = []
counter = 0

for i in ls:
    lint = int(i)
    l.append(lint)

while True:
    counter += 1

    if counter > 50:
        False

    c = input().split()

    if c[0] == "exchange":
        index = int(c[1])
        if 0 < index < len(l):
            l = l[index + 1:] + l[:index + 1]
            print(l)
        else:
            print("Invalid index")

    elif c[0] == "max":
        if c[1] == "odd":
            maxo = [num for num in l if num % 2 != 0]
            if not maxo:
                print("No matches")
            maxo = max(maxo)
            nli = len(l) - 1 - l[::-1].index(maxo)
            print(nli)

        if c[1] == "even":
            maxe = [num for num in l if num % 2 == 0]
            if not maxe:
                print("No matches")
            maxe = max(maxe)
            nli = len(l) - 1 - l[::-1].index(maxe)
            print(nli)

    elif c[0] == "min":
        if c[1] == "odd":
            mino = [num for num in l if num % 2 != 0]
            if not mino:
                print("No matches")
                continue
            mino = min(mino)
            nli = len(l) - 1 - l[::-1].index(mino)
            print(nli)

        if c[1] == "even":
            mine = [num for num in l if num % 2 == 0]
            if not mine:
                print("No matches")
                continue
            mine = min(mine)
            nli = len(l) - 1 - l[::-1].index(mine)
            print(nli)

    elif c[0] == "first":
        cf = int(c[1])
        if cf > len(l):
            print("Invalid count")

        if c[2] == "even":
            e = [num for num in l if num % 2 == 0]
            if len(e) < cf:
                cf = len(e)
            fn = e[:cf]
            print(fn)

        if c[2] == "odd":
            o = [num for num in l if num % 2 != 0]
            if len(o) < cf:
                cf = len(e)
            fn = o[:cf]
            print(fn)

    elif c[0] == "last":
        cf = int(c[1])
        if c[2] == "even":
            e = [num for num in l if num % 2 == 0]
            if len(e) < cf:
                cf = len(e)
            fn = e[-cf:]
            print(fn)

        if c[2] == "odd":
            o = [num for num in l if num % 2 != 0]
            if len(o) < cf:
                cf = len(o)
            fn = o[-cf:]
            print(fn)

    elif c[0] == "end":
        False
        break

print(l)