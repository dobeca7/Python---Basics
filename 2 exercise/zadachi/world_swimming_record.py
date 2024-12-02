from math import floor

world_record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())
personal_time = distance_in_meters * time_in_seconds_for_one_meter
slowing_time = floor(distance_in_meters / 15) * 12.5
total_time = personal_time + slowing_time
diff = abs(world_record_in_seconds - total_time)



if total_time >= world_record_in_seconds:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

