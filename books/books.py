import booksdatasource
import sys

def print_book(books):
    for book in books:
        #if (len(book.authors) > 1):
        #     print(book.title, book.publication_year, book.authors[0].given_name, 
        #     book.authors[0].surname, book.authors[1].given_name, book.authors[1].surname)
        # else:
            print(book.title, book.publication_year)

def print_author(authors):
    for author in authors:
        print(author.given_name, author.surname)

def main():
    data_source = booksdatasource.BooksDataSource('books1.csv')

    if (len(sys.argv) < 2):
        print("More arguments required, please type 'python3 books.py help' to see command line interface")
    elif sys.argv[1] == "title":
        if len(sys.argv) == 4:
            if sys.argv[3] == "title" or sys.argv[3] == "year":
                books = data_source.books(sys.argv[2], sys.argv[3])
                print_book(books)
            else:
                print("Sorting command invalid, please type 'python3 books.py help' to see command line interface")
        elif len(sys.argv) == 3:
            books = data_source.books(sys.argv[2])
            print_book(books)
        elif len(sys.argv) == 2:
            books = data_source.books()
            print_book(books)
        else:
            print("Too many arguments provided, please type 'python3 books.py help' to see command line interface")
    elif sys.argv[1] == "author":
        if len(sys.argv) == 3:
            authors = data_source.authors(sys.argv[2])
            print_author(authors)
        elif len(sys.argv) == 2:
            authors = data_source.authors()
            print_author(authors)
        else:
            print("Too many arguments provided, please type 'python3 books.py help' to see command line interface")
    elif sys.argv[1] == "year":
        if len(sys.argv) == 4:
            years = data_source.books_between_years(sys.argv[2], sys.argv[3])
            for book in years:
                print(book.title, book.publication_year)
        elif len(sys.argv) == 3:
            years = data_source.books_between_years(sys.argv[2])
            for book in years:
                print(book.title, book.publication_year)
        elif len(sys.argv) == 2:
            years = data_source.books_between_years()
            for book in years:
                print(book.title, book.publication_year)
        else:
            print("Too many arguments provided, please type 'python3 books.py help' to see command line interface")

    elif sys.argv[1] == "help":
        file = open("usage.txt", "r")
        print(file.read())
    else:
        print("Command not found, please type 'python3 books.py help' to see command line interface")

       
if __name__ == '__main__':
    main()
