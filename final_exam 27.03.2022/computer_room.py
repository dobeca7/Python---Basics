month = input()
hours = int(input())
people_in_group = int(input())
time_of_the_day = input()
tax = 0

if month == "march" or month == "may" or month == "april":
    if time_of_the_day == "day":
        tax = 10.50
        if people_in_group >= 4:
            tax -= 0.1 * tax
        if hours >= 5:
            tax -= 0.5 * tax
    elif time_of_the_day == "night":
        tax = 8.40
        if people_in_group >= 4:
            tax -= 0.1 * tax
        if hours >= 5:
            tax -= 0.5 * tax

elif month == "june" or month == "august" or month == "july":
    if time_of_the_day == "day":
        tax = 12.60
        if people_in_group >= 4:
            tax -= 0.1 * tax
        if hours >= 5:
            tax -= 0.5 * tax
    elif time_of_the_day == "night":
        tax = 10.20
        if people_in_group >= 4:
            tax -= 0.1 * tax
        if hours >= 5:
            tax -= 0.5 * tax



total_price = tax * hours * people_in_group

print(f"Price per person for one hour: {tax:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")


