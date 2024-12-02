standard_tickets = 0
student_tickets = 0
kid_tickets = 0
total_tickets = 0
tickets_per_movie = 0
condition = False

while True:
    name_of_movie = input()

    if name_of_movie == "Finish":
        standard_percent = (standard_tickets / total_tickets) * 100
        student_percent = (student_tickets / total_tickets) * 100
        kid_percent = (kid_tickets / total_tickets) * 100

        print(f"Total tickets: {total_tickets}")

        print(f"{student_percent}% student tickets.")
        print(f"{standard_percent}% standard tickets.")
        print(f"{kid_percent}% kids tickets.")

        break
    available_seats = int(input())

    while True:
        type_of_tickets = input()

        if type_of_tickets == "End":
            total_tickets += tickets_per_movie
            movie_percent = total_tickets / available_seats * 100
            tickets_per_movie = 0
            break

        if type_of_tickets == "standard":
            standard_tickets += 1
        elif type_of_tickets == "student":
            student_tickets += 1
        elif type_of_tickets == "kid":
            kid_tickets += 1
        tickets_per_movie += 1
        







