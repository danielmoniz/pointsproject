from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
#from django.template import RequestContext

def home(request):
    #return HttpResponse('test')
    return render_to_response('social/home.html')
