number_of_groups = int(input())

group_Musala = 0
group_Monblan = 0
group_Kilimandjaro = 0
group_K2 = 0
group_Everest = 0
all_people = 0

for i in range(number_of_groups):
    number_of_people_in_group = int(input())

    if number_of_people_in_group <= 5:
        group_Musala += number_of_people_in_group
    if 6 <= number_of_people_in_group <= 12:
        group_Monblan += number_of_people_in_group
    if 13 <= number_of_people_in_group <= 25:
        group_Kilimandjaro += number_of_people_in_group
    if 26 <= number_of_people_in_group <= 40:
        group_K2 += number_of_people_in_group
    if number_of_people_in_group > 40:
        group_Everest += number_of_people_in_group
    all_people += number_of_people_in_group

print(f"{group_Musala / all_people * 100:.2f}%")
print(f"{group_Monblan / all_people * 100:.2f}%")
print(f"{group_Kilimandjaro / all_people * 100:.2f}%")
print(f"{group_K2 / all_people * 100:.2f}%")
print(f"{group_Everest / all_people * 100:.2f}%")




