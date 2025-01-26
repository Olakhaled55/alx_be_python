class Book:
    def __init__(self, title, author):
        """Initialize Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file_size."""
        super().__init__(title, author)  # Call the base class (Book) constructor
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and page_count."""
        super().__init__(title, author)  # Call the base class (Book) constructor
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize Library with an empty book collection."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        if isinstance(book, Book):  # Ensure that the book is an instance of Book or its subclasses
            self.books.append(book)
        else:
            print("Invalid book type")

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)
