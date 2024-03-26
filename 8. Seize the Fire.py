def put_out_fire(fires, water):
    total_effort = 0
    total_fire_put_out = 0
    cells_put_out = []

    # Define fire ranges
    fire_ranges = {
        'High': (81, 125),
        'Medium': (51, 80),
        'Low': (1, 50)
    }

    # Process each fire cell
    for fire_cell in fires.split('#'):
        fire_type, value = fire_cell.split(' = ')
        value = int(value)

        # Check if fire cell is valid
        if fire_ranges[fire_type][0] <= value <= fire_ranges[fire_type][1]:
            # Check if there is enough water to put out the fire
            if water >= value:
                water -= value
                effort = 0.25 * value
                total_effort += effort
                total_fire_put_out += value
                cells_put_out.append(value)
            else:
                continue

    return total_effort, total_fire_put_out, cells_put_out


# Input
fires_input = input()
water_input = int(input())

# Calculate
effort, total_fire, cells = put_out_fire(fires_input, water_input)

# Output
print("Cells:")
for cell in cells:
    print(f"- {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
