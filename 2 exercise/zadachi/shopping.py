budget = float(input())
video = int(input())
processors = int(input())
ram = int(input())

video_sum = video * 250
processors_price = 0.35 * video_sum
processors_sum = processors * processors_price
ram_price = 0.10 * video_sum
ram_sum = ram * ram_price

grand_sum = video_sum + processors_sum + ram_sum

if video > processors:
    grand_sum -= 0.15 * grand_sum

diff = abs(budget - grand_sum)

if grand_sum <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")

