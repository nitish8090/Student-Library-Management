from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import UserViewSet

router = SimpleRouter()
router.register('User', UserViewSet, basename='User')
urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.obtain_auth_token)
]
