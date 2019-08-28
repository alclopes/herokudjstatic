from django.urls import path
from .views import index, exclude_images

app_name = 'mypage'

urlpatterns = [
    path('', index, name='index'),
    path('cleanimages/', exclude_images, name='exclude_images'),
]

