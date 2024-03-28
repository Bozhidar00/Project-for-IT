j = int(input())
p = []
n = []

for i in range(j):
    num = int(input())
    if num >= 0:
        p.append(num)
    else:
        n.append(num)

print(p)
print(n)
print(f"Count of positives : {len(p)}. Sum of negatives : {sum(n)}. ")