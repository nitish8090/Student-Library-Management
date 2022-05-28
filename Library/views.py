from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Book, BookIssue
from .serializers import BookSerializer, BookIssueSerializer
from StudentLibrarian.models import Student, Librarian


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['created_by'] = request.user.username

        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    @action(detail=True, url_path='IssueBook', methods=['POST'])
    def issue_book(self, request, pk):

        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response('Book not found', status=404)

        try:
            student = Student.objects.get(serial=request.data['student_serial'])
        except Student.DoesNotExist:
            return Response("Student not found", status=404)
        except KeyError as e:
            return Response(f"Please send {e}", status=400)

        try:
            librarian = Librarian.objects.get(username=request.user.username)
        except Librarian.DoesNotExist:
            return Response("Librarian not found", status=404)

        if book.quantity - book.quantity_issued > 0:
            book_issue = BookIssue(book=book, student=student, issued_by=librarian)

            book.quantity_issued += 1
            book_issue.save()
            book.save()

            serializer = BookIssueSerializer(book_issue)
            return Response(serializer.data, status=201)
        else:
            return Response("No book remaining to issue")

    @action(detail=True, url_path='ReturnBook', methods=['POST'])
    def return_book(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response('Book not found', status=404)

        try:
            student = Student.objects.get(serial=request.data['student_serial'])
        except Student.DoesNotExist:
            return Response("Student not found", status=404)
        except KeyError as e:
            return Response(f"Please send {e}", status=400)

        try:
            book_issue = BookIssue.objects.get(book=book, student=student, is_returned=False)
        except BookIssue.DoesNotExist:
            return Response(f"No books with this id {book.name} issued to student: {student.full_name}")

        book.quantity_issued -= 1
        book.save()

        book_issue.is_returned = True
        book_issue.save()


class BookIssueViewSet(viewsets.ModelViewSet):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
