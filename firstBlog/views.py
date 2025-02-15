from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, TechPost


def home(request):
    return render(request, 'base.html', {})

class HomeView(ListView):
    model= Post
    template_name = 'home.html'
    


class MentalView(ListView):
    model= Post
    template_name = 'mental.html'


class TechView(ListView):
    model= TechPost
    template_name = 'tech.html'



class articalDetailsView(DetailView):
    model= Post
    template_name = 'detailsView.html'
    
class addBlogView(CreateView):
    model= Post
    template_name = 'add_blog.html'
    fields= '__all__'