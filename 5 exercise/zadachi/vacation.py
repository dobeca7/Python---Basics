needed_money = float(input())
available_money = float(input())
spend_counter = 0
days_counter = 0
condition = False

while available_money < needed_money:
    type_of_command = input()
    current_sum = float(input())
    days_counter += 1

    if type_of_command == "spend":
        spend_counter += 1
        if spend_counter == 5:
            print(f"You can't save the money.")
            print(f"{days_counter}")
            condition = True
            break
        if current_sum > available_money:
            available_money = 0
        else:
            available_money -= current_sum
    elif type_of_command == "save":
        spend_counter = 0
        available_money += current_sum

if not condition:
    print(f"You saved the money for {days_counter} days.")
