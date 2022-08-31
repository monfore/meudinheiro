from django.shortcuts import render
from django.http import HttpResponse

def principal(request):
    template_name = 'base.html'
    return render(request, template_name, {})




