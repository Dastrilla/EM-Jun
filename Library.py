import os
import json


#path to data file
DATA_FILE = 'lib.json'


class Book:
    """
    Class for creating books, contains the required attributes:
    title, author, year
    The id and status attributes are created automatically
    """
    def __init__(self, title:str, author:str, year:int,
                 id: int = None, status: str = "в наличии") -> None:
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
    
    def to_dict(self) -> dict:
        """
        to_dict(self)
        returns a dictionary based on a class 
        """
        return self.__dict__
    
    @staticmethod
    def from_dict(data: dict)-> 'Book':
        """
        from_dict(data: dict)
        static function that returns an instance of a class
        based on input data (dictionary)
        """
        return Book(**data)
    
class Library:
    """
    A class for managing a library, contains functions for adding,
    deleting, searching, displaying and changing books.
    It also contains functions for generating id,
    loading and saving the library and exiting the program.
    """

    def __init__(self) -> None:
        self.books = Library.load_books()

    @staticmethod
    def save_books(books: list['Book']):
        """
        save_books(books: list['Book'])
        Static function for saving books in json format.
        """
        with open(DATA_FILE, 'w', encoding='utf-8') as DB:
            json.dump([Book.to_dict(book) for book in books], DB, ensure_ascii=False, indent=4)

    @staticmethod
    def load_books() -> list['Book']:
        """
        load books()
        Static function for loading a library of books
        from json format. If the library is present,
        the function returns
        a list of books.[Book] otherwise,
        the function returns an empty list.
        """
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as DB:
                    return [Book.from_dict(book) for book in json.load(DB)]
        return []

    def generator_id(self) -> int:
        """
        generator_id(self)
        Function for generating id.
        Returns the next id.
        In the case of the first generation, returns 1
        return int
        """
        if self.books:
            return self.books[-1].id + 1
        return 1
    
    def add_book(self, title:str, author:str, year:int) -> None:
        """
        add_book(self, title:str, author:str, year:int)
        Function for adding books to the library
        Accepts arguments: title, author, year
        Creates an instance of the Book class,
        adds it to the list of all books,
        and stores it in the library.
        return None
        """
        book = Book(title, author, year, id = self.generator_id())
        self.books.append(book)
        Library.save_books(self.books)
        print(f"Книга {book.title} добавлена с ID {book.id}.")

    def delete_book(self, id: int) -> None:
        """
        delete_book(self, id:int)
        The function for deleting a book from the library
        takes one argument - the id of the book, deletes the book and saves it;
        if the id is missing, it displays a corresponding message.
        return None
        """
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                print(f"Книга с ID:{id} удалена.")
                Library.save_books(self.books)
                return None
        print(f"Книги с ID:{id} не существует.")

    def search_book(self, search_field: str, query: str) -> None:
        """
        search_book(self, search_field: str, query: str)
        The function for searching a book takes two arguments:
        Search field and query
        Depending on the selected search field,
        a request is made and the corresponding information
        is displayed on the screen.
        If there is no or incorrect input,
        a corresponding message will be displayed.
        return None
        """

        match search_field:
            case "1":
                result =[book for book in self.books if query.lower() in book.title.lower()]
            case "2":
                result =[book for book in self.books if query.lower() in book.author.lower()]
            case "3":
                result =[book for book in self.books if int(query) == book.year]
            case _:
                print("Что-то пошло не так :(")

        if result:
            self.show_books(result)
        else:
            print("Ничего не найдено :(")
            
    def show_books(self, books: list["Book"] = None) -> None:
        """
        show_books(self, books: list["Book"])
        A function for displaying books in a human-friendly format.
        Accepts an optional books argument necessary to display not
        the entire library of books
        return None
        """
        if len(self.books) == 0:
            print("Библиотека пустая!")
            return None
        headers = self.books[0].__dict__.keys()
        row_format = "{:<15} " * len(headers)
        if books is None:
            print(row_format.format(*headers))
            for book in self.books:
                print(row_format.format(*book.__dict__.values()))
            return None
        print(row_format.format(*headers))
        for book in books:
            print(row_format.format(*book.__dict__.values()))

    def change_book_status(self, id: int, status: str) -> None:
        """
        change_book_status(self, id: int, status: str)
        Function for changing the status of books.
        Accepts arguments: id, status
        Finds the required book by id and changes its status
        to the one specified by the user (in stock/issued);
        in case of incorrect data entry,
        a corresponding message is displayed
        return None
        """
        for book in self.books:
            if book.id == id:
                if status != book.status:
                    book.status = status.lower()
                    Library.save_books(self.books)
                    print(f"Изменен статус книги с ID({id}):{status}")
                    return None
                print("Такой статус уже установлен")
                return None
        print(f"Книги с ID:{id} не существует.")

    @staticmethod
    def exit()-> None:
        """
        exit()
        static function to exit the program
        return None
        """
        quit()