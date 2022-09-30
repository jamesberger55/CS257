import booksdatasource
import sys

def authors_display(data_source):
    if (len(sys.argv) == 2):
       results = data_source.authors()
    else:
       results = data_source.authors(sys.argv[2])
    for author in results:
       print(author)
 
def books_display(data_source):
    if (len(sys.argv) == 2):
        results = data_source.books()
    elif (len(sys.argv) == 3): 
        results = data_source.books(sys.argv[2])
    else:
        results = data_source.books(sys.argv[2], sys.argv[3])
    for book in results:
        print(book)

def year_display(data_source):
    if (len(sys.argv) == 2):
        results = data_source.books_between_years()
    elif (len(sys.argv) == 3): 
        results = data_source.books_between_years(sys.argv[2])
    else:
        results = data_source.books_between_years(sys.argv[2], sys.argv[3])
    for book in results:
        print(book)


def main():
    data_source = booksdatasource.BooksDataSource('books1.csv')
    '''
    if (len(sys.argv) <=1):
       print("input error")
    
    elif (len(sys.argv) <= 3):
            authors_display(data_source)
        
    elif (len(sys.argv) <= 4):
            books_display(data_source)

    elif (len(sys.argv) <= 4):
            year_display(data_source)
    
    else: 
         print("error")
    '''

    if (len(sys.argv) < 2):
        print("More arguments required, please see man to see command line interface")
    elif sys.argv[1] == "title":
        if len(sys.argv) == 3:
            books = data_source.books(sys.argv[2])
            print(books)
        elif len(sys.argv) == 2:
            books = data_source.books()
            print(books)
        else:
            print("Too many arguments provided, please see man to see command line interface")
    elif sys.argv[1] == "author":
        if len(sys.argv) == 3:
            authors = data_source.authors(sys.argv[2])
            print(authors)
        elif len(sys.argv) == 2:
            authors = data_source.authors()
            print(authors)
        else:
            print("Too many arguments provided, please see man to see command line interface")
    elif sys.argv[1] == "years":
        if len(sys.argv) == 4:
            years = data_source.books_between_years(sys.argv[2], sys.argv[3])
            print(years)
        elif len(sys.argv) == 3:
            years = data_source.books_between_years(sys.argv[2])
            print(years)
        elif len(sys.argv) == 2:
            years = data_source.books_between_years()
            print(years)
        else:
            print("Too many arguments provided, please see man to see command line interface")

    elif sys.argv[1] == "man":
        file = open("usage.txt", "r")
        print(file.read())
    else:
        print("Command not found, please see man to see command line interface")

       
if __name__ == '__main__':
    main()
