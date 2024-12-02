quantity_of_food = int(input())
grams_of_food = quantity_of_food * 1000

while True:
    grams = input()
    if grams == "Adopted":
        break
    grams_of_food -= int(grams)

if quantity_of_food * 1000 >= grams_of_food:
    print(f"Food is enough! Leftovers: {grams_of_food} grams.")
elif quantity_of_food * 1000 < grams_of_food:
    print(f"Food is not enough. You need {abs(grams_of_food)} grams more.")