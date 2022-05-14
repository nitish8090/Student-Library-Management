from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import BookViewSet, BookIssueViewSet

router = SimpleRouter()
router.register('Book', BookViewSet)
router.register('BookIssue', BookIssueViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
