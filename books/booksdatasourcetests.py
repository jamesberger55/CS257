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
    
    def test_all_authors(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        authors = self.tiny_data_source.authors()
        self.assertTrue(len(authors) == 3)
        self.assertTrue(authors[0] == Author('Austen', 'Jane'))
        self.assertTrue(authors[1] == Author('Gaiman', 'Neil'))
        self.assertTrue(authors[2] == Author('Melville', 'Herman'))

    def test_unique_book(self):
        books = self.data_source.books('Beloved')
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0] == Book('Beloved'))
         
    def test_all_books(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books()
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0].title == 'Omoo')
        self.assertTrue(books[1].title == 'Emma')
        self.assertTrue(books[2].title == 'Neverwhere')
    
    def test_book_not_in_csv(self):
        books = self.data_source.books('Orange')
        self.assertTrue(len(books) == 0)

    def test_case_sensitive_title(self):
        books = self.data_source.books('beloved')
        self.assertTrue(len(books) == 0)

    def test_two_books(self):
        books = self.data_source.books("Beloved, Omoo")
        self.assertTrue(len(books) == 0)

    def year_not_in_scope(self):
        books = self.data_source.books.year(1000)
        self.assertTrue(len(books) == 0)

if __name__ == '__main__':
   unittest.main()
