type_of_fruit = input()
day_of_the_week = input()
quantity = float(input())



if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" \
        or day_of_the_week == "Wednesday" or day_of_the_week == "Thursday" or day_of_the_week == "Friday":
    if type_of_fruit == "banana":
        print(f"{quantity * 2.50:.2f}")
    elif type_of_fruit == "apple":
        print(f"{quantity * 1.20:.2f}")
    elif type_of_fruit == "orange":
        print(f"{quantity * 0.85:.2f}")
    elif type_of_fruit == "grapefruit":
        print(f"{quantity * 1.45:.2f}")
    elif type_of_fruit == "kiwi":
        print(f"{quantity * 2.70:.2f}")
    elif type_of_fruit == "pineapple":
        print(f"{quantity * 5.50:.2f}")
    elif type_of_fruit == "grapes":
        print(f"{quantity * 3.85:.2f}")
    else:
        print("error")

elif day_of_the_week == "Saturday" or day_of_the_week ==  "Sunday":
    if type_of_fruit == "banana":
        print(f"{quantity * 2.70:.2f}")
    elif type_of_fruit == "apple":
        print(f"{quantity * 1.25:.2f}")
    elif type_of_fruit == "orange":
        print(f"{quantity * 0.90:.2f}")
    elif type_of_fruit == "grapefruit":
        print(f"{quantity * 1.60:.2f}")
    elif type_of_fruit == "kiwi":
        print(f"{quantity * 3.00:.2f}")
    elif type_of_fruit == "pineapple":
        print(f"{quantity * 5.60:.2f}")
    elif type_of_fruit == "grapes":
        print(f"{quantity * 4.20:.2f}")
    else:
        print("error")
else:
    print("error")





