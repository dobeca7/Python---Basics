name_of_the_searching_book = input()
book_counter = 0

while True:
    current_book_name = input()

    if current_book_name == name_of_the_searching_book:
        print(f"You checked {book_counter} books and found it.")
        break

    elif current_book_name == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_counter} books.")
        break

    book_counter += 1
