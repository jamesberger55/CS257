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
      
    def test_initialisation(self):
        books = self.data_source.book_list
        authors = self.data_source.author_list

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))
       
   
    def test_all_authors(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        authors = tiny_data_source.authors()
        self.assertTrue(len(authors) == 3)
        self.assertTrue(authors[0] == Author('Austen', 'Jane'))
        self.assertTrue(authors[1] == Author('Gaiman', 'Neil'))
        self.assertTrue(authors[2] == Author('Melville', 'Herman'))
    

    def test_unique_author(self):
        author = self.data_source.authors('Campbell')
        self.assertTrue(len(author) == 0)
         
    def test_two_authors(self):
        author = self.data_source.authors('Campbell', 'bob')
        self.assertTrue(len(author) == 0)
  

    
    def invalid_book_input(self):
        books = self.data_source.books(2000)
        self.assertTrue(len(books) == 0)
     
      
    def test_book_not_in_csv(self):
        books = self.data_source.books('Orange')
        self.assertTrue(len(books) == 0)

     
    def test_case_sensitive_title(self):
        books = self.data_source.books('Beloved')
  

    def test_case_sensitive_title(self):
        books = self.data_source.books('beloved')
        self.assertTrue(len(books) == 1)
        print("hello")
   
   
    def test_two_books(self):
         books = self.data_source.books("Beloved, Orange")
         self.assertTrue(len(books) == 0)
         
       

    def years_not_in_scope(self):
        books = self.data_source.books_between_years(1000, 1001)
        self.assertTrue(len(books) == 0)
 


    def invalid_year_input(self):
        books = self.data_source.books_between_years('bad', 'input')
        self.assertTrue(len(books) == 0)
    

if __name__ == '__main__':
   unittest.main()
