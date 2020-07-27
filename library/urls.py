from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import BookViewset, AuthorAPIView

router = DefaultRouter()
router.register(r'book', BookViewset, basename="Books")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    
    ]
