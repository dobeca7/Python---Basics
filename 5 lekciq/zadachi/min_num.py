import sys

min_number = sys.maxsize
while True:
    number = input()

    if number == "Stop":
        break

    if int(number) < int(min_number):
        min_number = number


print(min_number)