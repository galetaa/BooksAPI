import grpc
from concurrent import futures
import time
import logging

from proto import book_service_pb2_grpc, book_service_pb2
from database import get_book_by_id, get_all_books


class BookService(book_service_pb2_grpc.BookServiceServicer):

    def GetBookById(self, request, context):
        book = get_book_by_id(request.id)
        if book:
            return book_service_pb2.BookResponse(
                id=book['id'],
                title=book['title'],
                author=book['author'],
                publication_date=str(book['publication_date'])
            )
        else:
            context.set_details('Book not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return book_service_pb2.BookResponse()

    def GetAllBooks(self, request, context):
        books = get_all_books()
        return book_service_pb2.BookListResponse(
            books=[
                book_service_pb2.BookResponse(
                    id=book['id'],
                    title=book['title'],
                    author=book['author'],
                    publication_date=str(book['publication_date'])
                )
                for book in books
            ]
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    book_service_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()

    logging.info("Starting server on [::]:50051")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Server stopped by user.")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()
