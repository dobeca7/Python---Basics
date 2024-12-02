budget = int(input())
type_of_the_season = input()
number_fishers = int(input())

costs = 0

if type_of_the_season == "Spring":
    costs = 3000
elif type_of_the_season == "Summer" or type_of_the_season == "Autumn":
    costs = 4200
elif type_of_the_season == "Winter":
    costs = 2600

if number_fishers <= 6:
    costs -= costs * 0.1
elif 6 < number_fishers <= 11:
    costs -= costs * 0.15
elif number_fishers > 11:
    costs -= costs * 0.25

if number_fishers % 2 == 0 and type_of_the_season != "Autumn":
    costs -= costs * 0.05

diff = abs(budget - costs)

if budget >= costs:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")


