class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_taken = False

    def taken(self):
        self.is_taken = True
        print(self.title, "has been taken by a student.")

    def return_book(self):
        self.is_taken = False
        print(self.title, "has been returned by the student.")


book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Secrets of The Cacklefur Castle", "Geronimo Stilton")
book3 = Book("Wings of Fire", "A.P.J. Abdul Kalam")
book4 = Book("Grandma's Bag of Stories", "Sudha Murthy")
book5 = Book("The Secret City", "Thea Stilton")


book1.taken()
book1.return_book()

book2.taken()
book2.return_book()

book3.taken()
book3.return_book()

book4.taken()
book4.return_book()

book5.taken()
book5.return_book()