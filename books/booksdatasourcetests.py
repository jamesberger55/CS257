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
         
    def test_unique_book(self):
        books = self.data_source.books('Beloved')
        self.assertTrue(len(books) == 1)
        self.assertTrue(books[0] == Book('Beloved'))
         
         
    

if __name__ == '__main__':
    unittest.main()
