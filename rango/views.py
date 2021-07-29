from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page


def index(request):
    # Query the database for a list of ALL categories currently stored. Order the categories by the number of likes
    # in descending order. Retrieve the top 5 only -- or all if less than 5. Place the list in our context_dict
    # dictionary (with our boldmessage!) # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    pages_list = Page.objects.order_by('-views')[:5]
    # print(pages_list)
    for item in pages_list:
        print(item.title)
        print(item.views)

    context_dict['pages'] = pages_list
    return render(request, 'rango/index.html', context=context_dict)

    # context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'myname': 'zuho wang'}
    return render(request, 'rango/about.html', context=context_dict)
    # return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")


def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass # to the template rendering engine.
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)
