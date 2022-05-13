from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import StudentViewSet, LibrarianViewSet

router = SimpleRouter()
router.register('Student', StudentViewSet)
router.register('Librarian', LibrarianViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
