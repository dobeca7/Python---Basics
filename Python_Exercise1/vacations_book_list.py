number_pages = int(input())
pages_hour = int(input())
number_days = int(input())

total_hours = number_pages // pages_hour
hours_per_day = total_hours / number_days
print(hours_per_day)