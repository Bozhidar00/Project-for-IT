n = input().split()
s1 = 0
s2 = 0


half = len(n) // 2
lh = n[:half]
rh = n[half:]
for j in lh:
    if j == "0":
        s1 *= 0.8
    else:
        s1 += int(j)
for h in rh:
    if h == "0":
        s2 *= 0.8
    else:
        s2 += int(h)

if s2 > s1:
    print(f"The winner is left with total time {s1:.1f}.")
else:
    print(f"The winner is right with total time {s2:.1f}.")