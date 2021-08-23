from django.urls import path
from . views import BlogListView, BlogDetailView

app_name = 'blogs'
urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('', BlogListView.as_view(), name='home'),
]
