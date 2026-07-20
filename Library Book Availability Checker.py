books = ["Python Basics", "Data Science", "Machine Learning", "AI Essentials", "Web Development"]
copy_counts = [5, 0, 3, 2, 1]

library = {book: count for book, count in zip(books, copy_counts)}
print("Library Inventory:", library)


available_books = [book for book in books if library[book] > 0]
print("Available Books:", available_books)

chosen_book = input("Which book do you want to borrow? ")


if chosen_book not in library or library[chosen_book] == 0:
    print(chosen_book, "is unavailable! Stopping the checker.")
    exit()


late_fees = [10, 15, 20, 25, 30]
increase = int(input("Enter the late fee increase amount: "))


updated_fees = list(map(lambda fee: fee + increase, late_fees))
print("Updated Late Fees:", updated_fees)


book_index = books.index(chosen_book)
chosen_fee = updated_fees[book_index]
print("Late fee for", chosen_book, "after update:", chosen_fee)


library[chosen_book] = library[chosen_book] - 1
print(chosen_book, "borrowed! Remaining copies:", library[chosen_book])

print("")
print("======= LIBRARY BOOK AVAILABILITY CHECKER =======")
print("Book Borrowed:", chosen_book)
print("Updated Late Fee:", chosen_fee)
print("Updated Library Inventory:", library)
print("================================================")