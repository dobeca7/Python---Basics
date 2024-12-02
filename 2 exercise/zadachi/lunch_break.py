from math import ceil

name_of_movie = input()
episode_duration = int(input())
rest_duration = int(input())

time_to_lunch = rest_duration * 1 / 8
time_to_break = rest_duration * 1 / 4
left_time = rest_duration - time_to_lunch - time_to_break

diff = ceil(abs(episode_duration-left_time))

if episode_duration <= left_time:
    print(f"You have enough time to watch {name_of_movie} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_movie}, you need {diff} more minutes.")
