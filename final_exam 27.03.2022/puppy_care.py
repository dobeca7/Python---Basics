quantity_of_food = int(input())
grams_of_food = quantity_of_food * 1000
my_grams = 0

while True:
    grams = input()
    if grams == "Adopted":
        break
    my_grams += int(grams)

diff = abs(grams_of_food - my_grams)

if grams_of_food >= my_grams:
    print(f"Food is enough! Leftovers: {diff} grams.")
elif grams_of_food < my_grams:
    print(f"Food is not enough. You need {diff} grams more.")



