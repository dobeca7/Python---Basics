n = int(input())
left_sum = 0
right_sum = 0

for i in range(2 * n):
    current_number = int(input())

    if i < n:
        left_sum += current_number
    else:
        right_sum += current_number

diff = abs(left_sum-right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")
