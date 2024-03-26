g = input().split(" ")

while True:
    c = input().split(" ")
    if c[0] == "No" and c[1] == "Money":
        break
    elif c[0] == "OutOfStock":
        if c[1] in g:
            g = list(map(lambda lst: lst.replace(c[1], "None"), g))
    elif c[0] == "Required":
        index = int(c[2])
        if 0 < index < len(g):
            g[index] = c[1]
    elif c[0] == "JustInCase":
        g[-1] = c[1]

while "None" in g:
    g.remove("None")

for i in g:
    print(i, end =" ")
