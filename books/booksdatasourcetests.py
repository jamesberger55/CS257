'''
   booksdatasourcetest.py
   Jeff Ondich, 24 September 2021
'''

from booksdatasource import Author, Book, BooksDataSource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))
        print("1")
   
    def test_all_authors(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        authors = tiny_data_source.authors()
        self.assertTrue(len(authors) == 3)
        self.assertTrue(authors[0] == Author('Austen', 'Jane'))
        self.assertTrue(authors[1] == Author('Gaiman', 'Neil'))
        self.assertTrue(authors[2] == Author('Melville', 'Herman'))
         print("2")


    def test_unique_author(self):
        author = self.data_source.authors('Campbell')
        self.assertTrue(len(author) == 0)
        print("3")

    
    def invalid_book_input(self):
        books = self.data_source.books(2000)
        self.assertTrue(len(books) == 0)
         print("4")
      
    def test_book_not_in_csv(self):
        books = self.data_source.books('Orange')
        self.assertTrue(len(books) == 0)
        print("5")
     
    def test_case_sensitive_title(self):
        books = self.data_source.books('Beloved')
        print("6")

    def test_case_sensitive_title(self):
        books = self.data_source.books('beloved')
        self.assertTrue(len(books) == 0)
         print("7")

    def test_two_books(self):
        books = self.data_source.books("Beloved, Omoo")
        self.assertTrue(len(books) == 0)
        print("8")

    def years_not_in_scope(self):
        books = self.data_source.books_between_years(1000, 1001)
        self.assertTrue(len(books) == 0)
        print("9")

    def test_one_year(self):
        books = self.data_source.books_between_years(2016, 2019)
        self.assertTrue(len(books) == 3)
        print("10")

    def invalid_year_input(self):
        books = self.data_source.books_between_years('bad', 'input')
        self.assertTrue(len(books) == 0)

if __name__ == '__main__':
   unittest.main()
