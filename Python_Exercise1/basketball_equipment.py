year_tax = int(input())
shoes = year_tax - (year_tax * 0.40)
suit = shoes - (shoes* 0.20)
ball = suit / 4
acc = ball / 5
total_expences = year_tax + shoes + suit + ball + acc

print(total_expences)
