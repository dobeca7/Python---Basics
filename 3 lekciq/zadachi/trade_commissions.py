city = input()
volume_of_sales = float(input())
bonus = 0
condition = True

if city == "Sofia":
    if 0 <= volume_of_sales  <= 500:
        bonus = volume_of_sales * 0.05
    elif 500 <= volume_of_sales  <= 1000:
        bonus = volume_of_sales * 0.07
    elif 1000 <= volume_of_sales  <= 10000:
        bonus = volume_of_sales * 0.08
    elif volume_of_sales > 10000:
        bonus = volume_of_sales * 0.12
    else:
        print("error")
        condition = False
elif city == "Varna":
    if 0 <= volume_of_sales  <= 500:
        bonus = volume_of_sales * 0.045
    elif 500 <= volume_of_sales  <= 1000:
        bonus = volume_of_sales * 0.075
    elif 1000 <= volume_of_sales  <= 10000:
        bonus = volume_of_sales * 0.1
    elif volume_of_sales > 10000:
        bonus = volume_of_sales * 0.13
    else:
        print("error")
        condition = False
elif city == "Plovdiv":
    if 0 <= volume_of_sales <= 500:
        bonus = volume_of_sales * 0.055
    elif 500 <= volume_of_sales <= 1000:
        bonus = volume_of_sales * 0.08
    elif 1000 <= volume_of_sales <= 10000:
        bonus = volume_of_sales * 0.12
    elif volume_of_sales > 10000:
        bonus = volume_of_sales * 0.145
    else:
        print("error")
        condition = False

else:
    print("error")
    condition = False

if condition:

    print(f"{bonus:.2f}")