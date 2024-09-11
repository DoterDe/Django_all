from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from app.views import home, DeletePost, CreatePost, view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('view/', view, name='view'),
    path('create/', CreatePost.as_view(), name='create'),
    path('delete/<int:id>', DeletePost.as_view(), name='delete'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
