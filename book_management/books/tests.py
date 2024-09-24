from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User
from django.test import TestCase


class BookModelTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_date="2023-01-01"
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(str(self.book.publication_date), "2023-01-01")

    def test_book_str_representation(self):
        self.assertEqual(str(self.book), "Test Book")

    def test_book_update(self):
        self.book.title = "Updated Test Book"
        self.book.save()
        updated_book = Book.objects.get(id=self.book.id)
        self.assertEqual(updated_book.title, "Updated Test Book")


from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User


class BookAPITest(APITestCase):

    def setUp(self):
        # Создаем пользователя
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Получаем JWT-токен
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpass'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']

        # Добавляем заголовок Authorization для всех последующих запросов
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # Создаем тестовую книгу
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_date="2023-01-01"
        )
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.id})

    def test_create_book(self):
        url = reverse('book-list-create')
        data = {
            "title": "New Book",
            "author": "New Author",
            "publication_date": "2023-02-01"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_book(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book")

    def test_update_book(self):
        data = {
            "title": "Updated Test Book",
            "author": "Updated Author",
            "publication_date": "2023-03-01"
        }
        response = self.client.put(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_book = Book.objects.get(id=self.book.id)
        self.assertEqual(updated_book.title, "Updated Test Book")

    def test_delete_book(self):
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
