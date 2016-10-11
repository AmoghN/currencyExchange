# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    q = "NONE"
    if 'q' in request.GET:
        q = request.GET['q']
    return render(request, 'index.html', {'q': q})
