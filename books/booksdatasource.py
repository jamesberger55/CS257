#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022
    Authors: Doug Pham and James Berger
    Revised by James Berger: Changed the names to be more clear as Ali and suggested, was the only person who sent revisions

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
'''

import csv
from operator import attrgetter


class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None, books=[]):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year
        self.books = books

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name

    # For sorting authors, you could add a "def __lt__(self, other)" method
    # to go along with __eq__ to enable you to use the built-in "sorted" function
    # to sort a list of Author objects.

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title

    # For sorting books, you could add a "def __lt__(self, other)" method
    # to go along with __eq__ to enable you to use the built-in "sorted" function
    # to sort a list of Book objects.

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
        #Initialize our lists and format different years into more uniform way using commas to make parsing easier
        self.author_list = []
        self.book_list = []
        with open(books_csv_file_name) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                author_info = row[2].replace("(", ",").replace(")", "").replace("-", ",").replace("and", ",")
                author_library = author_info.split(",")
          
                #Standard author with one given name, one surname, and date of living
                if (len(author_library) == 3):
                    author_name = author_library[0]
                    author_birth_year = int(author_library[1])
                    author_death_year = author_library[2]
                    #If author is still alive
                    if author_death_year == '':
                        author_death_year = None
                    else:
                        author_death_year = int(author_library[2])

               #Special case with multiple authors
                else:
                    author_name = author_library[0]
                    author_birth_year = int(author_library[1])
                    author_death_year = author_library[2]
                    author2_name = author_library[3]
                    author2_birth_year = int(author_library[4])
                    author2_death_year = author_library[5]
                    if author2_death_year == '' or author_death_year == ' ':
                        author2_death_year = None
                    else:
                        author2_death_year = int(author_library[5])
                    if author_death_year == '' or author_death_year == ' ':
                        author_death_year = None
                    else:
                        author_death_year = int(author_library[2])

                #Parses author name into first and last name
                author_names_dict = author_name.split(" ") 
                author_given_name = author_names_dict[0]
                author_surname = author_names_dict[1]
                
                #After properly parsed creates object of Author class and adds to author_list
                author = Author(surname=author_surname, given_name=author_given_name, birth_year=author_birth_year, death_year=author_death_year)
                if author not in self.author_list:
                    self.author_list.append(author)

                #Adds second author if there was one
                if (len(author_library) > 3):
                    author2_names_dictionary = author_name.split(" ") 
                    author2_given_name = author_names_dict[0]
                    author2_surname = author_names_dict[1]
                      
                    author2 = Author(surname=author2_surname, given_name=author2_given_name, birth_year=author2_birth_year, death_year=author2_death_year)
                    if author2 not in self.author_list:
                        self.author_list.append(author2)

                #Creates new object of Book class with the input variables from the first two values in csv and adds to our book_list 
                new_book = Book(row[0], int(row[1]))
                self.book_list.append(new_book)

                #Sets our instance variable for list of books and authors appropriately
                new_book.authors.append(self.author_list)
                author.books.append(self.book_list)
               
 

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        
        results = []
        #If no search text is provided then displays sorted by surname
        if search_text == None:
            sort_authors = sorted(self.author_list, key=attrgetter("surname", "given_name"))
            return sort_authors
        else:
            search_text = search_text.lower()
            for author in self.author_list:
                #If specified lower and surname than sorts by surname in descending order
                if search_text in author.surname.lower():
                    results.append(author)
                #Here if specified by lower and given name into descending order
                elif search_text in author.given_name.lower():
                    results.append(author)
            sort_authors = sorted(results, key=attrgetter("surname", "given_name"))
            return sort_authors
   
    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        results = []
        #If no search text is provided then displays sorted by title
        if search_text == None:
            return sorted(self.book_list, key=attrgetter("title", "publication_year"))
        else:
            search_text = search_text.lower()
            for book in self.book_list:
                #If specified to go in descending order
                if search_text in book.title.lower():
                    results.append(book)
            #If specified by year
            if sort_by == 'year':
                return sorted(results, key=attrgetter("publication_year", "title"))
            else:
                return sorted(results, key=attrgetter("title", "publication_year")) 

    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        results = []
        sort_year = sorted(self.book_list, key=lambda book:book.publication_year)
        #No years specified so returns list as is
        if start_year == None and end_year == None:
            for book in sort_year:
                results.append(book)
        elif start_year == None and end_year != None:
            for book in sort_year:
                for book in sort_year:
                    #Appends books that are not after the specified end year date
                    if int(book.publication_year) <= int(end_year):
                        results.append(book)
        elif end_year == None and start_year != None:
            for book in sort_year:
                #Appends books that are not before the specified start year date
                if int(book.publication_year) >= int(start_year):
                    results.append(book)
        elif start_year != None and end_year != None:
            #Appends books within range of start year and end year
            for book in sort_year:
                if int(book.publication_year) >= int(start_year) and int(book.publication_year) <= int(end_year):
                    results.append(book)
        return results

if __name__ == "__main__":
    ds = BooksDataSource("books1.csv")
