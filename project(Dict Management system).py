class book:
    def __init__(self,title,author):
         self.title = title
         self.author = author
         self.is_available = True

    def __str__(self):
         return f"{self.title} by {self.author}"
    def borrow(self):
         if self.is_available:
              self.is_available = False
              return True
         return False
    
    def return_book(self):
         self.is_available = True


class Library:
    def _init_(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def view_available_books(self):
        print("\nAvailable Books in the Library:")
        for book in self.books:
            if book.is_available:
                print(book)
    
    def borrow_book(self, member, book_title):
        for book in self.books:
            if book.title == book_title and book.is_available:
                if member.borrow(book):
                    print(f"{member.name} borrowed '{book_title}'.")
                return
        print(f"Sorry, the book '{book_title}' is not available.")
    
    def return_book(self, member, book_title):
        for book in self.books:
            if book.title == book_title and not book.is_available:
                member.return_book(book)
                print(f"{member.name} returned '{book_title}'.")
                return
        print(f"Sorry, the book '{book_title}' was not borrowed.")

class Member:
    def _init_(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)

class Librarian(Member):
    def _init_(self, name):
        super()._init_(name)

    def add_book(self, library, book):
        library.add_book(book)




if __name__ == "__main__":
    # Create a library
    my_library = Library()
    
    # Create books
    book1 = book("Python Basics", "John Doe")
    book2 = book("Advanced Python", "Jane Smith")
    
    # Add books to the library
    librarian = Librarian()
    librarian.add_book(my_library, book1)
    librarian.add_book(my_library, book2)
    
    # View available books
    my_library.view_available_books()
    
    # Create a member
    member1 = Member("Alice")
    
    # Borrow a book
    my_library.borrow_book(member1, "Python Basics")
    
    # View available books after borrowing
    my_library.view_available_books()
    
    # Return the book
    my_library.return_book(member1, "Python Basics")
    
    # View available books after returning
    my_library.view_available_books()

    