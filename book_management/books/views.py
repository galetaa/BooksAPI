# books/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from .tasks import send_book_message


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book = serializer.save()
        send_book_message.delay('create', book.id)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        book = serializer.save()
        send_book_message.delay('update', book.id)

    def perform_destroy(self, instance):
        book_id = instance.id
        instance.delete()
        send_book_message.delay('delete', book_id)
