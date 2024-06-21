from django.shortcuts import render
from django.http import HttpResponse

def home_page_view(request, *args, **kwargs):
    html_template = "home.html"
    return render(request, html_template)