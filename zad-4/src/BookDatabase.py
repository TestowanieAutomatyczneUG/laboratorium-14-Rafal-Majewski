class BookDatabase:
	def __init__(self):
		self.books = dict()

	def addBook(self, book):
		if book.isbn in self.books:
			raise ValueError("Book with this ISBN already exists")
		self.books[book.isbn] = book

	def hasIsbn(self, isbn):
		return isbn in self.books

	def getBookByIsbn(self, isbn):
		if not self.hasIsbn(isbn):
			return None
		return self.books[isbn]