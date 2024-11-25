import datetime as dt
import Library

def main()-> None:
    """
    """
    print("Добро пожаловать в систему управление библиотекой!")
    my_library = Library.Library()
    while True:
        print("\nМеню управление библиотекой:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        user_input = input("\n").strip()[0]

        match user_input:
            case "1":
                title = input("Введите название книги: ").strip()
                author = input("Введите автора книги: ").strip()
                year = input("Введите год издания книги: ").strip()
                if not year.isdigit() or int(year) < 0 or int(year) > dt.datetime.now().year:
                    print("Неккоректный год.")
                    continue
                if not author.isalpha():
                    print("Неккоректный ввод имени автора")
                    continue
                my_library.add_book(title, author, int(year))

            case "2":
                book_id = input("Введите ID книги для удаления: ").strip()
                if not book_id.isdigit() or int(book_id) < 0:
                    print("Неккоректный ввод ID.")
                    continue
                my_library.delete_book(int(book_id))
            
            case "3":
                search_field = input("Введите поле для поиска:\n"
                                     "1. Заголовок\n"
                                     "2. Автор\n"
                                     "3. Год\n")
                query = input("Введи данные: ")
                print("Результат поиска: ")
                my_library.search_book(search_field, query)

            case "4":
                my_library.show_books()

            case "5":
                book_id = input("Введите ID книги для изменения статуса: ").strip()
                if not book_id.isdigit() or int(book_id) < 0:
                    print("Неккоректный ввод ID.")
                    continue
                status = input("Введите новый статус книги (в наличии/выдана): ").strip()
                if status not in ("в наличии", "выдана"):
                    print("Некоректный ввод статуса")
                    continue
                my_library.change_book_status(int(book_id), status)

            case "6":
                print("Выход из системы управление библиотекой.")
                my_library.exit()

            case _:
                print("Что-то пошло не так.\nУбедитесь в корректности запроса.")

if __name__ == "__main__":
    main()