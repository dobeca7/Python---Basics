price_per_one_page = float(input())
price_per_one_korica = float(input())
percent_descent = int(input())
designer_price = float(input())
percent_from_all_sum = int(input())

starting_sum = (price_per_one_page * 899) + (price_per_one_korica * 2)
costs_after_descent = starting_sum - (percent_descent * starting_sum / 100)
costs_after_designer_price = costs_after_descent + designer_price
final_price = costs_after_designer_price - (percent_from_all_sum * costs_after_designer_price / 100)

print(f"Avtonom should pay {final_price:.2f} BGN.")

