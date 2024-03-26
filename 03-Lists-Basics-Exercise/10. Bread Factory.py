events = input().split("|")

energy = 100
coins = 100

for event in events:
    event_data = event.split("-")
    action = event_data[0]
    value = int(event_data[1])

    if action == "rest":
        gained_energy = min(value, 100 - energy)
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif action == "order":
        energy -= 30
        if energy >= 0:
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= value:
            coins -= value
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}.")
            break

if energy >= 0:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
