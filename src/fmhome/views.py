from django.shortcuts import render
from django.http import HttpResponse

from usrvisit.models import PageVisit

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    html_template = "home.html"
    my_content = {
        "page_details": page_qs.count(),
    }
    path = request.path
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_content)