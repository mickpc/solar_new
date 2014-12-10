"""
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

#from blog.models import posts

def foo(request):
    render_to_response("templates/index.html", {"foo": "bar"})
"""
"""
from django.http import HttpResponse

def foo(request):
    return HttpResponse("Hello World!")

#def foo(request):
#     return render_to_response('index.html')
"""
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

import graph

def index(request):

	graph.generate()

	
# Request the context of the request.
# The context contains information such as the client's machine details, for example.
	context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
	context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
	return render_to_response('index.html', context_dict, context)

#def index(request):
#    return HttpResponse("Michael says hello world!")
