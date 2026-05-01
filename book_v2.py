class Book:
    def __init__(self, title, author, year, status="Available"):
        self.title = title
        self.author = author
        self.year = year
        self.__status = status

    def book_info(self):
        return f"Title: {self.title}, Author:{self.author}, Year: {self.year}, Status: {self.__status}"
    
    def rent_book(self):
        if self.__status == "Available":
            self.__status = "Rented"
        else:
            return f"{self.title} is currently unavailable"
        
    def return_book(self):
        if self.__status == "Rented":
            self.__status = "Available"
        else:
            return f"The book has already been returned"
        
book1 = Book("Babel", "R.F. Kuang", "2005")
print(book1.book_info())
book1.rent_book()

print(book1.book_info())
book1.return_book()
print(book1.book_info())
