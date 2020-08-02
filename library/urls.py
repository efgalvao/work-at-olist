from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from api.views import BookView, AuthorViewSet

router = DefaultRouter()
router.register(r'author', AuthorViewSet)
router.register(r'book', BookView)

urlpatterns = [
    path('', include(router.urls)),
    path('openapi', get_schema_view(
        title="Olist Library API",
        description="Store book and authors data with a REST API",
        version="1.0.0"
    ), name='openapi-schema'),
]
