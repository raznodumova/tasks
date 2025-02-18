"""Задача 1: Создание библиотеки
Создайте б-ку для управления коллекцией книг.
Каждая книга должна быть представлена как объект, содержащий атрибуты:
-название
-автор
-год издания
-жанр
-кол-во страниц.
Б-ка должна поддерживать следующие операции:
Добавление книги
Удаление книги
Поиск книги по названию
Вывод всех книг одного автора
Вывод всех книг, отсортированных по году издания"""


class Book:
    """Cоздаем класс книги."""
    def __init__(self, name: str, author: str,
                 year: int, genre: str, pages: int):
        """Конструктор. """
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages

    def __str__(self):
        """Метод для вывода информации о книге."""
        return (f'Название: {self.name}\n'
                f'Автор: {self.author}\n'
                f'Год издания: {self.year}\n'
                f'Жанр: {self.genre}\n'
                f'Количество страниц: {self.pages}\n')

    @property
    def is_year_valid(self):
        """Метод для проверки года издания."""
        return self.year > 0


class Library:
    """Cоздаем библиотеку."""
    def __init__(self):
        """Конструктор."""
        self.books = []

    def add_book(self, book: Book):
        """Метод для добавления книги в библиотеку."""
        if isinstance(book, Book):
            if book.is_year_valid:
                self.books.append(book)
            else:
                raise ValueError('Год издания должен быть больше нуля.')

    def remove_book(self, book: Book):
        """Метод для удаления книги из библиотеки."""
        if book in self.books:
            self.books.remove(book)
        else:
            raise ValueError('Такой книги нет в библиотеке.')

    def search_by_title(self, title: str):
        """Метод для поиска книги по названию."""
        books_by_title = []
        for book in self.books:
            if title.lower() in book.name.lower():
                books_by_title.append(book.name)
        return books_by_title if books_by_title else []

    def get_books_by_author(self, author: str):
        """Метод для поиска книг по автору."""
        books_by_author = []
        for book in self.books:
            if author.lower() in book.author.lower():
                books_by_author.append(book.name)
        return books_by_author if books_by_author else []

    def get_books_sorted_by_year(self):
        """Метод для сортировки книг по году издания."""
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
