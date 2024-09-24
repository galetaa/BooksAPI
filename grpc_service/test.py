import grpc
from proto import book_service_pb2, book_service_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = book_service_pb2_grpc.BookServiceStub(channel)
        all_books_request = book_service_pb2.GetAllBooksRequest()
        all_books_response = stub.GetAllBooks(all_books_request)
        print("All Books: ", all_books_response)


if __name__ == '__main__':
    run()
