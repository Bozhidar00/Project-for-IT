max_prices = {
    'Clothes': 50.00,
    'Shoes': 35.00,
    'Accessories': 20.50
}

items_input = input().split('|')
budget = float(input())

new_prices = []
total_profit = 0

for item in items_input:
    item_type, price = item.split('->')
    price = float(price)

    if price <= max_prices[item_type] and price <= budget:

        budget -= price
        new_price = price * 1.40
        new_prices.append(new_price)

        profit = new_price - price
        total_profit += profit

# Print the new prices and total profit
print(" ".join([f"{price:.2f}" for price in new_prices]))
print(f"Profit: {total_profit:.2f}")

if profit >= 0:
    print("Hello, France!")
else:
    print("Not enough money.")