from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .models import User
from .serializers import UserSafeSerializer


class UserViewSet(viewsets.ViewSet):

    @action(methods=['POST'], url_path='Register', detail=False)
    def register(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
        except Exception as e:
            return Response(f"Please send {e}", status=400)

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username,
                        password=password)
            user.save()
            serializer = UserSafeSerializer(user)
            return Response(serializer.data, status=400)
        else:
            return Response("User already registered", status=500)

    @action(detail=False, methods=['POST'], url_path='Login')
    def login(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
        except Exception as e:
            return Response(f"Please send {e}", status=400)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(f"User not found", status=400)
        else:

            if user.password == password:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'message': 'Login Successful',
                    'token': token.key
                })
            else:
                return Response({
                    'message': 'Login Failed, invalid credentials'
                })
