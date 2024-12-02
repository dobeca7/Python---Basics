from math import floor

number_needed_processors = int(input())
employers = int(input())
working_days = int(input())


working_time = employers * working_days * 8
worked_processors = floor(working_time / 3)

diff = abs((number_needed_processors - worked_processors) * 110.10)


if worked_processors < number_needed_processors:
    print(f"Losses: -> {diff:.2f} BGN")
elif worked_processors >= number_needed_processors:
    print(f"Profit: -> {diff:.2f} BGN")
