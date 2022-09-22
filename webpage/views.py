import re
from django.shortcuts import render

from django.http import HttpResponse



def index_view(request):
    return render(request,'website/index.html')

# def index(requset):
#     return HttpResponse('<h1> heloo </h1>')

