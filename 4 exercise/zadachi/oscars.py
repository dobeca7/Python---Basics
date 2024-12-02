name_of_actor = input()
points_by_academy = float(input())
number_of_judges = int(input())

personal_points = 0

for i in range(number_of_judges):
    name_of_judge = input()
    points_by_judge = float(input())
    points_by_academy += (len(name_of_judge) * points_by_judge / 2)
    if points_by_academy > 1250.5:
        break


diff = abs(1250.5 - points_by_academy)

if points_by_academy > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {points_by_academy:.1f}!")
else:
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")



