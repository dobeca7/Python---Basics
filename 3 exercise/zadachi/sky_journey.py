days = int(input())
type_of_property = input()
rating = input()

costs = 0
number_of_nights = days - 1

if type_of_property == "room for one person":
    costs = 18 * number_of_nights
elif type_of_property == "apartment":
    costs = 25 * number_of_nights
    if number_of_nights < 10:
        costs -= costs * 0.30
    elif 10 <= number_of_nights <= 15:
        costs -= costs * 0.35
    elif number_of_nights > 15:
        costs -= costs * 0.5
elif type_of_property == "president apartment":
    costs = 35 * number_of_nights
    if number_of_nights < 10:
        costs -= costs * 0.10
    elif 10 <= number_of_nights <= 15:
        costs -= costs * 0.15
    elif number_of_nights > 15:
        costs -= costs * 0.2

if rating == "positive":
    costs += costs * 0.25
elif rating == "negative":
    costs -= costs * 0.10

print(f"{costs:.2f}")




