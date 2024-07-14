class Book:
    def __init__(self, title ,author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def is_available(self):
        return self._is_checked_out
    
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book.Book):
            self._books.append(book)
        else:
            print("Only Book instances can be added to the library.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"The book '{title}' has been checked out.")
                else:
                    print(f"The book '{title}' is already checked out.")
                return
            print(f"The book'{title}' is not available in the library.")
    
    def return_book(self,title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"The book '{title}' has been returned.")
                else:
                    print(f"The book '{title}' was not checked out.")
                return
            print(f"The book '{title}' is not availabe in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"Title: {book.title}, Author: {book.author}")
        else:
            print("No books are currently available.")
