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
    else:\
        results = data_source.books_between_years(sys.argv[2], sys.argv[3])
    for book in results:
        print(book)


def main():
    data_source = booksdatasource.BooksDataSource('books1.csv')
    
    if (len(sys.argv) <=1):
       print("input error")
    
    elif (len(sys.argv) <= 3):
            display_authors(data_source)
        
    elif (len(sys.argv) <= 4):
            display_books(data_source)

    elif (len(sys.argv) <= 4):
            display_years(data_source)
    
    else: 
         print("error")
       
if __name__ == '__main__':
    main()
