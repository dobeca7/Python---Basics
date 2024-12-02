pens_count = int(input())
markers_count= int(input())
detergent_liters = int(input())
percent = int(input())

price_pens = pens_count * 5.8
price_markers = markers_count * 7.20
price_detergent = detergent_liters * 1.20

total_price = price_pens + price_markers + price_detergent
result = total_price - (total_price * (percent / 100))
print(result)