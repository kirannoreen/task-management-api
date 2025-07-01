# projects/urls.py
from django.http import HttpResponse
from django.urls import path

# Define the view function
def home(request):
    return HttpResponse("Welcome to the API!")

# Define the URL patterns
urlpatterns = [
    path('', home, name='home'),  # Route the root URL to the home view
]
