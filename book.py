class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        return f'Title: {self.title}, Author: {self.author}, Pages: {self.pages}'
    
book1 = Book("1984", "George Orwell", 328)
book2 = Book("Pride and Prejudice", "Jane Austen", 450)

print(book1.display_info())
print(book2.display_info())