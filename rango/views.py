from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from django.http import HttpResponse
from unicodedata import category

from rango.models import Category
from rango.models import Page





def index (request):
    # return HttpResponse('why did u play chunriying? <a href="/rango/about/">About</a>')
    # return HttpResponse('why did u play chunriying?')

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]



    # print("_____________" + category_list)
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categoriesmessage'] = 'Most Liked Categories!'
    context_dict['pagesmessage'] = 'Most Viewed Pages!'


    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)



def about (request):
    # return HttpResponse('Rango says here is the about page. <a href="/rango/">Index</a>')
    context_dict = {'boldmessage': 'This tutorial has been put together by Fanhao'}

    return render(request, 'rango/about.html')



def show_category(request,category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug = category_name_slug)
        pages = Page.objects.filter(category = category)
        context_dict['category'] = category
        context_dict['pages'] = pages

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)


# def index(request):
# # Construct a dictionary to pass to the template engine as its context.
# # Note the key boldmessage matches to {{ boldmessage }} in the template!
#     context_dict = {'boldmessage': '求求你们不要再去日本'}
# # Return a rendered response to send to the client.
# # We make use of the shortcut function to make our lives easier.
# # Note that the first parameter is the template we wish to use.
#
#     return render(request, 'rango/index.html', context=context_dict)