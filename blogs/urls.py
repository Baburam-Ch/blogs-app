from django.urls import path
from . views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = 'blogs'
urlpatterns = [
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='delete'),
    path('post/<int:pk>/update', BlogUpdateView.as_view(), name='update'),
    path('post/new/', BlogCreateView.as_view(), name='create'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('', BlogListView.as_view(), name='home'),
]
