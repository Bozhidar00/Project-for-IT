t = input()
b = input()
h = input()

l = [t,b,h]

l[0], l[2] = l[2],l[0]

print(l)