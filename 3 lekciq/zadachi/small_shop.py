type_of_product = input()
city = input()
quantity = float(input())
price = 0

if city == "Sofia":
    if type_of_product == "coffee":
        price = 0.50
    if type_of_product == "water":
        price = 0.80
    if type_of_product == "beer":
        price = 1.20
    if type_of_product == "sweets":
        price = 1.45
    if type_of_product == "peanuts":
        price = 1.60
elif city == "Plovdiv":
    if type_of_product == "coffee":
        price = 0.40
    if type_of_product == "water":
        price = 0.70
    if type_of_product == "beer":
        price = 1.15
    if type_of_product == "sweets":
        price = 1.30
    if type_of_product == "peanuts":
        price = 1.50
elif city == "Varna":
    if type_of_product == "coffee":
        price = 0.45
    if type_of_product == "water":
        price = 0.70
    if type_of_product == "beer":
        price = 1.10
    if type_of_product == "sweets":
        price = 1.35
    if type_of_product == "peanuts":
        price = 1.55

total_price = quantity * price
print(total_price)
