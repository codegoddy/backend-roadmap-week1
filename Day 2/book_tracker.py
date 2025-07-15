class Book:
    def __init__(self, title, author, pages, rating):
        self.title = title
        self.author = author
        self.pages = pages
        self.rating = rating

    def display(self):
        print(f"📖 {self.title} by {self.author} — {self.pages} pages, rated {self.rating}⭐")


class BookTracker:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, pages, rating):
        book = Book(title, author, pages, rating)
        self.books.append(book)

    def view_books(self):
        if not self.books:
            print("No books yet")
            return

        for i, book in enumerate(self.books, start=1):
            print(f"{i}. ", end="")
            book.display()

    def summary(self):
        total_books = len(self.books)
        total_pages = 0
        total_rating = 0

        for book in self.books:
            total_pages += book.pages
            total_rating += book.rating

        if total_books == 0:
            print("No books logged yet.")
            return

        avg_rating = total_rating / total_books

        print(f"\n📚 Summary:")
        print(f"- Total books: {total_books}")
        print(f"- Total pages read: {total_pages}")
        print(f"- Average rating: {avg_rating:.1f}⭐")


tracker = BookTracker()

while True:
    print("\nWelcome to your book tracker")
    print("[1] Add Book")
    print("[2] View Books")
    print("[3] Summary")
    print("[4] Exit")

    choice = input("Please choose an option: ")

    if choice == "1":
        book_title = input("Title: ")
        author_name = input("Author: ")
        try:
            pages = int(input("Pages: "))
            rating = int(input("Rating(1-5): "))

            if rating < 0:
                print("Enter a valid rating")
                continue
            elif rating > 5:
                print("Enter a valid rating")
                continue

            tracker.add_book(book_title, author_name, pages, rating)
            print("Book added successfully!")
        except ValueError:
            print("Enter a valid number")

    elif choice == "2":
        tracker.view_books()
    elif choice == "3":
        try:
            tracker.summary()
        except ValueError:
            print("⚠️ Please enter a valid number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("\nPlease enter a valid options!")
