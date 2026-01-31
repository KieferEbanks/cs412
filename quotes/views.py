# File: views.py
# Author: Kiefer Ebanks (kebanks@bu.edu), 1/27/2026
# Description: The views file for the quotes app
# Creating the different views functions that handle the different http calls for different pages

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest # had to import these to handle HTTP requests and responses

import random # need this to select random quotes and images

# My global list of Tom Brady quotes:
quotes_list = ["You wanna know which ring is my favorite? The next one.",
               "If you don’t believe in yourself why is anyone else going to believe in you?",
               "I did not come this far to only come this far, so we have still got further to go."]

# My global list of Tom Brady images:
images_list = ["https://www.patriotshalloffame.com/wp-content/uploads/CP100117_EJA0059a-scaled.jpg",
               "https://people.com/thmb/2OsLFMYY7HdmyrNVbwHWIji1VdM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(599x0:601x2)/Tom-Brady-eb437ed7e54743d69a89a4d73c2fa004.jpg",
               "https://cst.brightspotcdn.com/dims4/default/0e57664/2147483647/strip/true/crop/3363x2242+0+0/resize/840x560!/quality/90/?url=https%3A%2F%2Fcdn.vox-cdn.com%2Fthumbor%2FJyC-NfPUwIGEkPfgs0Ry28iffis%3D%2F0x0%3A3363x2242%2F3363x2242%2Ffilters%3Afocal%281571x800%3A1572x801%29%2Fcdn.vox-cdn.com%2Fuploads%2Fchorus_asset%2Ffile%2F22288692%2FAP21039133644772.jpg",
               ]



def home(request):
    '''
    Creating a default view to handle the 'home' request.
    '''
 
    template_name = 'quotes/home.html'

    #dictionary of context variables to pass to the template
    context = {
        "quote": random.choice(quotes_list),
        "image": random.choice(images_list),
    }

    return render(request, template_name, context)


def quote(request):
    '''
    A view to display a random quote.
    '''

    template_name = 'quotes/quote.html'
    
    context = {
        "quote": random.choice(quotes_list),
        "image": random.choice(images_list),
    }
    
    return render(request, template_name, context)

def show_all(request):
    '''
    A view to display all quotes.
    '''

    template_name = 'quotes/show_all.html'

    
    context = {
        "quotes_list" : quotes_list,
        "image_list": images_list,
    }
    
    return render(request, template_name, context)

def about(request):
    '''
    A view to display information about the quotes app. This page doesn't need any context variables.
    '''
    
    template_name = 'quotes/about.html'
    
    return render(request, template_name)
