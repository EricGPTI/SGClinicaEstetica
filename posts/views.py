from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

class PostsList(ListView):
    pass

class PostsSearch(PostsList):
    pass

class PostsCategory(PostsList):
    pass

class PostsDetails(UpdateView):
    pass


