locations = int(input())

for loc in range(locations):
    expected_average_gold_digging = float(input())
    number_of_days_digging = int(input())
    all_days_gold = 0
    for n in range(number_of_days_digging):
        gold_per_day = float(input())

        all_days_gold += gold_per_day

    if all_days_gold / number_of_days_digging >= expected_average_gold_digging:
        print(f"Good job! Average gold per day: {all_days_gold/ number_of_days_digging:.2f}.")
    elif all_days_gold / number_of_days_digging < expected_average_gold_digging:
        print(f"You need {expected_average_gold_digging - (all_days_gold / number_of_days_digging):.2f} gold.")

