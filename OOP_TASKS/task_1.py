"""Задача 1: Создание библиотеки
Создайте библиотеку для управления коллекцией книг.
Каждая книга должна быть представлена как объект, содержащий атрибуты:
-название
-автор
-год издания
-жанр
-количество страниц.
Библиотека должна поддерживать следующие операции:

1. Добавление книги.
2. Удаление книги.
3. Поиск книги по названию.
4. Вывод всех книг одного автора.
5. Вывод всех книг, отсортированных по году издания.

Используйте свойства для проверки корректности ввода данных (например, год издания должен быть положительным числом)."""

'''
создаем класс книги
__init__ - конструктор
__str__ - метод для вывода информации о книге
is_year_valid - метод для проверки корректности года издания
'''
class Book:
    def __init__(self, name: str, author: str, year: int, genre: str, pages: int):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages

    def __str__(self):
        return (f'Название: {self.name}\n'
                f'Автор: {self.author}\n'
                f'Год издания: {self.year}\n'
                f'Жанр: {self.genre}\n'
                f'Количество страниц: {self.pages}\n')

    @property
    def is_year_valid(self):
        return self.year > 0

'''
создаем библиотеку с книгами
__init__ - конструктор
add_book - метод для добавления книги в библиотеку
remove_book - метод для удаления книги из библиотеки
search_by_title - метод для поиска книги по названию
get_books_by_author - метод для поиска книг по автору
get_books_sorted_by_year - метод для сортировки книг по году издания
'''
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        if book.is_year_valid:
            if isinstance(book, Book):
                self.books.append(book)
            else:
                print('Неверный тип данных')

    def remove_book(self, book: Book):
        self.books.remove(book)

    def search_by_title(self, title: str):
        for book in self.books:
            if title.lower() in book.name.lower():
                return book.name, book.author, book.year
        return None

    def get_books_by_author(self, author: str):
        books_by_author = [book.name for book in self.books if author.lower() in book.author.lower()]
        return books_by_author if books_by_author else None

    def get_books_sorted_by_year(self):
        sorted_books = sorted(self.books, key=lambda book: book.year)
        return [f"{book.name} - {book.author}" for book in sorted_books]


if __name__ == '__main__':
    library = Library()
    book1 = Book("Название1", "Автор1", 2001, "Жанр1", 300)
    book2 = Book("Название2", "Автор2", 1999, "Жанр2", 150)
    library.add_book(book1)
    library.add_book(book2)
    print(library.search_by_title("Название1"))
    print('--------')
    print(library.get_books_by_author("Автор1"))
    print('--------')
    print(library.get_books_sorted_by_year())