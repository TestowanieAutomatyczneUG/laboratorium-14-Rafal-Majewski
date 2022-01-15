from behave import *
from src.BookDatabase import BookDatabase
from src.Book import Book
from src.Author import Author

use_step_matcher("re")

@given("máme databázi knih")
def step_impl(context):
	context.bookDatabase = BookDatabase()