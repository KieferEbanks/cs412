# file: django/hw/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

import time # This is to show its a static website
import random

# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    '''A function that responds to the home request'''

    response_text = f'''
    <html>
        <h1>Hello, World!</h1>
        The current time is: { time.ctime() }.
    </html>
    '''

    return HttpResponse(response_text)

def home_page(request: HttpRequest) -> HttpResponse:
    '''A function that responds to the home request using a template'''

    template_name = 'hw/home.html'

    #dictionary of context variables to pass to the template
    context = {
        "time": time.ctime(),
        "letter1": chr(random.randint(65, 90)), #random uppercase letter
        "letter2": chr(random.randint(65, 90)),
        "number": random.randint(1, 10),
    }

    return render(request, template_name, context)


def about(request: HttpRequest) -> HttpResponse:
    '''A function that responds to the about request using a template'''

    template_name = 'hw/about.html'

    #dictionary of context variables to pass to the template
    context = {
        "time": time.ctime(),
        "letter1": chr(random.randint(65, 90)), #random uppercase letter
        "letter2": chr(random.randint(65, 90)),
        "number": random.randint(1, 10),
    }

    return render(request, template_name, context)
