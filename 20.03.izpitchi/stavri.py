n = int(input())
sum_quantity = 0
degrees = 0


for d in range(n):
    quantity = float(input())
    degree_per_day = float(input())

    sum_quantity += quantity
    degrees += quantity * degree_per_day

    average_degrees = degrees / sum_quantity


print(f"Liter: {sum_quantity:.2f}")
print(f"Degrees: {average_degrees:.2f}")
if average_degrees < 38:
    print(f"Not good, you should baking!")
elif 38 <= average_degrees < 42:
    print(f"Super!")
elif average_degrees > 42:
    print(f"Dilution with distilled water!")



