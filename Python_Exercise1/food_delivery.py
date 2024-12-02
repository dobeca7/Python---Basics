chicken_food = int(input())
fish_food = int(input())
vegetarian_food = int(input())
price_of_chicken_food = chicken_food * 10.35
price_of_fish_food = fish_food * 12.40
price_of_vegetarian_food = vegetarian_food * 8.15
total_food_price = price_of_fish_food + price_of_vegetarian_food + price_of_chicken_food
desert_price = 20 * total_food_price / 100
grand_total = total_food_price + desert_price + 2.50
print(grand_total)