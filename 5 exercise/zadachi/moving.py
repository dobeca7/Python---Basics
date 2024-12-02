width = int(input())
length = int(input())
height = int(input())

available_free_space = width * length * height
occupied_space = 0

while True:
    number = input()

    if number == "Done":
        break

    occupied_space += int(number)

    if occupied_space > available_free_space:
        break

diff = abs(occupied_space-available_free_space)

if available_free_space >= occupied_space:
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")

