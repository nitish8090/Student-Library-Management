from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from django.conf import settings

from .models import Student, Librarian
from .serializers import StudentSerializer, LibrarianSerializer
from UserManager.models import User
from UserManager.serializers import UserSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['created_by'] = request.user.username

        try:
            User.objects.get(username=request.data['username']['username'])
        except User.DoesNotExist:
            try:
                request.data['username']['role'] = 'Student'
                user_serializer = UserSerializer(data=request.data['username'])
            except KeyError as e:
                return Response(f"Please send {e}", status=400)

            if user_serializer.is_valid():
                new_student_user = user_serializer.save()
            else:
                return Response(user_serializer.errors)
        except KeyError as e:
            return Response(f"Please send {e}", status=400)
        else:
            return Response("Username already exists.", status=400)

        request.data['username'] = new_student_user.username

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class LibrarianViewSet(viewsets.ModelViewSet):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['created_by'] = request.user.username

        try:
            User.objects.get(username=request.data['username']['username'])
        except User.DoesNotExist:
            try:
                request.data['username']['role'] = 'Librarian'
                user_serializer = UserSerializer(data=request.data['username'])
            except KeyError as e:
                return Response(f"Please send {e}", status=400)

            if user_serializer.is_valid():
                new_librarian_user = user_serializer.save()
            else:
                return Response(user_serializer.errors)
        except KeyError as e:
            return Response(f"Please send {e}", status=400)
        else:
            return Response("Username already exists.", status=400)

        request.data['username'] = new_librarian_user.username

        serializer = LibrarianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
