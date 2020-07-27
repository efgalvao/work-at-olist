from django.urls import path, include
from .views import AuthorAPIView, AuthorSearchView, BookSearch
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('author/<int:pk>/', AuthorAPIView.as_view()),
    path('author/', AuthorSearchView.as_view()),
    path('search/', BookSearch.as_view()),

]
