from math import floor, ceil

days_no_santa = int(input())
amount_of_food = int(input())
food_for_deer_1 = float(input())
food_for_deer_2 = float(input())
food_for_deer_3 = float(input())

needed_food_deer_1 = food_for_deer_1 * days_no_santa
needed_food_deer_2 = food_for_deer_2 * days_no_santa
needed_food_dear_3 = food_for_deer_3 * days_no_santa

sum_food = needed_food_deer_1 + needed_food_deer_2 + needed_food_dear_3

diff = abs(amount_of_food - sum_food)

if sum_food < amount_of_food:
    diff = floor(diff)
    print(f"{diff} kilos of food left.")
else:
    diff = ceil(diff)
    print(f"{diff} more kilos of food are needed.")


