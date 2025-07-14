name = input("What's your name? ")
print(f"\n Welcome, {name}\n")

try:
    book_log = int(input("How many books do you want to log? "))
except ValueError:
    print("Please enter a valid number")
    exit()


books = []

for i in range(book_log):
    print(f"\nBook {i + 1}:")
    book_title = input("Title: ")
    author_name = input("Author: ")
    try:
        page_to_read = int(input("Pages: "))
    except ValueError:
        print("Enter a valid number")
        continue
    try:
        rating = int(input("Rating(1-5): "))
        if rating < 1 or rating > 5:
            print("Please enter a valid rating between 1-5")
            continue
    except ValueError:
        print("Please enter a valid number")
        continue


    books.append((book_title, author_name, page_to_read, rating))

print(f"\nReading Summary for {name}:\n")

total_pages = 0
total_rating = 0

for book_title, author_name, page_to_read, rating  in books:
    print(f"{book_title} by {author_name} - {page_to_read}pages, rated{rating}⭐")
    total_pages += page_to_read
    total_rating += rating

num_books = len(books)
if num_books > 0:
    avg_rating = total_rating / num_books
    print(f"\n Total pages read: {total_pages}")
    print(f"⭐ Average rating: {avg_rating:.1f}")






