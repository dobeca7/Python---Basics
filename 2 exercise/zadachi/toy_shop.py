price_for_trip = float(input())
number_of_puzzles = int(input())
number_of_talking_dolls = int(input())
number_of_bears = int(input())
number_of_minion = int(input())
number_of_trucks = int(input())
order_sum = (number_of_puzzles * 2.6) + (number_of_talking_dolls * 3) + (number_of_bears * 4.1) \
            + (number_of_minion * 8.2) + (number_of_trucks * 2)
number_of_toys = number_of_trucks + number_of_minion + number_of_bears + number_of_puzzles + number_of_talking_dolls

if number_of_toys >= 50:
    order_sum -= order_sum * 0.25
rent = order_sum * 0.1
profit = order_sum - rent
diff = abs(price_for_trip-profit)
if profit >= price_for_trip:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")