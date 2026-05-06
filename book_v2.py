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
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {status}"
    
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

    def update_book_info(self, new_title=None, new_author=None, new_year=None):
        if new_title:
            self.title = new_title
        if new_author:
            self.author = new_author
        if new_year:
            self.year = new_year
        print(f'Book information updated for "{self.title}".')
    
    def book_summary(self):
        return f'"{self.title} by {self.author}, published in {self.year}.'
    
class Library:
    def __init__(self):
        self.collection = []

    def add_book(self,book):
        self.collection.append(book)
        print(f'Book "{book.title}" added to the library.')

    def display_books(self):
        if not self.collection:
            print("No books in the library.")
        else:
            for book in self.collection:
                print(book.display_info())
        
book1 = Book("Babel", "R.F. Kuang", 2005)
book2 = Book("1984","George Orwell", 1949)
book3 = Book("IT", "Stephen King", 1925)
# print(book1.display_info())
# print(book2.display_info())

# book1.check_out()
# print(book1.display_info())
# book1.check_out()

# book1.return_book()
# print(book1.display_info())

# print(book3.book_summary())
# book3.update_book_info(new_title="Dark Tower", new_year=1982)
# print(book3.display_info())

my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

my_library.display_books()
