length = int(input())
width = int(input())

size_of_cake = length * width

while True:
    taking = input()
    if taking == "STOP":
        print(f"{abs(size_of_cake)} pieces are left.")
        break
    size_of_cake -= int(taking)
    if size_of_cake <= 0:
        print(f"No more cake left! You need {abs(size_of_cake)} pieces more.")
        break



