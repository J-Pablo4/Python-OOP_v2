class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.__is_checked_out = False
    
    def get_status(self):
        if self.__is_checked_out:
            return "Checked out"
        else:
            return "Available"

    def display_info(self):
        status = self.get_status()
        return f"Title: {self.title}, Author:{self.author}, Year: {self.year}, Status: {status}"
    
    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            print(f'You have successfully checked out "{self.title}".')
        else:
            print(f'Sorry, "{self.title}" is already checked out.')
        
    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            print(f'You have successfully returned "{self.title}".')
        else:
            print(f'"{self.title}" was not checked out.')
        
book1 = Book("Babel", "R.F. Kuang", 2005)
book2 = Book("1984","George Orwell", 1949)
print(book1.display_info())
print(book2.display_info())

book1.check_out()
print(book1.display_info())
book1.check_out()

book1.return_book()
print(book1.display_info())

