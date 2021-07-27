from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # add this line for chapter 3 tests
    return HttpResponse("Rango says hey there partner!<a href='/rango/about/'>About</a>")
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")