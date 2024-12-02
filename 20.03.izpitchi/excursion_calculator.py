number_people = int(input())
season = input()
costs = 0

if season == "spring":
    if number_people <= 5:
        costs = number_people * 50
    elif number_people > 5:
        costs = number_people * 48
if season == "summer":
    if number_people <= 5:
        costs = number_people * 48.5
    elif number_people > 5:
        costs = number_people * 45

if season == "autumn":
    if number_people <= 5:
        costs = number_people * 60
    elif number_people > 5:
        costs = number_people * 49.5
if season == "winter":
    if number_people <= 5:
        costs = number_people * 86
    elif number_people > 5:
        costs = number_people * 85
if season == "summer":
    costs -= costs * 0.15
elif season == "winter":
    costs += costs * 0.08

print(f"{costs:.2f} leva.")


