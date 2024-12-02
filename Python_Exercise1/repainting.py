nylon = int(input())
paint = int(input())
razr = int(input())
hours = int(input())

nylon_sum = (nylon + 2) * 1.5
paint_sum = (paint + paint * 0.1) * 14.5
razr_sum = razr * 5
total_sum = nylon_sum + paint_sum + razr_sum + 0.4
sum_workers = total_sum * 0.3 * 8
final_sum = total_sum + sum_workers
print(final_sum)