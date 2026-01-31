# File: urls.py
# Author: Kiefer Ebanks (kebanks@bu.edu), 1/27/2026
# Description: The URL file for the quotes app
# Creating the URLs for the quotes app


from django.urls import path
from django.conf import settings
from . import views
 
# Creating my URL paths.
urlpatterns = [ 
    path(r'', views.home, name="home"), # the default home page
    path(r'quote/', views.quote, name="quote"), # page that shows a random quote and image
    path(r'show_all/', views.show_all, name="show_all"), # page that shows all Tom Brady quotes and images
    path(r'about/', views.about, name="about"), # page that shows basic information about Tom Brady and myself
]