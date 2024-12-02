number_people = int(input())
number_nights = int(input())
transport_cards = int(input())
museum_tickets = int(input())

night_per_person = number_nights * 20
transport_cards_per_person = transport_cards * 1.6
museum_tickets_per_person = museum_tickets * 6
sum_per_person = night_per_person + transport_cards_per_person + museum_tickets_per_person
sum_per_group = sum_per_person * number_people
grand_sum = sum_per_group + (0.25 * sum_per_group)
print(f"{grand_sum:.2f}")