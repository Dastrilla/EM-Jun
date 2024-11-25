import os
import json


#path to data file
DATA_FILE = 'lib.json'


class Book:

    def __init__(self, title:str, author:str, year:int,
                 id: int = None, status: str = "в наличии") -> None:
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
    
    def to_dict(self) -> dict:
        return self.__dict__
    
    @staticmethod
    def from_dict(data: dict)-> 'Book':
        return Book(**data)
    
class Library:

    def __init__(self) -> None:
        self.books = Library.load_books()

    @staticmethod
    def save_books(books: list['Book']):
        with open(DATA_FILE, 'w', encoding='utf-8') as DB:
            json.dump([Book.to_dict(book) for book in books], DB, ensure_ascii=False, indent=4)

    @staticmethod
    def load_books() -> list['Book']:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as DB:
                    return [Book.from_dict(book) for book in json.load(DB)]
        return []

    def generator_id(self) -> int:
        if self.books:
            return self.books[-1].id + 1
        return 1
    
    def add_book(self, title:str, author:str, year:int) -> None:
        book = Book(title, author, year, id = self.generator_id())
        self.books.append(book)
        Library.save_books(self.books)
        print(f"Книга {book.title} добавлена с ID {book.id}.")

    def delete_book(self, id: int) -> None:
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                print(f"Книга с ID:{id} удалена.")
                Library.save_books(self.books)
                return None
        print(f"Книги с ID:{id} не существует.")

    def search_book(self, search_field: str, query: str) -> None: 

        match search_field:
            case "1":
                result =[book for book in self.books if query.lower() in book.title.lower()]
            case "2":
                result =[book for book in self.books if query.lower() in book.author.lower()]
            case "3":
                result =[book for book in self.books if int(query) == book.year]
            case _:
                print("Неправильное поле для поиска, убедитесь в корректном выборе.")

        if result:
            self.show_books(result)
        else:
            print("Ничего не найдено :(")
            
    def show_books(self, books: list["Book"] = None) -> None:
        if books is None:
            if len(self.books) == 0:
                print("Библиотека пустая!")
                return None
            headers = self.books[0].__dict__.keys()
            row_format = "{:<15} " * len(headers)
            print(row_format.format(*headers))
            for book in self.books:
                print(row_format.format(*book.__dict__.values()))
            return None
        print(row_format.format(*headers))
        for book in books:
            print(row_format.format(*book.__dict__.values()))

    def change_book_status(self, id: int, status: str) -> None:
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
        quit()