# blog/views.py
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Service, People, Languages
from django.shortcuts import render


# Create your views here.
class HomeView(ListView):
	model = Languages
	template_name = 'home.html'

class AboutView(TemplateView):
	template_name = 'about.html'
	
	
class ContactView(TemplateView):
	template_name = 'contact.html'

class ServiceView(ListView):
	model = Service
	template_name = 'service.html'

class RegisterView(CreateView):
	model = People
	template_name = 'register.html'
	fields= ['first_name', 'last_name', 'phone_no', 'email']
	
class ThanksView(TemplateView):
	template_name = 'thanks.html'

