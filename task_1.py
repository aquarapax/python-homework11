# Задача 1 Тестирование методов класса Разработать набор модульных тестов для класса BooksCollector.
class BooksCollector:
    def __init__(self):
        # Словарь для хранения книг и соответствующих им жанров
        self.books_genre = {}
        # Список для хранения избранных книг
        self.favorites = []
        # Список доступных жанров
        self.genres = []
        # Словарь для хранения возрастных рейтингов жанров
        self.genre_age_rating = {} 

    def add_new_book(self, book_name):
        """Добавляет новую книгу в словарь без указания жанра"""
        # Если книги нет в словаре добавляем и устанавливаем жанр книги как None
        if book_name not in self.books_genre: 
            self.books_genre[book_name] = None

    def set_book_genre(self, book_name, genre):
        """Устанавливает жанр книги"""
        # Проверяем, существует ли книга
        if book_name in self.books_genre:
            self.books_genre[book_name] = genre  # Устанавливаем жанр книги
            # Если жанр не добавлен в список жанров, добавляем его
            if genre not in self.genres:
                self.genres.append(genre)

    def set_age_rating(self, genre, age_rating):
        """Устанавливает возрастной рейтинг для жанра"""
        # Устанавливаем возрастной рейтинг для указанного жанра
        self.genre_age_rating[genre] = age_rating

    def get_book_genre(self, book_name):
        """Выводит жанр книги по ее имени"""
        # Возвращаем жанр книги, если он есть в словаре
        return self.books_genre.get(book_name)

    def get_books_with_specific_genre(self, genre):
        """Выводит список книг с определённым жанром"""
        # Возвращаем список книг, которые имеют указанный жанр
        return [book for book, g in self.books_genre.items() if g == genre]

    def get_books_genre(self):
        """Выводит текущий словарь books_genre"""
        # Возвращаем весь словарь книг и их жанров
        return self.books_genre

    def get_books_for_children(self, max_age):
        """Возвращает книги, которые подходят детям по возрастному рейтингу"""
        # Получаем подходящие жанры для указанного максимального возраста
        suitable_genres = [
            genre for genre, rating in self.genre_age_rating.items()
            if self.parse_age_rating(rating) <= max_age
        ]
        # Возвращаем список книг, жанр которых входит в список подходящих жанров
        return [book for book, g in self.books_genre.items() if g in suitable_genres]

    def parse_age_rating(self, age_rating):
        """Парсит возрастной рейтинг и возвращает максимальный возраст"""
        # Если возрастной рейтинг заканчивается на '+', возьмем число до знака '+'
        if age_rating.endswith("+"):
            return int(age_rating[:-1])  # Возвращаем число в виде integer
        return int(age_rating)  # Возвращаем ранжированный возраст

    def add_book_in_favorites(self, book_name):
        """Добавляет книгу в избранное"""
        # Проверяем, что книга существует и она не добавлена ранее в избранное
        if book_name in self.books_genre and book_name not in self.favorites:
            self.favorites.append(book_name)  # Добавляем книгу в избранное

    def delete_book_from_favorites(self, book_name):
        """Удаляет книгу из избранного"""
        # Проверяем, что книга есть в избранном
        if book_name in self.favorites:
            self.favorites.remove(book_name)  # Удаляем книгу из избранного

    def get_list_of_favorites_books(self):
        """Получает список избранных книг"""
        # Возвращаем список избранных книг
        return self.favorites

    def get_age_rating(self, genre):
        """Возвращает возрастной рейтинг для жанра"""
        # Возвращаем возрастной рейтинг, если он установлен для жанра
        return self.genre_age_rating.get(genre)
