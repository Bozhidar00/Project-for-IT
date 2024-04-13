def check_winner(field):

    for row in field:
        if row.count(1) == 3:
            return "First player won"
        elif row.count(2) == 3:
            return "Second player won"

    for col in range(3):
        if field[0][col] == field[1][col] == field[2][col] == 1:
            return "First player won"
        elif field[0][col] == field[1][col] == field[2][col] == 2:
            return "Second player won"

    if field[0][0] == field[1][1] == field[2][2] == 1 or field[0][2] == field[1][1] == field[2][0] == 1:
        return "First player won"
    elif field[0][0] == field[1][1] == field[2][2] == 2 or field[0][2] == field[1][1] == field[2][0] == 2:
        return "Second player won"

    if all(0 not in row for row in field):
        return "Draw!"

    return None

field = []
for _ in range(3):
    row = list(map(int, input().split()))
    field.append(row)

result = check_winner(field)
print(result)
