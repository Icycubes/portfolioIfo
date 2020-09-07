from django.shortcuts import render
from django.http import HttpResponse
#import datetime

# Create your views here.
def index(request):
    #hoy = datetime.datetime.now()
    #html = "<html><body><p>La fecha de hoy</p> %s.</body></html>" % hoy
    #return HttpResponse(html)
    texto = {'mensaje_texto':'Este es mi primer mensaje :)',}
    return render(request, 'index.html', context=texto)
    