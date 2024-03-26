a = input()
l = [int(i) for i in a.split(" ")]
n = int(input())

for i in range(n):
    m = min(l)
    l.remove(m)

r = ', '.join(map(str, l))
print(r)
