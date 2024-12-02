number_of_tournament = int(input())
starting_points = int(input())

points = 0
number_of_winning = 0

for _ in range (number_of_tournament):
    stage_of_tournament = input()

    if stage_of_tournament == "SF":
        points += 720
    elif stage_of_tournament == "F":
        points += 1200
    elif stage_of_tournament == "W":
        points += 2000
        number_of_winning += 1

average_points = points / number_of_tournament
total_sum_of_points = starting_points + points

print(f"Final points: {total_sum_of_points}")
print(f"Average points: {int(average_points)}")
print(f"{number_of_winning / number_of_tournament * 100:.2f}%")
