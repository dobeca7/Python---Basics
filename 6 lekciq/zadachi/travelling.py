while True:
    destination = input()
    if destination == "End":
        break
    minimum_budget = float(input())

    while True:
        savings = float(input())
        minimum_budget -= savings

        if minimum_budget <= 0:
            print(f"Going to {destination}!")
            condition = True
            break




