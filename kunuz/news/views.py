from django.shortcuts import render
from django.views.generic import ListView
from .models import News

# Create your views here.
class Newsview(ListView):
    model= News
    template_name = 'news.html'