import sys

max_number = -sys.maxsize
while True:
    number = input()

    if number == "Stop":
        break

    if int(number) > int(max_number):
        max_number = number


print(max_number)