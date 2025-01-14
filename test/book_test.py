from model.entity.book import Book
from model.repository.book_repository import BookRepository

#Entity test
book1=Book("Harry Potter","J. K. Rowling",233)
print(book1)


book_repo = BookRepository()
book_repo.save(book1)