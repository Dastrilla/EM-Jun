import unittest
from Library import Library


lib = Library()

class TestAddBook(unittest.TestCase):
    def test_add_book(self):
        lib.add_book('It', 'Stiven', 1998)
        self.assertEqual(lib.books[-1].title, 'It')
        self.assertEqual(lib.books[-1].author, 'Stiven')
        self.assertEqual(lib.books[-1].year, 1998)


class TestDeleteBook(unittest.TestCase):
    def test_delet_book(self):
        last_book = lib.books[-1]
        lib.delete_book(lib.books[-1].id)
        self.assertNotIn(last_book, lib.books, "Последняя книга была удалена")

class TestSearchBook(unittest.TestCase):
    def test_search_book(self):
        pass


if __name__ == "__main__":
    unittest.main()