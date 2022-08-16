# blog/urls.py
from django.urls import path
from .views import HomeView, ThanksView, ContactView, AboutView, ServiceView, RegisterView


urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('contact', ContactView.as_view(), name='contact'),
	path('about', AboutView.as_view(), name='about'),
	path('service', ServiceView.as_view(), name='service'),
	path('register', RegisterView.as_view(), name='register'),
	path('thanks', ThanksView.as_view(), name='thanks'),
	]
