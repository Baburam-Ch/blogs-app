from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'blogs/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogs/detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blogs/create.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blogs/update.html'
    fields = ('title', 'body')

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blogs/delete.html'
    success_url = reverse_lazy('blogs:home')
