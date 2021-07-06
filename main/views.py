from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import TrainingList



# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SigninView(TemplateView):
    template_name = 'signin.html'

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class HomeView(ListView):
    template_name = 'home.html'
    model = TrainingList


class TestView(TemplateView):
    template_name = 'test.html'
