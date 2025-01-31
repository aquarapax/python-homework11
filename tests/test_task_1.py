import unittest
from task_1 import BooksCollector

class TestBooksCollector(unittest.TestCase):

    def setUp(self):
        """Создает новый экземпляр BooksCollector перед каждым тестом."""
        self.collector = BooksCollector()

    def tearDown(self):
        """Очистка после теста."""
        del self.collector

    def test_add_new_book(self):
        """Тест для добавления новой книги без жанра."""
        self.collector.add_new_book('Гарри Поттер')
        self.assertIn('Гарри Поттер', self.collector.books_genre)
        self.assertIsNone(self.collector.books_genre['Гарри Поттер'])

    def test_set_book_genre(self):
        """Тест для установки жанра книги."""
        self.collector.add_new_book('Гарри Поттер')
        self.collector.set_book_genre('Гарри Поттер', 'Фэнтези')
        self.assertEqual(self.collector.books_genre['Гарри Поттер'], 'Фэнтези')
        self.assertIn('Фэнтези', self.collector.genres)

    def test_set_book_genre_for_nonexistent_book(self):
        """Тест для попытки установки жанра для несуществующей книги."""
        self.collector.set_book_genre('Несуществующая книга', 'Фэнтези')
        self.assertNotIn('Фэнтези', self.collector.genres)

    def test_set_age_rating(self):
        """Тест для установки возрастного рейтинга."""
        self.collector.set_age_rating('Фэнтези', '12+')
        self.assertEqual(self.collector.get_age_rating('Фэнтези'), '12+')

    def test_get_book_genre(self):
        """Тест для получения жанра книги по имени."""
        self.collector.add_new_book('Гарри Поттер')
        self.collector.set_book_genre('Гарри Поттер', 'Фэнтези')
        self.assertEqual(self.collector.get_book_genre('Гарри Поттер'), 'Фэнтези')

    def test_get_books_with_specific_genre(self):
        """Тест для получения списка книг с определенным жанром."""
        self.collector.add_new_book('Гарри Поттер')
        self.collector.set_book_genre('Гарри Поттер', 'Фэнтези')
        self.collector.add_new_book('Властелин колец')
        self.collector.set_book_genre('Властелин колец', 'Фэнтези')
        self.collector.add_new_book('Матрица')
        self.collector.set_book_genre('Матрица', 'Научная фантастика')

        fantasy_books = self.collector.get_books_with_specific_genre('Фэнтези')
        self.assertIn('Гарри Поттер', fantasy_books)
        self.assertIn('Властелин колец', fantasy_books)
        self.assertNotIn('Матрица', fantasy_books)

    def test_get_books_for_children(self):
        """Тест для получения книг, подходящих для детей по возрастному рейтингу. 
            Тест подогнан под условия задачи, где рейтинг устанавливается на жанр а не на саму книгу"""
        self.collector.add_new_book('Гарри Поттер')
        self.collector.set_book_genre('Гарри Поттер', 'Фэнтези')
        self.collector.set_age_rating('Фэнтези', '8+')

        self.collector.add_new_book('Властелин колец')
        self.collector.set_book_genre('Властелин колец', 'Фантастика')
        self.collector.set_age_rating('Фантастика', '12+')

        suitable_books = self.collector.get_books_for_children(10)
        self.assertNotIn('Властелин колец', suitable_books)
        self.assertIn('Гарри Поттер', suitable_books)

    def test_add_and_remove_favorite(self):
        """Тест для добавления и удаления книги из избранного."""
        self.collector.add_new_book('Гарри Поттер')
        self.collector.add_book_in_favorites('Гарри Поттер')
        self.assertIn('Гарри Поттер', self.collector.get_list_of_favorites_books())

        self.collector.delete_book_from_favorites('Гарри Поттер')
        self.assertNotIn('Гарри Поттер', self.collector.get_list_of_favorites_books())

    def test_get_age_rating(self):
        """Тест для получения возраста жанра."""
        self.collector.set_age_rating('Фэнтези', '16+')
        self.assertEqual(self.collector.get_age_rating('Фэнтези'), '16+')

if __name__ == '__main__':
    unittest.main()